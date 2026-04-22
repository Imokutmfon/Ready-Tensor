import os
from dotenv import load_dotenv

# This searches for a .env file and loads it into os.environ
load_dotenv()

# Now you can access them like normal environment variables
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)
response = llm.invoke("Explain prompt engineering in simple terms.")
print(response)