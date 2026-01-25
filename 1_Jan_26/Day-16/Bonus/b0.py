import FreeSimpleGUI as sg

# First row: file selection
label = sg.Text("Select file to compress:")
input_box = sg.InputText()
select_button = sg.FileBrowse('Choose')

# Second row: destination folder
label_1 = sg.Text("Select destination folder:")
input_box_1 = sg.InputText()
select_button_1 = sg.FolderBrowse('Choose')

# Window layout
layout = [
    [label, input_box, select_button],
    [label_1, input_box_1, select_button_1]
]

window = sg.Window("File Compressor", layout)

window.read()
window.close()
