from tkinter import *
from tkinter import ttk
import pandas as pd

def scrollbar(tree, root):
    bar = Scrollbar(root, orient="horizontal", command=tree.xview)
    bar.pack(side="bottom", fill=X)
    tree.configure(xscrollcommand=bar.set)

def show_result(df):
    win = Tk()
    win.title("Treeview Demo")

    columns = []
    for column in df.columns:
        columns.append(column.strip())
    tree = ttk.Treeview(win, columns=columns, show="headings")
    scrollbar(tree, win)
    for column in columns:
        tree.heading(column, text=column)
    for index, row in df.iterrows():
        content = []
        for value in row.values:
            content.append(value)
        tree.insert("", END, values=content)
    tree.pack()

    win.mainloop()
