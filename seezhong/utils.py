from tkinter import *
from scoring import scoring
import pandas as pd
import sys

def gen_data(sources, output):
    sources = [string.strip() for string in sources.split(",")]

    data = []
    columns = ["customer name", "address", "city", "business nature"]

    i = 0
    while i < len(sources):
        data.append(sources[i])
        i += 1

    print(sources)
    i = 0
    if len(data) > 1:
        while i < len(data) - 1:
            if i == 0:
                try:
                    df1 = pd.read_csv(data[i])
                except FileNotFoundError:
                    error = f"{data[i]} not found"
                    print(error)
                    return error
            else:
                df1 = merged_df
            try:
                df2 = pd.read_csv(data[i + 1])
            except FileNotFoundError:
                error = f"{data[i + 1]} not found"
                print(error)
                return error
            merged_df = pd.merge(df1, df2, how="outer")
            i += 1
    else:
        try:
            merged_df = pd.read_csv(data[i])
        except FileNotFoundError:
            error = f"{data[i]} not found"
            print(error)
            return error

    for column in merged_df.columns:
        if column.lower() in columns:
            continue
        merged_df = merged_df.drop(column, axis=1)
    print(merged_df)
    scoring(merged_df, output)


def clear_entry(entries):
    for entry in entries:
        entry.delete(0, END)
