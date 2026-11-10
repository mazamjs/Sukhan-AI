from backend.prompts import prompt
from backend.llm import llm

# Connect Prompt Template with Groq LLM

chain = prompt | llm
