# 🤖 AI Research & Study Assistant

An AI-powered PDF question-answering application built using **Retrieval-Augmented Generation (RAG)**.

Upload a research paper, study material, or technical document and ask questions about it using natural language. The application retrieves relevant content from the document and uses a local LLM to generate grounded answers.

## ✨ Features

- PDF document upload
- Semantic search
- MMR-based retrieval
- Cross-Encoder reranking
- Local Llama 3.2 LLM
- Source page references
- Streamlit web interface
- Local processing

## 🏗️ Architecture

```text
PDF
 ↓
Text Extraction
 ↓
Text Chunking
 ↓
HuggingFace Embeddings
 ↓
ChromaDB
 ↓
MMR Retrieval
 ↓
Cross-Encoder Reranking
 ↓
Llama 3.2
 ↓
Answer + Sources

🛠️ Tech Stack
Python
Streamlit
LangChain
ChromaDB
HuggingFace Embeddings
Sentence Transformers
Cross-Encoder
Ollama
Llama 3.2
PyPDF
⚙️ Installation
1. Clone the repository
git clone https://github.com/mrunalshinde30/ai_research_study_assistant.git
cd ai_research_study_assistant
2. Create a virtual environment
python -m venv venv
3. Activate the environment

Windows PowerShell:

venv\Scripts\Activate.ps1
4. Install dependencies
pip install -r requirements.txt
5. Install the Llama model

Install Ollama and download the required model:

ollama pull llama3.2:3b
6. Run the application
streamlit run app.py
📂 Project Structure
ai_research_study_assistant/
│
├── app.py
├── rag.py
├── requirements.txt
├── .gitignore
└── README.md
🔍 How It Works
The user uploads a PDF.
The document is split into smaller chunks.
Chunks are converted into embeddings and stored in ChromaDB.
MMR retrieves relevant document chunks.
A Cross-Encoder reranks the retrieved results.
The most relevant context is sent to Llama 3.2.
The generated answer and source pages are displayed.
📈 Current Implementation
PDF upload and text extraction
Local embeddings
ChromaDB vector storage
MMR retrieval
Cross-Encoder reranking
Llama 3.2 integration
Source page display
Streamlit interface
🚀 Future Improvements
Chat history
Multiple PDF support
Document summarization
Better citations
Streaming responses
RAG evaluation
Improved UI
Deployment
👩‍💻 Author

Mrunal Shinde

B.Tech Computer Science Engineering
