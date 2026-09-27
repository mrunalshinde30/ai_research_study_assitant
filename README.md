# 🤖 AI Research & Study Assistant

An AI-powered PDF question-answering application that uses **Retrieval-Augmented Generation (RAG)** to help users understand research papers, study materials, and technical documents.

The application retrieves relevant information from an uploaded PDF and uses a local LLM to generate grounded answers based on the document.

---

## ✨ Features

- 📄 Upload and process PDF documents
- 🔍 Semantic search over document content
- 🧠 Retrieval-Augmented Generation (RAG)
- 🎯 MMR-based document retrieval for diverse results
- 🔄 Cross-Encoder reranking for improved relevance
- 🤖 Local Llama 3.2 LLM through Ollama
- 📚 Displays source pages used to generate answers
- 🔐 Runs locally without requiring paid LLM API credits
- ⚡ Built with Python and Streamlit

---

## 🏗️ Architecture

```text
                 ┌─────────────────┐
                 │    PDF Upload   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   PDF Loader    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Text Chunking   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │    Embeddings   │
                 │ MiniLM-L6-v2    │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │    ChromaDB     │
                 │ Vector Database │
                 └────────┬────────┘
                          │
                    User Question
                          │
                          ▼
                 ┌─────────────────┐
                 │ MMR Retrieval   │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Cross-Encoder   │
                 │   Reranking     │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │   Llama 3.2     │
                 │     Ollama      │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ Answer + Sources│
                 └─────────────────┘


🛠️ Tech Stack
Technology	Purpose
Python	Core programming language
Streamlit	Web application interface
LangChain	RAG pipeline orchestration
ChromaDB	Vector database
HuggingFace	Text embeddings
Sentence Transformers	Embeddings and reranking
Cross-Encoder	Document reranking
Ollama	Local LLM inference
Llama 3.2	Generative language model
PyPDF	PDF text extraction
🔎 How RAG Works

The application follows a Retrieval-Augmented Generation pipeline:

User uploads a PDF.
The PDF is converted into text.
The text is split into smaller chunks.
Each chunk is converted into a vector embedding.
The embeddings are stored in ChromaDB.
The user's question is converted into an embedding.
MMR retrieval finds relevant document chunks.
A Cross-Encoder reranks the retrieved chunks.
The most relevant chunks are provided to Llama 3.2.
The model generates an answer using the retrieved context.
The application displays the answer along with source pages.
## ⚙️ Installation

## 1. Clone the repository


git clone https://github.com/mrunalshinde30/ai_research_study_assistant.git
cd ai_research_study_assistant
2. Create and activate a virtual environment
python -m venv venv

Windows PowerShell:

venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Install and run Ollama

Download Ollama and pull the required model:

ollama pull llama3.2:3b

Make sure Ollama is running.

5. Run the application
streamlit run app.py

The application will open in your browser.


💡 Example Questions

After uploading a research paper, you can ask questions such as:

What is Retrieval-Augmented Generation?

What problem does the paper address?

What are the main components of the proposed architecture?

What datasets were used?

What are the limitations discussed in the paper?

Summarize the methodology used in the paper.
📚 Retrieval Pipeline

This project uses a two-stage retrieval approach:

Stage 1 — MMR Retrieval

Maximum Marginal Relevance retrieves multiple relevant but diverse chunks from the document.

Question
   ↓
Vector Search
   ↓
MMR Retrieval
   ↓
12 Candidate Documents
Stage 2 — Cross-Encoder Reranking

The retrieved candidates are then scored using a Cross-Encoder.

12 Candidate Documents
        ↓
Cross-Encoder
        ↓
Relevance Scores
        ↓
Top 5 Documents
        ↓
Llama 3.2

This allows the system to perform retrieval first and then apply a more precise relevance ranking before generating the final answer.

🔐 Privacy

The application is designed to run locally.

Documents are processed on the local machine and the project uses a local LLM through Ollama rather than requiring a paid cloud LLM API.

API keys and local generated files are excluded from Git using .gitignore.

## 📈 Current Implementation

- PDF upload and text extraction
- Text chunking and local embeddings
- ChromaDB vector storage
- MMR-based retrieval
- Cross-Encoder reranking
- Local Llama 3.2 LLM
- Source page display
- Streamlit interface

## 🚀 Future Improvements

- Conversational chat history
- Multiple PDF support
- Document summarization
- Better citations
- Streaming responses
- RAG evaluation
- Improved UI/UX
- Deployment with Docker
👩‍💻 Author

Mrunal Shinde

B.Tech Computer Science Engineering

GitHub: @mrunalshinde30

⭐ Project Goal

The goal of this project is to explore modern Generative AI, RAG, vector databases, semantic search, and document intelligence by building a practical research and study assistant.


### Then on GitHub

At the bottom:

**Commit changes** → message:

```text
Add project documentation

→ Commit changes

After that, don't add anything else yet.

We'll next work in VS Code and make the app more impressive — particularly the chat history + better UI + multi-PDF capability, and we'll update GitHub as we go.

give proper

Yes — let’s make the README proper, professional, and portfolio-ready, not overly long or full of unnecessary claims.

Paste this as your complete README.md:

# 🤖 AI Research & Study Assistant

An AI-powered PDF question-answering application built using **Retrieval-Augmented Generation (RAG)**.

The application allows users to upload a PDF, retrieve relevant information from the document, and ask questions using a **local Large Language Model (LLM)**. It combines semantic search, MMR retrieval, and Cross-Encoder reranking to improve the relevance of the context provided to the language model.

---

## 📌 Overview

Reading and understanding long research papers or technical documents can be time-consuming.

This project provides an interactive way to query documents using natural language.

Instead of sending the entire document to an LLM, the system:

1. Extracts text from the PDF.
2. Splits the text into smaller chunks.
3. Converts the chunks into vector embeddings.
4. Stores the embeddings in a vector database.
5. Retrieves relevant chunks for a user's question.
6. Reranks the retrieved chunks using a Cross-Encoder.
7. Sends the most relevant context to a local LLM.
8. Generates an answer based on the retrieved document content.
9. Displays the source pages used for the answer.

---

## ✨ Features

- 📄 PDF document upload
- 🔎 Semantic document search
- 🧠 Retrieval-Augmented Generation (RAG)
- 🎯 Maximum Marginal Relevance (MMR) retrieval
- 🔄 Cross-Encoder document reranking
- 🤖 Local LLM inference using Ollama
- 📚 Source page references
- 🔐 Local document processing
- 💻 Streamlit-based web interface

---

## 🏗️ System Architecture

```text
                  PDF Document
                       │
                       ▼
               ┌───────────────┐
               │  PDF Loader   │
               └───────┬───────┘
                       │
                       ▼
             ┌───────────────────┐
             │  Text Chunking    │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │  HuggingFace     │
             │    Embeddings     │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │     ChromaDB      │
             │   Vector Store    │
             └─────────┬─────────┘
                       │
                 User Question
                       │
                       ▼
             ┌───────────────────┐
             │  MMR Retrieval    │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │ Cross-Encoder     │
             │    Reranking      │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │    Llama 3.2      │
             │      Ollama       │
             └─────────┬─────────┘
                       │
                       ▼
             ┌───────────────────┐
             │ Answer + Sources  │
             └───────────────────┘
🧠 RAG Pipeline
1. Document Processing

The uploaded PDF is loaded using PyPDFLoader.

The extracted text is divided into smaller overlapping chunks using RecursiveCharacterTextSplitter.

2. Embedding Generation

Each text chunk is converted into a numerical vector using:

sentence-transformers/all-MiniLM-L6-v2

These vectors represent the semantic meaning of the document chunks.

3. Vector Storage

The embeddings are stored in ChromaDB, which allows efficient similarity-based retrieval.

4. MMR Retrieval

For each user question, the system retrieves candidate chunks using Maximum Marginal Relevance (MMR).

MMR helps retrieve relevant information while reducing unnecessary duplication between retrieved chunks.

5. Cross-Encoder Reranking

The retrieved candidate documents are passed through:

cross-encoder/ms-marco-MiniLM-L-6-v2

The Cross-Encoder scores the relevance between the user's question and each retrieved document.

The highest-scoring documents are selected as the final context.

6. Answer Generation

The selected context is passed to:

Llama 3.2 3B through Ollama

The model generates an answer using the retrieved document context.

🛠️ Tech Stack
Technology	Purpose
Python	Application development
Streamlit	Web interface
LangChain	RAG pipeline
PyPDF	PDF text extraction
HuggingFace Embeddings	Text embeddings
Sentence Transformers	Embeddings and reranking
ChromaDB	Vector database
Ollama	Local LLM runtime
Llama 3.2	Answer generation
📂 Project Structure
ai_research_study_assistant/
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
app.py

Contains the Streamlit user interface.

rag.py

Contains the document processing, vector database, retrieval, reranking, and LLM generation logic.

requirements.txt

Contains the Python dependencies required to run the project.

.gitignore

Prevents sensitive and generated files such as .env, venv, and chroma_db from being uploaded to GitHub.

🚀 Getting Started
Prerequisites

Make sure the following are installed:

Python 3.10+
Git
Ollama
1. Clone the repository
git clone https://github.com/mrunalshinde30/ai_research_study_assistant.git

Navigate into the project:

cd ai_research_study_assistant
2. Create a virtual environment
python -m venv venv

Activate it on Windows PowerShell:

venv\Scripts\Activate.ps1
3. Install dependencies
pip install -r requirements.txt
4. Install the Llama model

Make sure Ollama is installed and then run:

ollama pull llama3.2:3b
5. Run the application
streamlit run app.py

The Streamlit application will open in your browser.

💬 Example Questions

After uploading a research paper, users can ask questions such as:

What is Retrieval-Augmented Generation?

What problem does this paper address?

What methodology is used in the paper?

What are the main components of the proposed system?

What datasets were used?

What are the limitations of the approach?

Summarize the main findings of the paper.
🔐 Privacy & Local Processing

The project is designed to use local models for embeddings and generation.

Document processing happens locally.
Embeddings are generated locally.
The Llama model runs through Ollama.
API keys and environment files are excluded using .gitignore.
📈 Current Implementation
Completed
 PDF upload
 PDF text extraction
 Text chunking
 Local text embeddings
 ChromaDB vector storage
 Semantic retrieval
 MMR retrieval
 Cross-Encoder reranking
 Local Llama 3.2 generation
 Source page display
 Streamlit interface
Planned Improvements
 Conversational chat history
 Multiple PDF support
 Document summarization
 Improved citation display
 Streaming LLM responses
 Retrieval evaluation
 RAG evaluation metrics
 Improved UI/UX
 Docker support
 Deployment
🎯 Learning Goals

This project is designed to explore practical applications of:

Retrieval-Augmented Generation
Large Language Models
Vector databases
Semantic search
Document intelligence
Embeddings
Reranking
Local AI inference
LangChain
👩‍💻 Author

Mrunal Shinde

B.Tech Computer Science Engineering

GitHub: @mrunalshinde30

⭐ Project

AI Research & Study Assistant

Built to experiment with modern RAG architectures and create a practical AI tool for research and study.


### Then

At the bottom of GitHub:

**Commit changes**

Commit message:

```text
Add professional project README

Then click Commit changes.

After committing, your repository homepage will look much more like a proper portfolio project.

Don't worry about adding screenshots yet. We'll actually improve the application first, then take a clean screenshot of the working app and add a Demo section with it.

se give full readme as i can copy the full text and paste

Absolutely. Copy everything inside this box and paste it into README.md on GitHub:

# 🤖 AI Research & Study Assistant

An AI-powered PDF question-answering application built using **Retrieval-Augmented Generation (RAG)**.

The application allows users to upload a PDF document and ask questions about its content using natural language. It retrieves relevant information from the document and uses a local Large Language Model (LLM) to generate grounded answers.

---

## 📌 Overview

Research papers, technical documentation, and study materials can contain large amounts of information that are difficult to search manually.

The **AI Research & Study Assistant** provides an interactive way to query these documents.

The application uses a Retrieval-Augmented Generation pipeline to:

1. Extract text from an uploaded PDF.
2. Split the document into smaller chunks.
3. Generate vector embeddings for the chunks.
4. Store the embeddings in a vector database.
5. Retrieve relevant document sections for a user's question.
6. Rerank the retrieved sections using a Cross-Encoder.
7. Provide the most relevant context to a local LLM.
8. Generate an answer based on the document.
9. Display the source pages used for the answer.

---

## ✨ Features

- 📄 Upload PDF documents
- 🔎 Semantic search over document content
- 🧠 Retrieval-Augmented Generation (RAG)
- 🎯 Maximum Marginal Relevance (MMR) retrieval
- 🔄 Cross-Encoder reranking
- 🤖 Local LLM inference using Ollama
- 📚 Source page references
- 💻 Streamlit web interface
- 🔐 Local document processing
- ⚡ No paid LLM API required for the core pipeline

---

## 🏗️ Architecture

```text
                     PDF Document
                          │
                          ▼
                  ┌───────────────┐
                  │   PDF Loader  │
                  └───────┬───────┘
                          │
                          ▼
                ┌───────────────────┐
                │   Text Chunking   │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ HuggingFace       │
                │ Embeddings        │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │     ChromaDB      │
                │   Vector Store    │
                └─────────┬─────────┘
                          │
                    User Question
                          │
                          ▼
                ┌───────────────────┐
                │  MMR Retrieval    │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Cross-Encoder     │
                │    Reranking      │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │    Llama 3.2      │
                │      Ollama       │
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ Answer + Sources  │
                └───────────────────┘
🧠 RAG Pipeline
1. PDF Processing

The uploaded PDF is loaded using PyPDFLoader.

The extracted text is divided into smaller overlapping chunks using RecursiveCharacterTextSplitter.

2. Embedding Generation

Each document chunk is converted into a vector representation using:

sentence-transformers/all-MiniLM-L6-v2

These embeddings capture the semantic meaning of the document chunks.

3. Vector Database

The generated embeddings are stored in ChromaDB.

ChromaDB allows the application to efficiently search for document chunks that are semantically related to the user's question.

4. MMR Retrieval

The application uses Maximum Marginal Relevance (MMR) to retrieve relevant and diverse document chunks.

Instead of retrieving only highly similar chunks, MMR also reduces redundancy between the retrieved results.

5. Cross-Encoder Reranking

The retrieved candidate documents are then passed through:

cross-encoder/ms-marco-MiniLM-L-6-v2

The Cross-Encoder evaluates the relevance between the user's question and each candidate document.

The highest-scoring documents are selected as the final context.

6. Answer Generation

The selected context is provided to:

Llama 3.2 3B through Ollama

The model generates an answer using the retrieved document content.

🛠️ Tech Stack
Technology	Purpose
Python	Core application development
Streamlit	Web application interface
LangChain	RAG pipeline orchestration
PyPDF	PDF text extraction
HuggingFace Embeddings	Text embeddings
Sentence Transformers	Embeddings and reranking
ChromaDB	Vector database
Ollama	Local LLM runtime
Llama 3.2	Answer generation
📂 Project Structure
ai_research_study_assistant/
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
app.py

Contains the Streamlit user interface for:

Uploading PDFs
Processing documents
Entering questions
Displaying generated answers
Displaying source information
rag.py

Contains the core RAG pipeline:

PDF loading
Text chunking
Embedding generation
ChromaDB vector storage
MMR retrieval
Cross-Encoder reranking
Llama 3.2 response generation
requirements.txt

Contains the Python dependencies required to run the application.

.gitignore

Prevents sensitive and generated files from being uploaded to GitHub, including:

.env
venv
chroma_db
Python cache files
🚀 Getting Started
Prerequisites

Make sure the following are installed:

Python 3.10+
Ollama
Git
1. Clone the Repository
git clone https://github.com/mrunalshinde30/ai_research_study_assistant.git

Navigate into the project:

cd ai_research_study_assistant
2. Create a Virtual Environment
python -m venv venv

Activate the environment on Windows PowerShell:

venv\Scripts\Activate.ps1
3. Install Dependencies
pip install -r requirements.txt
4. Install the LLM

Install Ollama and download the Llama 3.2 model:

ollama pull llama3.2:3b

Make sure Ollama is running before starting the application.

5. Run the Application
streamlit run app.py

The Streamlit application will open in your browser.

💬 Example Questions

After uploading a research paper or study document, users can ask questions such as:

What is Retrieval-Augmented Generation?

What problem does this paper address?

What methodology is used in the paper?

What are the main components of the proposed system?

What datasets were used?

What are the limitations of the approach?

What are the main findings of the paper?

Summarize the methodology used in the paper.
🔍 Retrieval Strategy

The project uses a two-stage retrieval pipeline.

Stage 1 — MMR Retrieval

The system first retrieves multiple candidate documents using Maximum Marginal Relevance.

User Question
      │
      ▼
Semantic Search
      │
      ▼
MMR Retrieval
      │
      ▼
Candidate Documents

MMR helps balance:

Relevance to the question
Diversity among retrieved chunks
Stage 2 — Cross-Encoder Reranking

The candidate documents are then reranked using a Cross-Encoder.

Candidate Documents
        │
        ▼
Cross-Encoder
        │
        ▼
Relevance Scores
        │
        ▼
Top Relevant Documents
        │
        ▼
Llama 3.2

This two-stage approach allows the system to perform broad retrieval first and then apply more precise relevance scoring before generating the final answer.

🔐 Privacy & Local Processing

The project is designed around local processing.

PDF documents are processed locally.
Embeddings are generated locally.
ChromaDB runs locally.
The Llama model runs locally through Ollama.
Sensitive environment files are excluded using .gitignore.

No API key is required for the current local LLM pipeline.

📈 Current Implementation
Completed
 PDF upload
 PDF text extraction
 Text chunking
 Local embeddings
 ChromaDB vector storage
 Semantic retrieval
 MMR retrieval
 Cross-Encoder reranking
 Local Llama 3.2 generation
 Source page display
 Streamlit interface
Future Improvements
 Conversational chat history
 Multiple PDF support
 Document summarization
 Improved citation display
 Streaming responses
 Retrieval evaluation
 RAG evaluation metrics
 Improved UI/UX
 Docker support
 Cloud deployment

🎯 Learning Goals

This project is being developed to explore practical applications of modern AI technologies, including:

Retrieval-Augmented Generation
Large Language Models
Vector databases
Semantic search
Text embeddings
Document intelligence
Cross-Encoder reranking
Local AI inference
LangChain
Generative AI application development
👩‍💻 Author

Mrunal Shinde

B.Tech Computer Science Engineering



⭐ Project Goal

The goal of this project is to build a practical AI research and study assistant while exploring modern RAG architectures, semantic retrieval, reranking, vector databases, and local Large Language Models.



