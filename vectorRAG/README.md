## 1. What is RAG?

Retrieval-Augmented Generation (RAG) is an AI architecture that combines information retrieval with Large Language Models (LLMs).

It retrieves relevant information from external knowledge sources and provides it to an LLM as context to generate accurate, context-aware responses.

Why RAG?

- Reduces LLM hallucinations.
- Provides access to updated information.
- Enables searching private or domain-specific documents.
- Avoids retraining the LLM whenever data changes.

## 2. RAG Pipeline Architecture

RAG Architectures: A Complete Guide for 2025 | Data Science Collective

[medium.com](<https://medium.com/data-science-collective/rag-architectures-a-complete-guide-for-2025-daf98a2ede8c>)

A RAG pipeline has two major stages:

1. Data Ingestion: Preparing and storing data.
2. Data Retrieval: Finding relevant information and generating answers.

## 3. Data Ingestion Pipeline

Data ingestion converts raw documents into searchable information.

### Step 1: Data Collection

Collect data from different sources:

- PDFs, DOCX, TXT files.
- Websites and APIs.
- SQL and NoSQL databases.
- Excel and CSV files.

### Step 2: Data Extraction

Extract text and meaningful content from documents.

Tools: PyPDF, PyMuPDF, Unstructured, Apache Tika.

### Step 3: Data Cleaning

Remove unwanted content and prepare clean data.

- Remove duplicate records.
- Remove unnecessary characters.
- Handle missing values.
- Normalize text.

### Step 4: Text Chunking

Divide large documents into smaller meaningful pieces called chunks.

Example: A 100-page PDF is divided into smaller sections of 500 tokens each.

Common strategies:

- Fixed-size chunking.
- Recursive chunking.
- Semantic chunking.

Important parameters:

- Chunk size.
- Chunk overlap.
- Separators.

### Step 5: Embedding Generation

Convert each text chunk into a numerical vector using an embedding model.

Example models:

- OpenAI Embeddings.
- BGE.
- Sentence Transformers.
- E5.

Example:

`"What is machine learning?"`

↓ Embedding model

`[0.21, 0.45, 0.78, 0.12, ...]`

These vectors represent the semantic meaning of the text.

### Step 6: Vector Database Storage

Store embeddings along with original text and metadata.

Popular vector databases:

- FAISS.
- ChromaDB.
- Pinecone.
- Weaviate.
- Milvus.

Metadata may include document name, page number, source, and timestamp.

## 4. Data Retrieval Pipeline

Data retrieval finds the most relevant information based on the user's question.

### Step 1: User Query

The user submits a question.

Example: "What is the company's leave policy?"

### Step 2: Query Embedding

Convert the user query into a numerical vector using an embedding model compatible with the document embeddings.

### Step 3: Similarity Search

Compare the query vector with stored document vectors to find relevant chunks.

Common techniques:

- Cosine similarity.
- Euclidean distance.
- Dot product.

### Step 4: Reranking

Reorder retrieved chunks based on their relevance to the query.

Common reranking models include cross-encoders and BGE Reranker.

### Step 5: Context Construction

Combine the most relevant chunks into a context and prepare the prompt.

Example:

text

```text
Context:
Employees receive 20 annual leave days.

Question:
What is the company's annual leave entitlement?

Instruction:
Answer using the provided context.
```

### Step 6: LLM Response Generation

Pass the context and user query to an LLM.

Examples:

- GPT.
- Llama.
- Claude.
- Gemini.

The LLM generates an answer grounded in the retrieved information.

### Step 7: Final Response

Return the generated answer to the user, optionally including document references and citations.

## 5. Important RAG Components

| Component | Purpose |
| --- | --- |
| Document Loader | Loads documents |
| Text Splitter | Divides documents into chunks |
| Embedding Model | Converts text into vectors |
| Vector Database | Stores and searches vectors |
| Retriever | Finds relevant chunks |
| Reranker | Improves retrieval relevance |
| LLM | Generates the final response |

## 6. Popular RAG Technology Stack

| Layer | Technologies |
| --- | --- |
| Programming | Python |
| Document Processing | PyMuPDF, Unstructured |
| Chunking | LangChain, LlamaIndex |
| Embeddings | OpenAI, BGE, Hugging Face |
| Vector Database | FAISS, ChromaDB, Pinecone |
| LLM | GPT, Llama, Gemini |
| Frameworks | LangChain, LlamaIndex |
| API Development | FastAPI |

## 7\. Simple RAG Example

Suppose you upload a company policy PDF and ask:

"How many sick leaves are employees entitled to?"

The RAG system works as follows:

1. Extracts text from the PDF.
2. Splits the text into chunks.
3. Generates embeddings.
4. Stores embeddings in a vector database.
5. Converts your question into an embedding.
6. Retrieves relevant chunks.
7. Sends retrieved context to the LLM.
8. Generates the final answer.

## 8\. Key Difference: Ingestion vs Retrieval

| Data Ingestion | Data Retrieval |
| --- | --- |
| Processes source documents | Processes user queries |
| Performs chunking | Performs similarity search |
| Generates document embeddings | Generates query embeddings |
| Stores vectors | Retrieves relevant vectors |
| Usually offline | Usually real-time |

In summary: Data ingestion prepares and indexes knowledge, while data retrieval searches that knowledge and provides relevant context to an LLM for answer generation.


### Table of Contents

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
| 11 | RAG Application Using Typesense – Setup & Client Initialization | Initializes the Typesense client and configures the connection to the Typesense server. |
| 12 | RAG Application Using Typesense – Collection Schema & Data Ingestion | Defines the Typesense collection schema and ingests documents into the collection. |
| 13 | RAG Application Using Typesense – Keyword, Filtered & Typo-Tolerant Search | Implements keyword-based search, filtered search, and typo-tolerant search using Typesense. |
| 14 | RAG Application Using Typesense – LangChain + Typesense Vector Store Integration | Integrates Typesense with LangChain to store and manage document embeddings for vector-based retrieval. |
| 15 | RAG Application Using Typesense – Similarity Search & Retriever Setup | Configures similarity search and retrievers to fetch relevant document chunks based on user queries. |

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

