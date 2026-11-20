# API Setup for Generative AI

## 1. Introduction

An API (Application Programming Interface) allows two software applications to communicate with each other.

In Generative AI, APIs allow our Python applications to communicate with Large Language Models (LLMs).

Instead of running a large AI model locally, we can send requests to an AI provider and receive generated responses.

## 2. What is an LLM API?

An LLM API provides access to language models through HTTP requests.

For example:

```text
Python Application
        |
        v
    LLM API
        |
        v
   AI Provider
        |
        v
   Language Model
        |
        v
 Generated Response
```

## 3. Popular LLM API Providers

| Provider | Description |
|---|---|
| OpenAI | Provides GPT models |
| Google Gemini | Provides Gemini models |
| Groq | Provides fast LLM inference |
| Anthropic | Provides Claude models |
| Mistral AI | Provides Mistral models |
| Hugging Face | Provides access to open-source models |

## 4. Get an API Key

For this project, we will use Groq.

Steps:

1. Visit https://console.groq.com/
2. Create an account.
3. Navigate to the API Keys section.
4. Generate a new API key.
5. Copy and securely store the key.

Note: Never share your API key publicly.

## 5. Install Required Packages

Install the following packages:

```bash
pip install langchain langchain-groq python-dotenv
```

## 6. Configure Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_actual_api_key
```

Never upload this file to GitHub.

## 7. Load Environment Variables

Use the `python-dotenv` package to load environment variables.

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

print("API Key Loaded:", bool(api_key))
```

Do not print the actual API key.

## 8. Initialize an LLM Using LangChain

LangChain provides a common interface to interact with different LLM providers.

Example using Groq:

```python
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

model = init_chat_model(
    "openai/gpt-oss-120b",
    model_provider="groq",
    temperature=0.7
)

response = model.invoke(
    "Explain Generative AI in simple words."
)

print(response.content)
```

Note: Model availability depends on the provider's current supported models and your account access.

## 9. Understanding Important Parameters

### model

Specifies which language model we want to use.

```python
"openai/gpt-oss-120b"
```

### model_provider

Specifies the provider hosting the model.

```python
model_provider="groq"
```

### temperature

Controls the randomness of generated responses.

```python
temperature=0.7
```

General understanding:

| Temperature | Behavior |
|---|---|
| 0.0 | More deterministic |
| 0.3 | More focused |
| 0.7 | Balanced creativity |
| 1.0 | More creative |
| Higher values | More randomness |

Actual behavior depends on the model and provider.

## 10. Understanding invoke()

`invoke()` sends input to the model and returns its response.

```python
response = model.invoke("Hello!")

print(response.content)
```

Here:

- `model.invoke()` sends the request.
- The model processes the input.
- The response is returned.
- `response.content` contains the generated text.

## 11. API Error Handling

Always handle API-related errors.

```python
try:
    response = model.invoke(
        "Explain Machine Learning."
    )

    print(response.content)

except Exception as e:
    print("API Error:", e)
```

Common API errors:

| Error | Possible Reason |
|---|---|
| 401 Unauthorized | Invalid API key |
| 403 Forbidden | Insufficient permissions |
| 404 Not Found | Invalid model or endpoint |
| 429 Too Many Requests | Rate limit exceeded |
| 500 Server Error | Provider-side issue |
| Connection Error | Network problem |

## 12. Security Best Practices

- Store API keys in environment variables.
- Never commit `.env` to GitHub.
- Never expose API keys in frontend code.
- Use API key rotation when required.
- Handle rate limits and API failures.
- Monitor API usage and costs.
- Avoid logging sensitive information.

## Summary

We have configured an LLM API and connected our Python application to a language model using LangChain.

This setup will be useful for building:

- AI Chatbots
- Text Summarizers
- Question Answering Systems
- AI Agents
- Document Processing Applications
- RAG Applications
