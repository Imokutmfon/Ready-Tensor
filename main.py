import os
from dotenv import load_dotenv

# This searches for a .env file and loads it into os.environ
load_dotenv()

# Now you can access them like normal environment variables
api_key = os.getenv("API_KEY")
print(f"My API Key is: {api_key}")