from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="p", unit="mm", format="A4")

df = pd.read_csv("topic.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times",style="B",size=24)
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=10, txt = row['Topic'], align="L")
    pdf.line(10,22,200,22)

    for item in range(row['Pages'] - 1):
        pdf.add_page()
    
pdf.output("demo_6.pdf")