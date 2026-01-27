import functions
import FreeSimpleGUI as Sg



label = Sg.Text("Type in todo: ")
input_box = Sg.InputText(tooltip="Enter todo", key="Todo")
add_button = Sg.Button("Add", tooltip="Add task")
list_box = Sg.Listbox(values=functions.read_todo(), key="Todo_list",
                      size=(45,10))
edit_button = Sg.Button("Edit", tooltip="Edit task")

window = Sg.Window("My todo App",
                   layout=[[label], [input_box], [add_button], [list_box,edit_button]],
                   font= ('Helvetica', 20))

while True:
    event, value = window.read()
    # print(event)
    # print(value)
    # print(value['Todo_list'][0])
    match event:
        case "Add":
            todo_list = functions.read_todo()
            todo_item = value['Todo']
            todo_list.append(todo_item + '\n')
            functions.write_todo(todo_list)
            window["Todo_list"].update(values=todo_list)
        case "Edit":
            todo_item = value['Todo_list'][0]
            new_todo_item = value['Todo']
            todo_list = functions.read_todo()
            index = todo_list.index(todo_item)
            todo_list[index] = new_todo_item + '\n'
            functions.write_todo(todo_list)
            window["Todo_list"].update(values = todo_list)
        case 'Todo_list':
            window["Todo_list"].update(value = value['todo_list'][0])
        case Sg.WIN_CLOSED:
            break

print("Bye")
window.close()