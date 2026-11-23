### Table of Contents

| Section | Sub-section / Component | Key Function / Class & Purpose |
| --- | --- | --- |
| **Setup & Dependencies** | Environment Imports | `DirectoryLoader`, `PyPDFLoader`, `PyMuPDFLoader`, `RecursiveCharacterTextSplitter`, `Path` |
| **1. Data Ingestion Pipeline to VectorStore** | **a) Data Ingestion** | `process_all_pdfs()` — Recursively loads PDF files and extracts page metadata |
|  | **b) Chunking** | `split_documents()` — Splits loaded documents into chunks with configurable size and overlap |
|  | **c) Embedding Generation** | `EmbeddingManager` — Generates dense vector embeddings via `SentenceTransformer` (`all-MiniLM-L6-v2`) |
|  | **d) VectorStore DB** | `VectorStore` — Persists document chunks and embeddings into a ChromaDB vector store |
| **2. RAG Retrieval Pipeline from VectorStore** | Query Retrieval | `RAGRetriever` — Encodes user queries and fetches top matching chunks with similarity thresholds |
| **3. Data Retrieval Pipeline - VectorDB To LLM Output Generation** | LLM Initialization | `GroqLLM` — Configures Groq API (`ChatGroq`) with `gemma2-9b-it` |
| **Integration Vectordb Context Pipeline With LLM Output** | Basic RAG Workflow | `rag_simple()` — Combines retrieved context with the LLM to generate basic answers |
| **Enhanced RAG Pipeline Features** | Configurable Retrieval | `rag_advanced()` — Adds `top_k` controls, minimum score filtering, and structured context formatting |
| **Advanced RAG Pipeline** | Production Features | `AdvancedRAGPipeline` — Supports streaming responses, source citations, query history, and summarization |

| S.No. | Topic | Description |
| --- | --- | --- |
| 1 | Setup & Dependencies | Imports required libraries and modules, including `DirectoryLoader`, `PyPDFLoader`, `PyMuPDFLoader`, `RecursiveCharacterTextSplitter`, and `Path`. |
| 2 | Data Ingestion Pipeline to VectorStore – Data Ingestion | `process_all_pdfs()` recursively loads PDF files and extracts document content along with page metadata. |
| 3 | Data Ingestion Pipeline to VectorStore – Chunking | `split_documents()` splits loaded documents into smaller chunks using configurable chunk size and overlap. |
| 4 | Data Ingestion Pipeline to VectorStore – Embedding Generation | `EmbeddingManager` generates dense vector embeddings using the SentenceTransformer model (`all-MiniLM-L6-v2`). |
| 5 | Data Ingestion Pipeline to VectorStore – VectorStore DB | `VectorStore` stores and persists document chunks and their embeddings in a ChromaDB vector database. |
| 6 | RAG Retrieval Pipeline from VectorStore | `RAGRetriever` encodes user queries and retrieves the top-matching document chunks based on similarity thresholds. |
| 7 | Data Retrieval Pipeline – VectorDB to LLM Output Generation | `GroqLLM` initializes and configures the Groq API using `ChatGroq` with the `gemma2-9b-it` model. |
| 8 | Integration of VectorDB Context Pipeline with LLM Output – Basic RAG Workflow | `rag_simple()` combines retrieved document context with the LLM to generate answers. |
| 9 | Enhanced RAG Pipeline Features – Configurable Retrieval | `rag_advanced()` provides configurable `top_k` retrieval, minimum score filtering, and structured context formatting. |
| 10 | Advanced RAG Pipeline – Production Features | `AdvancedRAGPipeline` supports streaming responses, source citations, query history, and summarization. |

### Initialise the project
```
uv init
```
Install the required dependencies
```
uv add langchain langchain-openai langchain-community langchain-google-genai google-generativeai python-dotenv langchain-core langchain-experimental google-genai faiss-cpu tiktoken faiss-cpu rank-bm25 ctransformers
```

Create a Virtual Environment
```
uv venv
```

Activate the envirenment
```
.venv\Scripts\activate
```

Install the requirements
```
uv add -r requirements.txt
```

Add the API keys in .env file

Install new library for jupyter notebook
```
uv add ipykernel
```

Modern pure-LangChain agents must be imported from the classic package
```
uv add langchain-classic
```

