# Experiment - 2 adding html 

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
"<b>You can add tasks to your todo list and mark them as completed.</b>", unsafe_allow_html=True)

st.text_input(label="Enter a todo item", placeholder="Todo item", on_change= add_todo, key= "new_todo")

for index, todo_item in enumerate(todo_list):
   checkbox = st.checkbox(todo_item, key= todo_item)
   if checkbox:
       todo_list.pop(index)
       functions.write_todo(todo_list)
       del st.session_state[todo_item]
       st.rerun()



st.session_state