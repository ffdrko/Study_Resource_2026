import streamlit as st
import functions

todo_list = functions.get_todo()

def add_todo():
    todo_item = st.session_state["new_todo"]
    todo_list.append(todo_item + '\n')
    functions.write_todo(todo_list)


st.title("My Todo App")
st.subheader("A simple todo app built with Streamlit")
st.write("This is a simple todo app built with Streamlit. " \
"You can add tasks to your todo list and mark them as completed.")

for todo_item in todo_list:
    st.checkbox(todo_item)

st.text_input(label="Enter a todo item", placeholder="Todo item", on_change= add_todo, key= "new_todo")

st.session_state