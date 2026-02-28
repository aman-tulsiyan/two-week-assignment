import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Read API key securely from environment
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY not found in environment variables.")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

# Guardrail: Maximum reasoning steps
MAX_STEPS = 5

# Model selection
MODEL_NAME = "llama-3.3-70b-versatile"