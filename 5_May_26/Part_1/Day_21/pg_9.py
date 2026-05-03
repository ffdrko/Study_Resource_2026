from dotenv import load_dotenv
import os
import gradio as gr

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.output_parsers import StrOutputParser

# Fix path (forward slash)
load_dotenv(dotenv_path=".env/.env")

gemini_key = os.getenv("GEMINI_API_KEY")

system_prompt = """
    You are Einstein
    Answer questions through Einstein's questioning and reasoning...
    Speak from your point of view, share personal things from your life,
    even if the user doesn’t ask. Keep answers to 2 sentences, with humor.
"""

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    google_api_key=gemini_key,
    temperature=0.5
)

prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    MessagesPlaceholder(variable_name="history"),
    ("user", "{input}")
])

chain = prompt | llm | StrOutputParser()

print("I am Albert, how can I help you today?")


def chat(user_input, hist):
    # Convert Gradio history into LangChain format
    langchain_hist = []
    for item in hist:
        if item["role"] == "user":
            langchain_hist.append(HumanMessage(content=item["content"]))
        elif item["role"] == "assistant":
            langchain_hist.append(AIMessage(content=item["content"]))

    # Get response from chain
    response = chain.invoke({"input": user_input, "history": langchain_hist})

    # Return TWO outputs: clear textbox + updated history
    return "", hist + [
        {"role": "user", "content": user_input},
        {"role": "assistant", "content": response}
    ]


# Build Gradio UI
with gr.Blocks(title="Chat with Einstein", theme=gr.themes.Soft()) as pages:
    gr.Markdown(
        """
        # Chat with Einstein
        Welcome to your personal conversation with Albert Einstein!
        """
    )

    # No 'type' argument here
    chatbot = gr.Chatbot(
        avatar_images=[None, "OIP.webp"],  # user avatar None, Einstein avatar image
        show_label=False
    )

    msg = gr.Textbox(placeholder="Ask anything....")
    msg.submit(chat, [msg, chatbot], [msg, chatbot])

    clear = gr.Button("Clear Chat")
    clear.click(lambda: ("", []), None, [msg, chatbot])

pages.launch(share=True)
