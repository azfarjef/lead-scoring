import pandas as pd
import numpy as np
from datetime import date
from decimal import Decimal
from re import sub

def str_to_dec(df, col):
    curr = [] * len(df.index)
    for index, row in df.iterrows():
        if isinstance(row[col], str) and not pd.isna(row[col]):
            if row[col].isalpha():
                df.at[index, col] = np.nan
                continue            
            curr = df.at[index, col]
            value = Decimal(sub(r'[^\d.]', '', curr))
            df.at[index, col] = value
    return (df)

def diff_date(df, col):
    today_date = date.today()
    df.insert(3, 'Today Date', today_date)
    diff = (pd.to_datetime(df["Today Date"]) - pd.to_datetime(df[col["created_date"]])).dt.days
    df.insert(5, "Last Created", diff)
