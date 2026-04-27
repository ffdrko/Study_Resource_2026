# Experiment - 3 adding a string in the layout to see what happens
# import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout= [[label],"hi" , [input_box, add_button]])
window.read()
print("The app is running")
window.close()