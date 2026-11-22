## Langchain
---

LangChain is an open source orchestration framework for application development using large language models (LLMs). Available in both Python- and Javascript-based libraries, LangChain’s tools and APIs simplify the process of building LLM-driven applications like chatbots and AI agents. 

LangChain serves as a generic interface for nearly any LLM, providing a centralized development environment to build LLM applications and integrate them with external data sources and software workflows. LangChain’s module-based approach allows developers and data scientists to dynamically compare different prompts and even different foundation models with minimal need to rewrite code. This modular environment also allows for programs that use multiple LLMs: for example, an application that uses one LLM to interpret user queries and another LLM to author a response.


#### Key Components and Ecosystem
---

- **Models & Prompts**: Provides unified interfaces to swap between LLMs (such as OpenAI, Google, AWS, and open-source models) along with prompt templates and output parsers.
- **Chains & Workflows**: Connects sequences of steps—such as retrieving data, prompting a model, and formatting output—using composable syntax like LangChain Expression Language (LCEL).
- **Retrieval (RAG)**: Connects document loaders, text splitters, and vector databases so models can answer questions using private or real-time data.
- **Agents & Memory**: Enables models to use external tools or APIs, maintain conversation history, and run stateful workflows via LangGraph.
- **Observability & Deployment**: Pairs with LangSmith for tracing, testing, evaluation, and monitoring across the agent development lifecycle.

#### Common Usage Examples

- **Knowledge-base chatbots**: Answering questions grounded in company documents or databases through Retrieval-Augmented Generation (RAG).
- **AI agents and assistants**: Automating multi-step tasks by calling APIs, searching the web, or interacting with software tools.
• **Document and code workflows**: Summarizing long texts, extracting structured data, and analyzing code.

#### Similar Frameworks and Alternatives

Because LangChain is a specific software framework rather than a standalone word, it does not have exact lexical synonyms. In AI development, developers often compare it with similar LLM orchestration and agent frameworks—such as **LlamaIndex (especially for data indexing and RAG), Semantic Kernel, Haystack, or custom SDKs** built directly on model APIs.

### Table of Contents
---

| S.No. | Topic |
|---|---|
| 1 | Agent Creation using `create_agent` |
| 2 | Model Integration using OpenAI, Gemini, and Groq API Keys |
| 3 | `ChatOpenAI`, `ChatGoogleGenerativeAI`, `ChatGroq` |
| 4 | Streaming |
| 5 | Batching |
| 6 | Tools |
| 7 | Tools Execution Loop |
| 8 | Messages - Text Prompt |
| 9 | Message Prompt - System Prompt, Human Prompt, AI Prompt, Tool Prompt |
| 10. | Conversation History |
| 11. | Structured Output - Pydantic (Message output alongside parsed structure, Nested Structure) |
| 11. | Structured Output - TypedDict |
| 12. | Structured Output - Dataclass |
| 13. | Middleware and uses |
| 14. | Middleware (Built-in) - Summarization Middleware|
| 15. | Middleware (Built-in) - Human in the Loop|

### Installation
---

Initialise the project

```uv init```

Install the required dependencies

```uv add langchain langchain-openai langchain-community langchain-google-genai google-generativeai python-dotenv langchain-core langchain-experimental google-genai faiss-cpu tiktoken faiss-cpu rank-bm25 ctransformers```

Create a Virtual Environment

```uv venv```

Activate the envirenment

```.venv\Scripts\activate```

Install the requirements

```uv add -r requirements.txt```

Add the API keys in .env file

Install new library for jupyter notobeeok

```uv add ipykernel```

Modern pure-LangChain agents must be imported from the classic package
```uv add langchain-classic```

