from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-pro-vision")

message = HumanMessage(
    content=[
        {
            "type": "text",
            "text": "Find the differences between the given images",
        },
        {
            "type": "image_url",
            "image_url": "https://picsum.photos/id/237/200/300"
        },
        {
            "type": "image_url",
            "image_url": "https://picsum.photos/id/219/5000/3333"
        }
    ]
)

response = llm.invoke([message])
print(response.content)