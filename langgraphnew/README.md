# **Langgraph**
LangGraph, created by LangChain, is an open source AI agent framework designed to build, deploy and manage complex generative AI agent workflows. It provides a set of tools and libraries that enable users to create, run and optimize large language models (LLMs) in a scalable and efficient manner. At its core, LangGraph uses the power of graph-based architectures to model and manage the intricate relationships between various components of an AI agent workflow.
LangGraph is designed to build, manage, and deploy complex AI agent workflows using graph structures rather than linear pipelines. Each step in the workflow is a node, and transitions between steps are edges, enabling branching, looping, and multi‑agent coordination. 

### Key characteristics:

Graph‑based architecture for flexible control flows
Stateful execution with persistent memory
Cyclical graphs for iterative agent reasoning
Human‑in‑the‑loop (HITL) moderation and approval
Integration with LangChain tools and models
Support for multi‑agent and hierarchical agent systems


- **Graph-Based Architecture**: Organizes workflows using nodes (tasks) and edges (connections) to control how an AI agent executes tasks.

- **Stateful Execution with Persistent Memory**: Allows AI agents to store, remember, and maintain information throughout workflow execution.

- **Cyclical Graphs for Iterative Agent Reasoning**: Enables AI agents to repeat tasks, evaluate results, and improve outputs until a condition is met.

- **Human-in-the-Loop (HITL)**: Allows humans to review, approve, reject, or modify AI-generated decisions and actions.

- **Integration with LangChain Tools and Models**: Enables LangGraph to use different LLMs, external tools, APIs, and data sources.

- **Multi-Agent and Hierarchical Agent Systems**: Allows multiple specialized AI agents to collaborate, with a supervisor agent coordinating and delegating tasks.

### Common Usage Example

- Complex chatbots with memory
- Multi‑agent research assistants
- Workflow automation with LLMs
- Decision‑making systems with loops
- Enterprise‑grade agent pipelines with auditability


LangGraph provides a powerful, low‑level, graph‑based runtime for building reliable, stateful, and controllable AI agents. Its combination of state management, cyclical graphs, multi‑agent support, and human‑in‑the‑loop features makes it ideal for complex, production‑grade LLM applications.


### How LangGraph Fits in the LangChain Ecosystem

- LangChain: high‑level agent framework (models, tools, agent loops).
- LangGraph: low‑level orchestration runtime (state, execution, HITL).
- LangSmith: tracing, evaluation, debugging, deployment.
### Table of Contents

| S. No. | Topic | Description |
| --- | --- | --- |
| 1 | Build a Basic Chatbot with LangGraph (Graph API) | Create a basic chatbot using LangGraph's Graph API. |
| 2 | Nodes and Edges | Understand nodes, edges, and graph workflow. |
| 3 | Chatbot with Tools | Integrate external tools into a chatbot. |
| 4 | Tavily Search | Integrate Tavily Search for web search capabilities. |
| 5 | Tools Binding with LLM | Bind tools with an LLM for tool calling. |
| 6 | ReAct Agent Architecture | Understand the Reasoning and Acting (ReAct) agent architecture. |
| 7 | Adding Memory in Agentic Graph | Implement short-term and long-term memory in an agentic graph. |
| 8 | Streaming - `stream()` and `astream()` | Learn synchronous and asynchronous streaming. |
| 9 | Stream Modes - `updates`, `values` | Understand different streaming modes in LangGraph. |
| 10 | Human in the Loop / Fallback | Implement human approval, intervention, and fallback mechanisms. |
| 11 | MCP Server | Integrate Model Context Protocol (MCP) servers with LangGraph agents. |


Initialise the project
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
```uv add langchain-classic```

