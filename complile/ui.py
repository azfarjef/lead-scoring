from tkinter import *
from gen_data import gen_data
from utils import clear_entry
from widget import menu_widget, frame_widget, label_widget, entry_widget, grid_widget
from search import search
import pandas as pd

def ui():
    win = Tk()
    win.title("DHL Lead Generation")

    # menu
    subMenu = menu_widget(win)

    #frame
    frame = frame_widget(win)

    #labels
    label_0, label_1, label_2, label_3, label_4, label_5 = label_widget(frame)
    entries = entry_widget(frame)

    #entries
    fileEntry, saveEntry, searchEntry, fromEntry = entries

    #buttons
    gen_button = Button(frame, text="Generate", command=lambda: gen_data(fileEntry.get(), saveEntry.get()))
    search_button = Button(frame, text="Search", command=lambda: search(searchEntry.get(), fromEntry.get()))
    subMenu.add_command(label="New", command=lambda: clear_entry(entries))
    subMenu.add_command(label="Exit", command=win.quit)

    #grid
    widgets = [label_0, label_1, label_2, label_3, label_4, label_5, fileEntry, saveEntry, searchEntry, fromEntry, gen_button, search_button]
    grid_widget(widgets)
    
    win.mainloop()
