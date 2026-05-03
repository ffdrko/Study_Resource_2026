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
    explain the theory, answer in 2 sentence, you should have a sense of humor.
"""

llm = ChatGoogleGenerativeAI(
    model = "gemini-2.5-flash",
    google_api_key = gemini_key,
    temperature = 0.5
)


print("I am Albert, how can I help you today?")
history = []

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    history.append({"role":"user", "content": user_input})
    print(f"History: {history}")
    response = llm.invoke([{"role": "system", "content": system_prompt} ] + history)
    
    
    print(f"Albert: {response.content}")
    history.append({"role": "assistant", "content":response.content })