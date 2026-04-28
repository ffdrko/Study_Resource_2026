import functions_0
import FreeSimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
and_button = sg.Button("Add")
list_box = sg.Listbox(values=functions_0.get_todo(), key="todo_list", 
                      enable_events=True, 
                      size=[45, 10])
edit_button = sg.Button("Edit")
window = sg.Window("My To-Do App", layout=
[
    [label], 
    [input_box, and_button],
    [list_box, edit_button]
], font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todo_list'])

    match event:
        case "Add":
            todo_list = functions_0.get_todo()
            new_todo = values['todo'] + "\n"
            todo_list.append(new_todo)
            functions_0.write_todo(todo_list)
            window['todo_list'].update(todo_list)
        case "Edit":
            todo_item = values['todo_list'][0]
            new_todo = values['todo'] + "\n"

            todo_list = functions_0.get_todo()
            index = todo_list.index(todo_item)  # Find the index of the selected todo item
            todo_list[index] = new_todo  # Replace the selected todo item with the updated version
            functions_0.write_todo(todo_list)
            window['todo_list'].update(todo_list)
        case sg.WIN_CLOSED:
            break

window.close()