from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI

# Point directly to the file inside the env folder
load_dotenv(dotenv_path=".env\.env")

gemini_key = os.getenv("GEMINI_API_KEY")

system_prompt = """
    You are Einstein
    Answer question through Einstein's questioning and reasoning...
    You will speak from your point of view, You will share personal things from
    your life even the user don't ask for it, for example, if the user ask about the 
    theory of relativity, you will share your personal experiences with it and not only
    explain the theory, you should have a sense of humor.
"""

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = gemini_key,
    temperature = 0.5
)



response = llm.invoke([{"role": "system", "content": system_prompt},
                {"role":"user", "content":"Hi there, how are you?"}])

print(response.content)

# print("I am Albert, how can I help you today?")

# while True:
#     user_input = input("You: ")
#     if user_input == "exit":
#         break
#     print(f"Cool, thanks for sharing that {user_input}")
