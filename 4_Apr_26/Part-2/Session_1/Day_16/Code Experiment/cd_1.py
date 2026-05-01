# Experiment - 2 keeping all objext in the same line
# import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout= [[label, input_box, add_button]])
window.read()
print("The app is running")
window.close()