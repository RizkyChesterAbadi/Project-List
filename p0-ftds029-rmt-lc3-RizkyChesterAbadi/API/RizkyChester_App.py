# Live Code 3
# Nama    : Rizky Chester Abadi

# Batch   : RMT-029

# Pembuatan API


# import package
from fastapi import FastAPI
import pandas as pd

# membuat object FastAPI / instance
app = FastAPI()

# Meloading file CSV dari data lokal
file = r'C:\Users\rizqc\Documents\Tugas Tugas\p0-ftds029-rmt-lc3-RizkyChesterAbadi\RizkyChester.csv'

# membuat dataframe untuk data CSV yang diambil
df_sale = pd.read_csv(file)

# mengconvert dataframe df_sale ke bentuk dict
@app.get('/show-data')
def getShowData():
    return df_sale.to_dict(orient='records')