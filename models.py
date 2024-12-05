import langchain
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

groq_key = os.getenv("LANGCHAIN_TOKEN")

model_llama = ChatGroq(
    groq_api_key = groq_key,
    model_name = "llama-3.1-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)

response = model_llama.invoke("Hello")
print(response.content)