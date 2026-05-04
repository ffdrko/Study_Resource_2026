from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="p", unit="mm", format="A4")

df = pd.read_csv("topic.csv")

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family="Times", size=10)
    pdf.cell(w=0, h=10, txt = "Hello there!", align="L")


pdf.output("demo_3.pdf")