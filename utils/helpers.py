import pandas as pd

def convert_decimal_separator(df):
    return df.apply(lambda x: float(x.replace('.', '').replace(',','.')))