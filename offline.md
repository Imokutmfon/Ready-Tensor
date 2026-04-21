# How to Set Up and Use Ollama

## Step 1: Install Ollama

Go to [https://ollama.com](https://ollama.com) and download the installer for your system (macOS, Windows, or Linux).

Follow the instructions to complete installation.

## Step 2: Download a Model

Once installed, open your terminal and run:

```bash
# Recommended starting point
ollama pull llama3-8b-8192
```

Other available models include:

```bash
ollama pull mistral
ollama pull codellama
```

These will download and prepare the models for local use.

## Step 3: Install the LangChain Integration

Install the Ollama LangChain wrapper:

```bash
pip install langchain-ollama
```

## Step 4: Run a Local LLM Test

Here's a minimal example:

```python
from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3-8b-8192")
response = llm.invoke("Summarize how local models work.")
print(response)
```

This will invoke the LLM running on your machine and return a response — no cloud involved.

> 🧪 Try a fun test prompt like: *"Explain agentic AI like you're a movie trailer narrator."*
