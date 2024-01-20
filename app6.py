import os
import google.generativeai as genai
from langchain_google_genai import GoogleGenerativeAIEmbeddings #to embed the text
from dotenv import load_dotenv
import PIL.Image
import requests
import io

load_dotenv()
genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))
model = genai.GenerativeModel('gemini-pro')
vision_model = genai.GenerativeModel('gemini-pro-vision')

"""
image = PIL.Image.open('./cubo.webp')
response = vision_model.generate_content(["write a story from the picture",image])
print(response.text)
"""

url = "https://res.cloudinary.com/practicaldev/image/fetch/s--Aplmm5Kg--/c_limit%2Cf_auto%2Cfl_progressive%2Cq_auto%2Cw_800/https://dev-to-uploads.s3.amazonaws.com/uploads/articles/18tk5unfi1ii679m7v3h.png" 
response = requests.get(url)

image = PIL.Image.open(io.BytesIO(response.content))
response = vision_model.generate_content(["Explain the picture?", image])
print(response.text)
"""
image = PIL.Image.open('./objetos.jfif')
vision_model = genai.GenerativeModel('gemini-pro-vision')
response = vision_model.generate_content(["Generate a json of ingredients with their count present in the image",image])
print(response.text)"""