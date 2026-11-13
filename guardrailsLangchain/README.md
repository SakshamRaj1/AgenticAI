Initialise the project
```uv init```Install the required dependencies
```uv add langchain langchain-openai langchain-community langchain-google-genai google-generativeai python-dotenv langchain-core langchain-experimental google-genai faiss-cpu tiktoken faiss-cpu rank-bm25 ctransformers
```

Create a Virtual Environment
```uv venv```

Activate the envirenment
```.venv\Scripts\activate```

Install the requirements
```uv add -r requirements.txt```

Add the API keys in .env file

Install new library for jupyter notebook
```uv add ipykernel```

Modern pure-LangChain agents must be imported from the classic package
```uv add langchain-classic```

