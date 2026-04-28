import FreeSimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
and_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=
[
    [label], 
    [input_box, and_button]
], font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)

window.close()