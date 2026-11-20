# 00 - Environment Setup

## Introduction

Before starting Generative AI development, we need to configure our development environment.

This section covers the basic tools, libraries, and configurations required to work with Generative AI and Large Language Models (LLMs).

## 1. Prerequisites

The following technologies are required:

- Python
- pip (Python Package Manager)
- Virtual Environment
- VS Code
- Git and GitHub
- API Keys
- Basic Python Programming

## 2. Required Tools

| Tool | Purpose |
|---|---|
| Python | Main programming language |
| VS Code | Code editor |
| pip | Install Python packages |
| venv | Manage virtual environments |
| Git | Version control |
| GitHub | Store and manage projects |
| dotenv | Manage environment variables |
| LangChain | Build LLM applications |

## 3. Important Python Libraries

Some commonly used libraries in Generative AI development:

| Library | Purpose |
|---|---|
| langchain | Framework for building LLM applications |
| langchain-core | Core LangChain abstractions |
| langchain-groq | Groq model integration |
| python-dotenv | Load environment variables |
| streamlit | Build interactive web applications |
| pydantic | Data validation and structured outputs |
| requests | Make HTTP requests |

## 4. Environment Setup Workflow

Follow these steps:

1. Install Python.
2. Install VS Code.
3. Create a project directory.
4. Create a virtual environment.
5. Activate the virtual environment.
6. Install required dependencies.
7. Configure API keys.
8. Test your environment.

## 5. Why Use a Virtual Environment?

A virtual environment is an isolated Python environment that allows us to install project-specific dependencies.

### Advantages

- Avoids dependency conflicts.
- Keeps projects independent.
- Makes dependency management easier.
- Helps maintain reproducible development environments.

## 6. Environment Variables

Environment variables store configuration values separately from application code.

For example:

- API keys
- Database URLs
- Secret tokens
- Application configurations

Never hardcode API keys directly into your Python source code.

## 7. Important Security Practices

- Never upload API keys to GitHub.
- Keep `.env` inside `.gitignore`.
- Use `.env.example` to document required variables.
- Never share private credentials.
- Use separate API keys for different projects.

## 8. Expected Folder Structure


## Summary

Environment setup is the foundation of Generative AI development.

A properly configured environment makes development, debugging, dependency management, and deployment easier.
