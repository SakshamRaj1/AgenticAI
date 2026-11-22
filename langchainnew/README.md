### Table of Contents

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

