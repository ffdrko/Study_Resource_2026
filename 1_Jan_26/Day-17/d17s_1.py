import functions
import FreeSimpleGUI as Sg

label = Sg.Text("Type in todo: ")
input_box = Sg.InputText(tooltip="Enter todo", key="Todo")
add_button = Sg.Button("Add", tooltip="Add task")

window = Sg.Window("My todo App",
                   layout=[[label], [input_box], [add_button]],
                   font= ('Helvetica', 20))

while True:
    event, value = window.read()
    print(event)
    print(value)
    match event:
        case "Add":
            todo_list = functions.read_todo()
            todo_item = value['Todo']
            todo_list.append(todo_item + '\n')
            functions.write_todo(todo_list)
        case Sg.WIN_CLOSED:
            break

window.close()