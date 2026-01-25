import FreeSimpleGUI as sg

label = sg.Text("Enter Feet: ")
input_box = sg.InputText()

label_1 = sg.Text("Enter Inches: ")
input_box_1 = sg.InputText()
add_button = sg.Button("Convert")

window = sg.Window("convertor", layout=[[label, input_box], [label_1, input_box_1],[add_button]])
window.read()
window.close()