import os
from dotenv import load_dotenv

# This searches for a .env file and loads it into os.environ
load_dotenv()

# Now you can access them like normal environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

from langchain_groq import ChatGroq

llm = ChatGroq(model="llama-3.1-8b-instant")
response = llm.invoke("What is agentic AI?")
print(response)