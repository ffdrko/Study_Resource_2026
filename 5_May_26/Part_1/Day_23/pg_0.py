import pandas as pd
import glob

filepath = glob.glob("invoice/*.xlsx")

for file_ded in filepath:
    df = pd.read_excel(file_ded, sheet_name= "Sheet 1")
    print(df)