import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("Invoice/*.xlsx")

print(filepaths)