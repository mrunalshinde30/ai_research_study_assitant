from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import ChatOllama

from sentence_transformers import CrossEncoder


# --------------------------------------------------
# CREATE VECTOR DATABASE
# --------------------------------------------------

def create_vector_database(pdf_path):

    # Load PDF
    loader = PyPDFLoader(pdf_path)

    documents = loader.load()

    # Split document into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )

    chunks = text_splitter.split_documents(documents)

    if not chunks:
        raise ValueError(
            "No readable text was found in this PDF."
        )

    # Local embedding model
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    # Store embeddings in ChromaDB
    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory="chroma_db"
    )

    return vector_db


# --------------------------------------------------
# RERANK DOCUMENTS
# --------------------------------------------------

def rerank_documents(question, documents, top_k=5):

    # Cross-encoder reranker
    reranker = CrossEncoder(
        "cross-encoder/ms-marco-MiniLM-L-6-v2"
    )

    # Create question-document pairs
    pairs = [
        [question, document.page_content]
        for document in documents
    ]

    # Calculate relevance scores
    scores = reranker.predict(pairs)

    # Combine documents with scores
    ranked_documents = list(
        zip(documents, scores)
    )

    # Sort by relevance score
    ranked_documents.sort(
        key=lambda x: x[1],
        reverse=True
    )

    # Return best documents
    return [
        document
        for document, score in ranked_documents[:top_k]
    ]


# --------------------------------------------------
# ASK QUESTION
# --------------------------------------------------

def ask_question(vector_db, question):

    # Local Llama model
    llm = ChatOllama(
        model="llama3.2:3b",
        temperature=0
    )

    # Retrieve more candidates first
    retriever = vector_db.as_retriever(
        search_type="mmr",
        search_kwargs={
            "k": 12,
            "fetch_k": 30,
            "lambda_mult": 0.7
        }
    )

    # Initial retrieval
    candidate_documents = retriever.invoke(
        question
    )

    if not candidate_documents:
        return (
            "I couldn't find relevant information "
            "in the uploaded document.",
            []
        )

    # Rerank retrieved documents
    documents = rerank_documents(
        question,
        candidate_documents,
        top_k=5
    )

    # Combine the best retrieved chunks
    context = "\n\n".join(
        document.page_content
        for document in documents
    )

    # Grounded prompt
    prompt = f"""
You are an AI research and study assistant.

Answer the user's question using ONLY the
information contained in the context below.

Rules:

1. Use the provided context as your primary source.
2. Do not invent information.
3. Combine information from multiple sections
   when necessary.
4. Give a clear and useful explanation.
5. If the answer cannot be found in the context,
   say:

"I couldn't find this information in the
uploaded document."

CONTEXT:
{context}

QUESTION:
{question}

ANSWER:
"""

    # Generate answer
    response = llm.invoke(prompt)

    return response.content, documents