from tkinter import messagebox
from tkinter import *
from show_table import show_result
import pandas as pd
import sys

def read_data(sheet):
    if sheet == "All":
        sheet = "Master data"
    try:
        df = pd.read_excel("output.xlsx", sheet_name=sheet)
    except FileNotFoundError:
        messagebox.showerror("Error", "master output not found")
    return df

def find_and_merge_data(entry, df, ret_df):
    if entry.isdigit():
        for index, row in df.iterrows():
            if entry == str(row["Unique Lead Assignment Number "]):
                temp = df.iloc[[index], :]
                ret_df = pd.merge(ret_df, temp, how="outer")
    else:
        for index, row in df.iterrows():
            if entry in row["Customer Name"].lower():
                temp = df.iloc[[index], :]
                ret_df = pd.merge(ret_df, temp, how="outer")
    print(ret_df)
    if ret_df.empty:
        error = "No results"
        messagebox.showinfo("message", "no results")
    return ret_df

def search(entry, mb_value):
    ret_df = pd.DataFrame(
            {
                "Customer Name": [],
                "Address": [],
                "City": [],
                "Business Nature": []
            }
    )
    try:
        df = read_data(mb_value)
    except:
        messagebox.showerror("Error", f"{mb_value} not found")
        return
    ret_df = find_and_merge_data(entry, df, ret_df) 
    if ret_df.empty == False:
        show_result(ret_df)
        ret_df.to_csv(entry + ".csv", index=False)
