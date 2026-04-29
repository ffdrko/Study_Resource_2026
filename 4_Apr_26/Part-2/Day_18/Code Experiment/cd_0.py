# Experiment 1 add button icon
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import functions as functions_0
import FreeSimpleGUI as sg
import time

sg.theme("BluePurple")
label = sg.Text("Type in a todo")
clock_display = sg.Text("", key="clock", font=('Helvetica', 16), text_color='blue')
input_box = sg.InputText(tooltip="Enter todo", key="todo")
and_button = sg.Button("➕", key="Add", size=(2, 1), font=('Helvetica', 18), tooltip="Add new todo")
list_box = sg.Listbox(values=functions_0.get_todo(), key="todo_list", 
                      enable_events=True, 
                      size=[45, 10])
edit_button = sg.Button("✏️", key="Edit", size=(2, 1), font=('Helvetica', 18), tooltip="Edit selected todo")
complete_button = sg.Button("✓", key="Complete", size=(2, 1), font=('Helvetica', 18), tooltip="Mark as complete")
exit_button = sg.Button("❌", key="Exit", size=(2, 1), font=('Helvetica', 18), tooltip="Exit application")
window = sg.Window("My To-Do App", layout=
[
    [clock_display],
    [label], 
    [input_box, and_button],
    [list_box, edit_button, complete_button], [exit_button]
], font=('Helvetica', 20), finalize=True)

# Update clock initially
current_time = time.strftime("%B %d, %H:%M:%S")
window['clock'].update(f"Current Time: {current_time}")

while True:
    event, values = window.read(timeout=1000)
    
    if event == sg.WINDOW_CLOSED:
        break
    
    # Update clock every second (only if window is open)
    if event is None or isinstance(event, str):
        try:
            current_time = time.strftime("%B %d, %H:%M:%S")
            window['clock'].update(f"Current Time: {current_time}")
        except:
            break
    
    if event is None:
        continue

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
                    if values['todo'].strip() == "":
                        sg.popup("Please enter a new todo item.", title="Alert", font=('Helvetica', 20))
                    else:
                        todo_list = functions_0.get_todo()
                        # Strip to compare items properly
                        index = None
                        for i, item in enumerate(todo_list):
                            if item.strip() == todo_item.strip():
                                index = i
                                break
                        
                        if index is not None:
                            timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
                            new_todo = f"[{timestamp}] {values['todo']}\n"
                            todo_list[index] = new_todo
                            functions_0.write_todo(todo_list)
                            window['todo_list'].update(todo_list)
                            window['todo'].update("")
                        else:
                            sg.popup("Item not found. Please refresh and try again.", title="Alert", font=('Helvetica', 20))
            except (IndexError, ValueError) as e:
                sg.popup(f"Error editing todo: {str(e)}", title="Error", font=('Helvetica', 20))
        case "todo_list":
            if values['todo_list']:  # Check if an item is selected
                window['todo'].update(values['todo_list'][0])
        case "Complete":
            try:
                if values['todo_list']:  # Check if an item is selected
                    todo_item = values['todo_list'][0]
                    todo_list = functions_0.get_todo()
                    if todo_item in todo_list:
                        todo_list.remove(todo_item)
                        functions_0.write_todo(todo_list)
                        window['todo_list'].update(todo_list)
                    else:
                        sg.popup("Item not found. Please refresh and try again.", title="Alert", font=('Helvetica', 20))
                else:
                    sg.popup("Please select an item to complete.", title="Alert", font=('Helvetica', 20))
            except Exception as e:
                sg.popup(f"Error completing todo: {str(e)}", title="Error", font=('Helvetica', 20))
        case "Exit":
             break
        case sg.WIN_CLOSED:
            break

window.close()