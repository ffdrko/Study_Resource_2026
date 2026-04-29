import FreeSimpleGUI as sg

sg.theme("DarkAmber")

label_1 = sg.Text("Enter Feet: ")
input_1 = sg.Input(key="feet")

label_2 = sg.Text("Enter Inches: ")
input_2 = sg.Input(key="inches")
convert_button = sg.Button("Convert")
output_label = sg.Text(key="output", text_color="green")

layout = [
    [label_1, input_1],
    [label_2, input_2],
    [convert_button],
    [output_label]
]

window = sg.Window("Feet and Inches to Centimeters Converter", layout=layout, font=('Helvetica', 16))
while True:
    event, values = window.read()
    
    if event == sg.WINDOW_CLOSED:
        break
    
    if event == "Convert":
        try:
            feet = float(values['feet'])
            inches = float(values['inches'])
            total_inches = feet * 12 + inches
            centimeters = total_inches * 2.54
            window['output'].update(f"{feet} feet and {inches} inches is equal to {centimeters:.2f} cm", text_color="green")
        except ValueError:
            window['output'].update("Please enter valid numbers for feet and inches.", text_color="red")

window.close()