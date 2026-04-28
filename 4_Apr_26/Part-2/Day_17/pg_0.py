import functions_0
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

    match event:
        case "Add":
            todo_list = functions_0.get_todo()
            new_todo = values['todo'] + "\n"
            todo_list.append(new_todo)
            functions_0.write_todo(todo_list)
        case sg.WIN_CLOSED:
            break

window.close()