import FreeSimpleGUI as Sg
from b1 import make_archive

label_1 = Sg.Text("Select files to compress: ")
input_1 = Sg.Input()
choose_btn_1 = Sg.FileBrowse("Choose", key= "file")

label_2 = Sg.Text("Select files to compress: ")
input_2 = Sg.Input()
choose_btn_2 = Sg.FolderBrowse("Choose", key= "folder")

compress_btn = Sg.Button("Compress")
window = Sg.Window("File compressor", layout=[[label_1,input_1,
                                               choose_btn_1],
                                              [label_2,input_2,choose_btn_2]
                                              ,[compress_btn]])
while True:
    event, value = window.read()
    print(event, value)
    filepaths = value['file'].split(';')
    folder = value['folder']
    make_archive(filepaths, folder)


window.close()