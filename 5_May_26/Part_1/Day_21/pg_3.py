from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Point directly to the file inside the env folder
load_dotenv(dotenv_path=".env\.env")

gemini_key = os.getenv("GEMINI_API_KEY")

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = gemini_key,
    temperature = 0.5
)

response = llm.invoke([{"role":"user", "content":"Hi there, how are you?"}])

print(response)
print(type(response))
print(type(response.content))
# print("I am Albert, how can I help you today?")

# while True:
#     user_input = input("You: ")
#     if user_input == "exit":
#         break
#     print(f"Cool, thanks for sharing that {user_input}")
