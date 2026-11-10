
import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

GROQ_API_KEY = (
    os.getenv("GROQ_API_KEY")
    or st.secrets.get("GROQ_API_KEY")
)

if not GROQ_API_KEY:
    raise ValueError(
        "GROQ_API_KEY not found. Please configure your .env file."
    )

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=GROQ_API_KEY,
    temperature=0.85,
    max_tokens=2048
)
