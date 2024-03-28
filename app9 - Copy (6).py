from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")

message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "describe all elements on the picture one by one.",
        },        
        {
            "type": "image_url",
            "image_url": "https://picsum.photos/id/237/200/300"
        },
    ]
)

response = llm.invoke([message])
print(response.content)