from tkinter import *
from gen_data import gen_data
from utils import clear_entry
import pandas as pd

def menu_widget(root):
    menu = Menu(root)
    root.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    return subMenu

def frame_widget(root):
    frame = Frame(root, bd=2, pady=10)
    frame.pack(fill=X)
    return frame

def label_widget(root):
    label_0 = Label(root, text="Compile & Generate Data", font="helvatica 10 bold underline")
    #label_1 = Label(root, text="Sources", anchor=E)
    label_2 = Label(root, text="Save As...", anchor=E)
    label_3 = Label(root, text="Search by Name", font="helvatica 10 bold underline", anchor=E)
    label_4 = Label(root, text="ID / Company Name", anchor=E)
    #label_5 = Label(root, text="From", anchor=E)
    return label_0, label_2, label_3, label_4

def entry_widget(root):
    fileEntry = Entry(root)
    #fileEntry.insert(0, "data/scoring_A.csv, data/scoring_B.csv, data/scoring_C.csv")
    saveEntry = Entry(root)
    saveEntry.insert(0, "results")
    searchEntry = Entry(root)
    #fromEntry = Entry(root)
    entries = [fileEntry, saveEntry, searchEntry]
    return entries

def radio_widget(root):
    options = ["All", "Company info", "Sales", "Contact info", "Lead info", "Lead scores"]
    value_inside = StringVar()
    value_inside.set("All")
    mb = OptionMenu(root, value_inside, *options)
    return mb, value_inside

def grid_widget(widgets):
    widgets[0].grid(sticky=W, row=0, columnspan=2, padx=5)
    widgets[1].grid(sticky=E, row=1, padx=5)
    widgets[2].grid(sticky=E, row=2, padx=5)
    widgets[3].grid(sticky=W, row=5, columnspan=2) 
    widgets[4].grid(sticky=E, row=6, padx=5)
    #widgets[5].grid(sticky=E, row=7, padx=5)
    widgets[5].grid(row=1, column=1, pady=5, padx=3)
    widgets[6].grid(row=2, column=1, pady=5, padx=3)
    widgets[7].grid(row=6, column=1, pady=5, padx=3)
    #widgets[9].grid(row=7, column=1, pady=5, padx=3)
    widgets[8].grid(sticky=E, row=3, columnspan=2)
    widgets[9].grid(sticky=E, row=7, columnspan=2)
    widgets[10].grid(sticky=E, row=7, column=0) 
