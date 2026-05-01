# Experiment - 1 removing all bracket inside the layout 
# and see what happens

import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

# if we remove the brackets inside the layout,
#  it will throw an error because the layout expects a list of lists (rows of elements)
window = sg.Window("My To-Do App", layout= [[label], [input_box, add_button]])
window.read()
print("The app is running")
window.close()