from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
import pandas as pd
import sys

def collect_data(sources):
    sources = [string.strip() for string in sources.split(" ")]
    return sources
    """
    data = []
    i = 0
    while i < len(sources):
        data.append(sources[i])
        i += 1
    return data
    """

def find_and_merge(data, col):
    i = 0
    if len(data) > 1:
        while i < len(data):
            print(f"len = {len(data)}")
            print(f"PRINT =  {data[i]}")
            if i == 0:
                try:
                    if data[i].endswith(".csv"):
                        df1 = pd.read_csv(data[i])
                        # df1 = pd.read_csv(data[i], parse_dates=True, dayfirst=True)
                    else:
                        df1 = pd.read_excel(data[i])
                except FileNotFoundError:
                    error = f"{data[i]} not found"
                    messagebox.showerror("Error", error)
                    return error
            else:
                df1 = merged_df
            try:
                if data[i + 1].endswith(".csv"):
                    df2 = pd.read_csv(data[i + 1])
                    # df2 = pd.read_csv(data[i], parse_dates=True, dayfirst=True)
                else:
                    df2 = pd.read_excel(data[i + 1])
            except FileNotFoundError:
                error = f"{data[i + 1]} not found"
                messagebox.showerror("Error", error)
            # merged_df = pd.merge(df1, df2, how="outer")
            frames = [df1, df2]
            merged_df = pd.concat(frames, join="outer")
            i += 1
    else:
        try:
            if data[i].endswith(".csv"):
                merged_df = pd.read_csv(data[i])
                # merged_df = pd.read_csv(data[i], parse_dates=col["created_date"], dayfirst=True)
            else:
                merged_df = pd.read_excel(data[i])
        except FileNotFoundError:
            error = f"{data[i]} not found"
            messagebox.showerror("Error", error)
    print(merged_df)
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
    
def merge_data(sources, output, col):
    data = collect_data(sources)
    try:
        merged_df = find_and_merge(data, col)
    except:
        return
    merged_df = drop_column(merged_df) 
    return merged_df

def clear_entry(entries):
    for entry in entries:
        entry.delete(0, END)

def browse_file(fileEntry):
    files = []
    fileEntry.delete(0, END)
    filename = filedialog.askopenfiles(initialdir="/", title="select files", filetypes=(("csv files", "*.csv*"), ("all files", "*.*")))
    for file in filename:
        files.append(file.name)
    fileEntry.insert(0, files)
    print(files)
    return files

def get_filename_from_path(path):
    slash = path.count("/")
    i = 0
    j = 0
    print(path)
    while i < len(path):
        if j == slash:
            return path[i:]
        if path[i] == "/":
            j += 1
        i += 1 
