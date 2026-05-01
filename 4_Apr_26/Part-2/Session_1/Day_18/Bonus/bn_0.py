import FreeSimpleGUI as sg
import zipfile
import os

sg.theme("Black")

label1 = sg.Text("Select archive: ")
input_1 = sg.Input(key="archive_path")
choose_button = sg.FileBrowse("Choose", key="archive", target="archive_path")

label2 = sg.Text("Select destination direction: ")
input_2 = sg.Input(key="folder_path")
choose_button_2 = sg.FolderBrowse("Choose", key="folder", target="folder_path")

extract_button = sg.Button("Extract")
output_label = sg.Text(key="output", text_color="green")

layout = [
    [label1, input_1, choose_button],
    [label2, input_2, choose_button_2],
    [extract_button],
    [output_label]
]

window = sg.Window("Archive Extractor", layout, font=('Helvetica', 16))

while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == "Extract":
        archive_path = values['archive_path']
        destination_path = values['folder_path']
        
        if not archive_path or not destination_path:
            sg.popup("Please select both archive and destination folder.", title="Error", font=('Helvetica', 14))
        elif not os.path.exists(archive_path):
            sg.popup("Archive file does not exist.", title="Error", font=('Helvetica', 14))
        elif not os.path.exists(destination_path):
            sg.popup("Destination folder does not exist.", title="Error", font=('Helvetica', 14))
        else:
            try:
                with zipfile.ZipFile(archive_path, 'r') as zip_ref:
                    zip_ref.extractall(destination_path)
                window['output'].update(f"✓ Successfully extracted to {destination_path}", text_color="green")
            except Exception as e:
                window['output'].update(f"✗ Error: {str(e)}", text_color="red")

window.close()