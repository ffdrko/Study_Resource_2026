from dotenv import load_dotenv
import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

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
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    (MessagesPlaceholder(variable_name="history")),
    ("user", "{input}")]
)

chain = prompt | llm | StrOutputParser()#  here | means output of the prompt will go as input into llm

print("I am Albert, how can I help you today?")
history = []

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    
    response = chain.invoke({"input": user_input, "history": history})
    
    
    print(f"Albert: {response}")
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=response))