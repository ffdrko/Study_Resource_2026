import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path
import openpyxl

filepath = glob.glob("Invoice/*.xlsx")

for file_ded in filepath:
    df = pd.read_excel(file_ded, sheet_name= "Sheet 1")
    pdf = FPDF(orientation="P", unit= "mm", format= "A4")
    pdf.add_page()
    filename = Path(file_ded).stem
    invoice_nr = filename.split("-")[0]
    pdf.set_font(family="Times", size= 16, style= "B")
    pdf.cell(w=50, h=8, txt= f"Invoice name:{invoice_nr}", ln=1)

    time_Date = filename.split("-")[1]
    pdf.set_font(family="Times", size= 16, style= "B")
    pdf.cell(w=50, h=8, txt= f"Date:{time_Date}")


    pdf.output(f"Pdf/{invoice_nr}.pdf")