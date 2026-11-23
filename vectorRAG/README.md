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

