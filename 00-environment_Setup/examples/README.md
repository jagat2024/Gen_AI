# Environment Setup - Examples

This directory contains practical Python examples demonstrating environment configuration and API integration.

## Available Examples

| File | Description |
|---|---|
| `hello.py` | Basic Python environment test |
| `env_example.py` | Loading environment variables |
| `api_test.py` | Testing an LLM API connection |

## 1. hello.py

Checks whether Python is working correctly.

```python
print("Welcome to Generative AI!")
print("Python Environment Setup Successful!")
```

Run:

```bash
python hello.py
```

## 2. env_example.py

Demonstrates how to load environment variables.

```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if api_key:
    print("API Key Loaded Successfully!")
else:
    print("API Key Not Found!")
```

Run:

```bash
python env_example.py
```

## 3. api_test.py

Tests the connection with a Groq-hosted language model.

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
    "Say Hello and introduce yourself."
)

print(response.content)
```

Run:

```bash
python api_test.py
```

## Learning Outcomes

After completing these examples, you should understand:

- How to configure a Python environment.
- How to create and activate virtual environments.
- How to install Python dependencies.
- How to manage environment variables.
- How to configure API keys.
- How to connect Python applications with LLM APIs.
- How to generate responses using LangChain.
