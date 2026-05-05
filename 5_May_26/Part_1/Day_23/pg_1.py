import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepath = glob.glob("invoice/*.xlsx")

for file_ded in filepath:
    df = pd.read_excel(file_ded, sheet_name= "Sheet 1")
    pdf = FPDF(orientation="P", unit= "mm", format= "A4")
    pdf.add_page()
    filename = Path(file_ded).stem
    pdf.set_font(family="Times", size= 16, style= "B")
    pdf.cell(w=50, h=8, txt= f"Invoice name:{filename}")
    pdf.output(f"pdfs/{filename}.pdf")