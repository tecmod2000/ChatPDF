from dotenv import load_dotenv
import google.generativeai as genai
import os
from langchain_google_genai import ChatGoogleGenerativeAI


#load_dotenv()
#genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
"""
llm = ChatGoogleGenerativeAI(model="gemini-pro")
response = llm.invoke("Explain Quantum Computing in 50 words?")
print(response.content)
"""
llm = ChatGoogleGenerativeAI(model="gemini-pro")
batch_responses = llm.batch(
    [
        "Who is the Prime Minister of India?",
        "What is the capital of India?",
    ]
)
for response in batch_responses:
    print(response.content)