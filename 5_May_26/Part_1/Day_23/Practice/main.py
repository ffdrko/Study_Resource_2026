from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("Practice/*.txt")

pdf = FPDF(orientation="P", unit= "mm", format="A4")

for file_destination in filepaths:
    pdf.add_page()

    filename = Path(file_destination).stem
    name = filename.title()

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt = name, ln=1)


pdf.output("Practice/animal.pdf")