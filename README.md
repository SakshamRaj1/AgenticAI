# Agentic AI & Retrieval-Augmented Generation (RAG) Monorepo

A consolidated collection of hands-on implementations, architectures, and experiments covering **Agentic AI**, **Multi-Agent Workflows**, **Model Context Protocol (MCP)**, **Guardrails**, **LLM Gateways**, **Evaluation Pipelines**, **Guardrails** and **Vector / Vectorless RAG** systems.

---

## Repository Structure

| Module | Description | Core Stack |
| :--- | :--- | :--- |
| **`langchainnew/`** | Modern LangChain v0.3+ primitives, LCEL (LangChain Expression Language) chains, structured outputs, and memory patterns. | LangChain, LCEL, Python |
| **`langgraphnew/`** | Stateful, cyclic, and multi-agent graph workflows featuring conditional routing, human-in-the-loop checkpoints, and state persistence. | LangGraph, LangChain |
| **`mcpdemo-langgraph/`** | Integration of the **Model Context Protocol (MCP)** with LangGraph agents to connect external tools, servers, and context sources dynamically. | MCP, LangGraph, Python |
| **`vectorRAG/`** | End-to-end semantic Retrieval-Augmented Generation pipelines covering document ingestion, chunking, embedding generation, and vector store querying. | Python, Vector Stores, Embeddings |
| **`vectorlessRAG/`** | Tree-based and reasoning-driven retrieval architectures (such as PageIndex) that navigate structured documents without relying on vector embeddings. | Python, Groq, PageIndex |
| **`deepagentsBasics/`** | Foundations of autonomous and multi-step deep agent architectures, planning loops, and tool-calling workflows. | Python, LangChain, DeepAgents |
| **`llmEval/`** | Automated evaluation frameworks for benchmarking LLM responses, RAG faithfulness, relevance, and latency metrics. | Python, LLM Evaluators |
| **`llmGateways/`** | Unified API routing, fallback handling, rate-limit management, and multi-provider model orchestration. | Python, LLM Gateway APIs |
| **`guardrailsLangchain/`** | Input/output validation, model-based safety guardrails, hallucination mitigation, and policy enforcement for LLM pipelines. | LangChain, Groq / Gemini |

---

## Prerequisites & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/SakshamRaj1/AgenticAI.git](https://github.com/SakshamRaj1/AgenticAI.git)
   cd AgenticAI

2. Create and activate a virtual environment:
```
Bash
python -m venv .venv
# Windows (Git Bash / PowerShell)
source .venv/Scripts/activate
```
```
# Linux / macOS
source .venv/bin/activate
Install dependencies:
Navigate into the specific sub-project folder you want to run and install its requirements (using uv or pip):
```

3. Install dependencies:
```
Bash
cd langgraphnew
pip install -r requirements.txt
```

4. Configure environment variables:
   Configure environment variables: Each sub-project loads its own .env file locally (ignored by Git). Create a .env file inside the sub-project directory you are running and add the required API keys:

```
GROQ_API_KEY="your_groq_api_key"
GOOGLE_API_KEY="your_google_gemini_api_key"
TAVILY_API_KEY="your_tavily_api_key"
LANGCHAIN_API_KEY="your_langsmith_api_key"
LANGCHAIN_TRACING_V2="true"
GOOGLE_API_KEY = "your_api_key_gemini"
GROQ_API_KEY = "your_api_key_groq"
OPENAI_API_KEY = "your_api_key_openai"
TAVILY_API_KEY = "your_api_key_tavily"
HF_TOKEN = "your_api_key_hf"
PAGEINDEX_API_KEY = "your_api_key_pageindex"
LANGSMITH_API_KEY = "your_api_key_langsmith"
OPENROUTER_API_KEY = "your_api_key_openrouter"
NVIDIA_API_KEY = "your_api_key_nvidia"
```

### Key Concepts Covered
- Orchestration & State Machines: Deterministic vs. agentic routing using StateGraph, nodes, conditional edges, and checkpointing in LangGraph.

- Tool Use & MCP: Exposing Python functions and Model Context Protocol servers as standardized tools for autonomous agents.

- Retrieval Paradigms: Comparing dense embedding similarity (vectorRAG) against hierarchical tree-search retrieval (vectorlessRAG).

- Production Reliability: Implementing guardrails, unified LLM gateways, and systematic evaluation loops before deployment.

Author: Saksham Raj

GitHub: @SakshamRaj1


### Push `README.md` to GitHub
Run these commands in Git Bash from your main repository folder:

```bash
git add README.md
git commit -m "docs: add comprehensive root README.md"
git push
```
