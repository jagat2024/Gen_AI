# Python Environment Setup

## 1. Introduction

Python is one of the most widely used programming languages in Artificial Intelligence, Machine Learning, and Generative AI.

We use Python to interact with LLM APIs, process data, build AI applications, and develop intelligent systems.

## 2. Check Python Installation

First, check whether Python is installed.

```bash
python --version
```

Alternative:

```bash
python3 --version
```

Check pip:

```bash
pip --version
```

## 3. Create Project Directory

Create a directory for your Generative AI project.

```bash
mkdir Generative_AI
cd Generative_AI
```

## 4. Create Virtual Environment

A virtual environment provides an isolated environment for Python dependencies.

```bash
python -m venv .venv
```

Here:

- `python`: Python interpreter.
- `-m`: Execute a Python module.
- `venv`: Virtual environment module.
- `.venv`: Environment directory name.

## 5. Activate Virtual Environment

### Windows PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

### Windows CMD

```cmd
.venv\Scripts\activate.bat
```

### Linux / macOS

```bash
source .venv/bin/activate
```

After activation, you should see something similar to:

```text
(.venv) PS C:\Users\Home\Desktop\Generative_AI>
```

## 6. Upgrade pip

Upgrade pip to its latest available version.

```bash
python -m pip install --upgrade pip
```

## 7. Install Required Packages

Install the required libraries.

```bash
pip install langchain langchain-core
pip install langchain-groq
pip install python-dotenv
pip install streamlit
pip install pydantic
```

## 8. Verify Installed Packages

```bash
pip list
```

Check an individual package:

```bash
pip show langchain
```

## 9. Save Dependencies

Save all installed dependencies into a requirements file.

```bash
pip freeze > requirements.txt
```

Install dependencies from an existing requirements file:

```bash
pip install -r requirements.txt
```

## 10. Deactivate Virtual Environment

When you finish working:

```bash
deactivate
```

## 11. Recommended .gitignore

Create a `.gitignore` file in your project root.

```gitignore
# Virtual Environment
.venv/
venv/
env/

# Environment Variables
.env

# Python Cache
__pycache__/
*.pyc

# Jupyter Notebook
.ipynb_checkpoints/

# IDE
.vscode/

# Operating System
.DS_Store
Thumbs.db
```

## 12. Best Practices

- Always use a virtual environment.
- Keep dependencies inside `requirements.txt`.
- Avoid installing unnecessary packages.
- Never upload `.env` files.
- Use meaningful package and folder names.
- Keep your Python environment organized.

## Summary

We have successfully configured our Python development environment.

We are now ready to start building Generative AI applications using Python and LLM frameworks.
