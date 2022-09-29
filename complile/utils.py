from tkinter import *
import pandas as pd

test_df = None

def collect_data(sources):
    sources = [string.strip() for string in sources.split(",")]
    data = []
    i = 0
    while i < len(sources):
        data.append(sources[i])
        i += 1
    return data

def find_and_merge(data):
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
            #merged_df = pd.merge(df1, df2, how="outer")
            frames = [df1, df2]
            merged_df = pd.concat(frames, join="outer")
            i += 1
    else:
        try:
            merged_df = pd.read_csv(data[i])
        except FileNotFoundError:
            error = f"{data[i]} not found"
            print(error)
    return merged_df

def drop_column(merged_df):
    #get columns input
    columns = []
    cf = pd.read_csv("data/columns.csv")
    for index, row in cf.iterrows():
        columns.append(row.item().lower().strip())

    for column in merged_df.columns:
        if column.lower().strip() in columns:
            continue
        merged_df = merged_df.drop(column, axis=1)
        print(f"merged_df = {merged_df}")
    return merged_df
    
def merge_data(sources, output):
    data = collect_data(sources)
    try:
        merged_df = find_and_merge(data)
    except:
        return
    merged_df = drop_column(merged_df) 
    #merged_df.to_csv(output + ".csv")
    return merged_df

def clear_entry(entries):
    for entry in entries:
        entry.delete(0, END)
