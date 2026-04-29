import functions as functions_0
import FreeSimpleGUI as sg
import time

sg.theme("BluePurple")
label = sg.Text("Type in a todo")
clock_display = sg.Text("", key="clock", font=('Helvetica', 16), text_color='blue')
input_box = sg.InputText(tooltip="Enter todo", key="todo")
and_button = sg.Button("Add")
list_box = sg.Listbox(values=functions_0.get_todo(), key="todo_list", 
                      enable_events=True, 
                      size=[45, 10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
window = sg.Window("My To-Do App", layout=
[
    [clock_display],
    [label], 
    [input_box, and_button],
    [list_box, edit_button, complete_button], [exit_button]
], font=('Helvetica', 20))

while True:
    event, values = window.read(timeout=1000)
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event is None:
        # Update clock every second (only if window is still open)
        try:
            current_time = time.strftime("%B %d, %H:%M:%S")
            window['clock'].update(f"Current Time: {current_time}")
        except:
            break
        continue
    
    print(event)
    print(values)
    print(values['todo_list'])

    match event:
        case "Add":
            try:
                if values['todo'].strip() == "":
                    sg.popup("Please enter a todo item.", title="Alert", font=('Helvetica', 20))
                else:
                    todo_list = functions_0.get_todo()
                    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                    new_todo = f"[{timestamp}] {values['todo']}\n"
                    todo_list.append(new_todo)
                    functions_0.write_todo(todo_list)
                    window['todo_list'].update(todo_list)
                    window['todo'].update("")
            except Exception as e:
                sg.popup(f"Error adding todo: {str(e)}", title="Error", font=('Helvetica', 20))
        case "Edit":
            try:
                if values['todo_list']:  # Check if an item is selected
                    todo_item = values['todo_list'][0]
                    new_todo = values['todo'] + "\n"

                    todo_list = functions_0.get_todo()
                    index = todo_list.index(todo_item)  # Find the index of the selected todo item
                    todo_list[index] = new_todo  # Replace the selected todo item with the updated version
                    functions_0.write_todo(todo_list)
                    window['todo_list'].update(todo_list)
            except IndexError:
                sg.popup("Please select an item to edit.",  font=('Helvetica', 20))
        case "todo_list":
            if values['todo_list']:  # Check if an item is selected
                window['todo'].update(values['todo_list'][0])
        case "Complete":
            if values['todo_list']:  # Check if an item is selected
                todo_item = values['todo_list'][0]
                todo_list = functions_0.get_todo()
                todo_list.remove(todo_item)  # Remove the selected todo item using pop method
                functions_0.write_todo(todo_list)
                window['todo_list'].update(todo_list)
            else:
                sg.popup("Please select an item to complete.", title="Alert", font=('Helvetica', 20))
        case "Exit":
             break
        case sg.WIN_CLOSED:
            break

window.close()