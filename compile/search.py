from tkinter import messagebox
from tkinter import *
from show_table import show_result
import pandas as pd
import sys
from gen_data import get_col_name

def read_columns(sheet):
    if sheet == "All":
        sheet = "Master data"
    try:
        df = pd.read_excel("results.xlsx", sheet_name=sheet)
    except FileNotFoundError:
        messagebox.showerror("Error", "master output not found")

def read_data(sheet):
    if sheet == "All":
        sheet = "Master data"
    try:
        df = pd.read_excel("output_backup.xlsx", sheet_name=sheet)
    except FileNotFoundError:
        messagebox.showerror("Error", "master output not found")
    return df

def find_and_merge_data(entry, df, ret_df, col):
    if entry.isdigit():
        print("hellooooooooooooooooooooooo")
        #entry = entry + ".0"
        for index, row in df.iterrows():
            if entry == str(row[col["unique_id"]]):
                temp = df.iloc[[index], :]
                frames = [ret_df, temp]
                ret_df = pd.concat(frames, join="outer")
                #ret_df = pd.merge(ret_df, temp, how="outer")
    else:
        for index, row in df.iterrows():
            if entry.lower() in row[col["name"]].lower():
                temp = df.iloc[[index], :]
                frames = [ret_df, temp]
                ret_df = pd.concat(frames, join="outer")
                #ret_df = pd.merge(ret_df, temp, how="outer")
    print(ret_df)
    if ret_df.empty:
        error = "No results"
        messagebox.showinfo("message", "no results")
    return ret_df

def search(entry, options_list):
    """
    columns = []
    cf = pd.read_csv("data/columns.csv")
    for index, row in cf.iterrows():
        columns.append(row.item().strip())
    """
    col = get_col_name()
    ret_df = pd.DataFrame(columns=[col["name"]])
    try:
        #df = read_data(options_list)
        df = pd.read_excel("output_backup.xlsx", sheet_name="Master data")
        temp_df = read_data(options_list) # temp_df to get columns
    except:
        messagebox.showerror("Error", f"{options_list} not found")
        return
    required_column = []
    for column in temp_df.columns:
        required_column.append(column)
    print(required_column)
    for column in df.columns:
        if column not in required_column:
            df = df.drop(column, axis=1)
    print(df.columns)
    ret_df = find_and_merge_data(entry, df, ret_df, col) 
    if ret_df.empty == False:
        show_result(ret_df)
        ret_df.to_csv(entry + ".csv", index=False)
