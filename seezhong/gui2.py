from tkinter import *
from utils import gen_data, clear_entry 
from search import search
import pandas as pd
import tkinter.messagebox

def main():
    win = Tk()
    win.title("DHL Lead Generation")

    # menu
    menu = Menu(win)
    win.config(menu=menu)

    subMenu = Menu(menu)
    menu.add_cascade(label="File", menu=subMenu)
    subMenu.add_command(label="New", command=lambda: clear_entry(entries))
    subMenu.add_command(label="Exit", command=win.quit)

    # frame
    frame = Frame(win, bd=2, pady=10)
    frame.pack(fill=X)

    # label
    label_0 = Label(frame, text="Compile & Generate Data", font="helvatica 10 bold underline")
    label_1 = Label(frame, text="Sources", anchor=E) 
    label_2 = Label(frame, text="Save As...", anchor=E)
    label_3 = Label(frame, text="Search by Name", font="helvatica 10 bold underline", anchor=E)
    label_4 = Label(frame, text="Company Name", anchor=E)
    label_5 = Label(frame, text="From", anchor=E)

    # Entry
    fileEntry = Entry(frame)
    saveEntry = Entry(frame)
    searchEntry = Entry(frame)
    fromEntry = Entry(frame)
    entries = [fileEntry, saveEntry, searchEntry, fromEntry]

    # Button
    gen_button = Button(frame, text="Generate", command=lambda: gen_data(fileEntry.get(), saveEntry.get()))
    search_button = Button(frame, text="Search", command=lambda: search(searchEntry.get(), fromEntry.get()))

    # Grid 
    label_0.grid(sticky=W, row=0, columnspan=2, padx=5)
    label_1.grid(sticky=E, row=1, padx=5)
    label_2.grid(sticky=E, row=2, padx=5)
    label_3.grid(sticky=W, row=5, columnspan=2) 
    label_4.grid(sticky=E, row=6, padx=5)
    label_5.grid(sticky=E, row=7, padx=5)
    fileEntry.grid(row=1, column=1, pady=5, padx=3)
    saveEntry.grid(row=2, column=1, pady=5, padx=3)
    searchEntry.grid(row=6, column=1, pady=5, padx=3)
    fromEntry.grid(row=7, column=1, pady=5, padx=3)
    gen_button.grid(row=3, columnspan=2)
    search_button.grid(row=8, columnspan=2)

    win.mainloop()

if __name__ == "__main__":
    main()
