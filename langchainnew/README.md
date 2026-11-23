# Langchain

LangChain is an open source orchestration framework for application development using large language models (LLMs). Available in both Python- and Javascript-based libraries, LangChain’s tools and APIs simplify the process of building LLM-driven applications like chatbots and AI agents. 

LangChain serves as a generic interface for nearly any LLM, providing a centralized development environment to build LLM applications and integrate them with external data sources and software workflows. LangChain’s module-based approach allows developers and data scientists to dynamically compare different prompts and even different foundation models with minimal need to rewrite code. This modular environment also allows for programs that use multiple LLMs: for example, an application that uses one LLM to interpret user queries and another LLM to author a response.


#### Key Components and Ecosystem
---

- **Models & Prompts**: Provides unified interfaces to swap between LLMs (such as OpenAI, Google, AWS, and open-source models) along with prompt templates and output parsers.
- **Chains & Workflows**: Connects sequences of steps-such as retrieving data, prompting a model, and formatting output-using composable syntax like LangChain Expression Language (LCEL).
- **Retrieval (RAG)**: Connects document loaders, text splitters, and vector databases so models can answer questions using private or real-time data.
- **Agents & Memory**: Enables models to use external tools or APIs, maintain conversation history, and run stateful workflows via LangGraph.
- **Observability & Deployment**: Pairs with LangSmith for tracing, testing, evaluation, and monitoring across the agent development lifecycle.

#### Common Usage Examples

- **Knowledge-base chatbots**: Answering questions grounded in company documents or databases through Retrieval-Augmented Generation (RAG).
- **AI agents and assistants**: Automating multi-step tasks by calling APIs, searching the web, or interacting with software tools.
• **Document and code workflows**: Summarizing long texts, extracting structured data, and analyzing code.

#### Similar Frameworks and Alternatives

Because LangChain is a specific software framework rather than a standalone word, it does not have exact lexical synonyms. In AI development, developers often compare it with similar LLM orchestration and agent frameworks-such as **LlamaIndex (especially for data indexing and RAG), Semantic Kernel, Haystack, or custom SDKs** built directly on model APIs.

### Table of Contents
---

| S.No. | Topic | Description |
| --- | --- | --- |
| 1 | Agent Creation using `create_agent` | Create and configure AI agents. |
| 2 | Model Integration (OpenAI, Gemini, Groq) | Connect LLM providers using API keys. |
| 3 | `ChatOpenAI`, `ChatGoogleGenerativeAI`, `ChatGroq` | Initialize and configure chat models. |
| 4 | Streaming | Generate responses token by token. |
| 5 | Batching | Process multiple inputs efficiently. |
| 6 | Tools | Create and integrate custom and built-in tools. |
| 7 | Tools Execution Loop | Understand tool calling and execution flow. |
| 8 | Messages - Text Prompt | Send text prompts to LLMs. |
| 9 | Message Prompts | Understand System, Human, AI, and Tool messages. |
| 10 | Conversation History | Maintain context across conversations. |
| 11 | Structured Output - Pydantic | Generate validated and nested structured outputs. |
| 12 | Structured Output - TypedDict | Define structured outputs using TypedDict. |
| 13 | Structured Output - Dataclass | Generate structured outputs using dataclasses. |
| 14 | Middleware and Uses | Customize agent behavior using middleware. |
| 15 | Summarization Middleware | Summarize conversations using length, token, and fraction thresholds. |
| 16 | Human in the Loop | Add human approval and intervention to workflows. |

### Installation
---

Initialise the project

```
uv init
```

Create a Virtual Environment

```
uv venv
```

Activate the envirenment

```
.venv\Scripts\activate
```

Install the required dependencies

```
uv add langchain langchain-community langchain-openai langchain-groq langchain-google-genai python-dotenv
```

Install the requirements

```
uv add -r requirements.txt
```

Add the API keys in .env file

Install new library for jupyter notobeeok

```
uv add ipykernel
```

Modern pure-LangChain agents must be imported from the classic package
```uv add langchain-classic```

