import d16s_0 as func
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do item: ")
input_box = sg.InputText(tooltip= "Enter todo")

window = sg.Window("My To-Do App", layout=[[label, input_box]])
window.read()
window.close()