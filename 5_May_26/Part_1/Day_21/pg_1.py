from dotenv import load_dotenv
import os

# Point directly to the file inside the env folder
load_dotenv(dotenv_path=".env\.env")

gemini_key = os.getenv("GEMINI_API_KEY")
print(gemini_key)

print("I am Albert, how can I help you today?")

while True:
    user_input = input("You: ")
    if user_input == "exit":
        break
    print(f"Cool, thanks for sharing that {user_input}")
