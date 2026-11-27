# **LiteLLM**
LiteLLM is an open-source AI gateway (LLM proxy) and Python SDK that puts over 100–140 AI model providers behind a single OpenAI-compatible API. Developed by BerriAI under an MIT license, it lets developers call models from providers like OpenAI, Anthropic, Google Gemini, Amazon Bedrock, and local runtimes like Ollama using one standardized request and response format.

### Key characteristics:

• Unified Interface: Translates inputs and outputs between different model APIs into a consistent OpenAI-style format so you can switch models without rewriting client code.
• Two Deployment Modes: Can be used directly inside code as a Python SDK or deployed as a self-hosted proxy server (including on-premises or air-gapped environments).
• Routing and Reliability: Supports model routing, load balancing, caching, and automatic retries or fallbacks if a provider fails.
• Governance and Cost Controls: Offers virtual API keys, rate limits, spend tracking, and budget caps per key, team, or model.
• Protocol and Tool Support: Supports Model Context Protocol (MCP) tools and agents alongside standard LLM calls.

### Common Usage Example

- Unified API for All LLM Providers - LLM gateways expose a single, consistent API so applications don’t need to handle different provider formats, authentication schemes, or response structures 
- Multi‑Provider Routing and Failover - They route requests across multiple LLMs, enabling provider agnosticism, intelligent routing, and automatic failover when a provider is down or rate‑limited 
- Centralized Security, Access Control, and Governance - Gateways enforce authentication, rate limits, RBAC/ABAC, PII masking, and other guardrails from one place 
- Observability, Monitoring, and Logging - They provide centralized logs, metrics, token usage tracking, and audit trails for debugging, compliance, and performance monitoring 
- Cost Management and Optimization - Gateways track token usage, enforce budgets, apply rate limits, and route to cheaper models when appropriate. Some also support caching to reduce repeated costs.


### Table of Contents

| S.no | Title | Explanation |
| --- | --- | --- |
| **1** | **Part 1: What is an LLM Gateway?** | Introduces the concept of an LLM Gateway as a middleware layer between applications and model providers (OpenAI, Anthropic, Google, Groq, etc.), contrasting the pain points of separate SDKs with the benefits of a unified API. |
| **2** | **Part 2: Installation & Setup** | Covers installing core libraries (`litellm`, `langchain`, `python-dotenv`), suppressing noisy debug logs/warnings, and verifying environment API keys for OpenAI, Anthropic, Groq, Gemini, OpenRouter, and Nvidia. |
| **3** | **Part 3: The Simplest LiteLLM Example — Unified API** | Demonstrates how to call multiple providers (Groq, Gemini, OpenRouter, Nvidia) using a single `completion()` function by simply changing the `model` string, including looping through a list of providers. |
| **4** | **Part 4: Automatic Fallbacks — When OpenAI Goes Down** | Shows how to configure a `fallbacks` list in `completion()` so that if a primary model fails (e.g., due to rate limits or nonexistent models), the gateway transparently retries with backup providers without crashing the app. |
| **5** | **Part 5: Cost Tracking — Know Where Your Money Goes** | Explains how to use `completion_cost()` to automatically calculate the exact USD cost, input tokens, and output tokens for every individual LLM API call. |
| **6** | **Part 6: Caching — Don't Pay Twice for the Same Question** | Demonstrates enabling local in-memory caching (`litellm.cache = Cache(type="local")`) to serve repeated prompts instantaneously at zero cost. |
| **7** | **Part 7: Smart Routing — The Right Model for the Right Job** | Introduces LiteLLM's `Router` class to map abstract model aliases (e.g., `"fast-cheap"`, `"smart-coding"`, `"balanced"`) to specific underlying models, allowing provider swaps via configuration rather than code rewrites. |
| **8** | **Part 8: Load Balancing & Routing Strategies** | Explores distributing traffic across multiple deployments using `Router` strategies, including `simple-shuffle`, **Strategy 1: `least-busy**` (fewest in-flight requests), **Strategy 2: `latency-based-routing**` (fastest response time), and **Strategy 3: Cost-based-routing** (cheapest per token). |
| **9** | **Part 9: Observability — Log Every Single Call** | Shows how to attach custom `success_callback` and `failure_callback` hooks to build an audit log tracking model usage, prompt snippets, token counts, latency, cost, and user attribution. |
| **10** | **Part 10: Integrating the Gateway with LangChain** | Demonstrates wrapping LiteLLM inside LangChain using `ChatLiteLLM` and composing it with `ChatPromptTemplate` and `StrOutputParser` via LangChain Expression Language (LCEL). |
| **11** | **Part 11: Multi-Provider LangChain Chain with Fallbacks** | Combines LangChain and LiteLLM by chaining a primary `ChatLiteLLM` model with backup models using `.with_fallbacks()`, enforcing structured JSON output even when the primary model errors out. |
| **12** | **Part 13: Mini End-to-End Demo — Smart Router for a Chatbot** | Builds a complete task-aware chatbot (`smart_chat`) that uses a fast classifier model to categorize queries (`code`, `summary`, or `general`), routes them to specialized fallback chains, and reports latency and cost. *(Note: Part 12 is skipped in the notebook's numbering).* |
| **13** | **Guardrails Stack (Input Callbacks)** | Implements three custom Python pre-call security guardrails via `litellm.input_callback`: **Guardrail 1** (regex-based PII redaction for emails, Indian/US phones, SSN, Aadhaar, PAN, credit cards, IPs), **Guardrail 2** (prompt injection & jailbreak blocking), and **Guardrail 3** (forbidden topic keyword filtering). |
| **14** | **Part 14: Production Best Practices** | Outlines 10 essential production readiness rules, including using Redis caching, per-user rate limits, observability backends (Langfuse/Helicone), virtual keys, version pinning, timeouts, health checks, Kubernetes HPA, and Git-versioned `config.yaml`. |
| **15** | **Part 15: Popular LLM Gateways Compared** | Compares six gateway solutions—**LiteLLM**, **Portkey**, **Helicone**, **Cloudflare AI Gateway**, **Kong AI Gateway**, and **OpenRouter**—by type (Open-source vs. SaaS/Enterprise) and ideal use case. |
| **16** | **Wrapping Up** | Provides a 5-point summary of the tutorial alongside links to [LiteLLM documentation](https://docs.litellm.ai/), [LangChain documentation](https://python.langchain.com/), and creator resources. |


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

