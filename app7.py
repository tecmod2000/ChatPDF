import os
import google.generativeai as genai
#from langchain_google_genai import GoogleGenerativeAIEmbeddings #to embed the text
from dotenv import load_dotenv
import PIL.Image
import requests
import io

load_dotenv()
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')

chat_model = genai.GenerativeModel('gemini-pro')
chat = chat_model.start_chat(history=[])

response = chat.send_message("Which is one of the best place to visit in India during summer?")
print(response.text)
response = chat.send_message("continue extending the detail about this site, on 50 words")
print(response.text)
print(chat.history)
