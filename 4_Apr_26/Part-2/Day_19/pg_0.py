import streamlit as st
import functions

todo_list = functions.get_todo()

st.title("My Todo App")
st.subheader("A simple todo app built with Streamlit")
st.write("This is a simple todo app built with Streamlit. " \
"You can add tasks to your todo list and mark them as completed.")


for todo_item in todo_list:
    st.checkbox(todo_item)

st.text_input(label="Enter a todo item", key="new_todo")