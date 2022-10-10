import pandas as pd
import numpy as np
from datetime import date
from decimal import Decimal
from re import sub

def cleaning(df):
    df.reset_index(inplace=True)
    if 'Unnamed: 0' in df.columns:
        df = df.drop('Unnamed: 0', axis = 1)
    if 'index' in df.columns:
        df = df.drop('index', axis = 1)
    return (df)

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

def put_last(df, col):
    cols_at_end = [col["source_type"], col["score"]]
    df = df[[c for c in df if c not in cols_at_end]
            + [c for c in cols_at_end if c in df]]
    return (df)
