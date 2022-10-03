from tkinter import *
from tkinter import ttk
import pandas as pd

def show_table(df):
    win = Tk()
    win.title("search result")
    columns = []
    row = 0
    for column in df.columns:
        columns.append(column)
        row += 1
    tree = ttk.Treeview(win, columns=columns, height=row) 
    scroll = ttk.Scrollbar(win, orient="horizontal", command=tree.xview)
    i = 0
    while i < len(columns):
        if i == 0:
            tree.heading("#0", text=columns[0])
            tree.column("#0", width=100)
        else:
            tree.heading(columns[i], text=columns[i])
            tree.column(columns[i], width=100)
        i += 1
    tree.pack()
    scroll.pack(fill=Y)
    win.mainloop()
