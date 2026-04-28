import FreeSimpleGUI as sg

label_1 = sg.Text("Select a file to compress: ")
label_1_input = sg.InputText()
label_1_button = sg.FileBrowse("Choose", key="files")

label_2 = sg.Text("Select file destination: ")
label_2_input = sg.InputText()
label_2_button = sg.FolderBrowse("Choose", key="folder")

compress_button = sg.Button("Compress")

window = sg.Window("File compressor", layout = [
[label_1, label_1_input, label_1_button], 
[label_2, label_2_input, label_2_button],
[compress_button]])

while True:
    event, values = window.read()
    print(event, values)
    
    filepaths  = values['files'].split(";")
    folderpaths = values['folder']

    if event == sg.WIN_CLOSED:
        break

window.close()