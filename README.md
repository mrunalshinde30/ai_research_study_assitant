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
