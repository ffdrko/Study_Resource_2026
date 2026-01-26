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

window.close()