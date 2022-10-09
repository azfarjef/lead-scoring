from tkinter import *
from gen_data import gen_data
from utils import clear_entry, browse_file
from widget import menu_widget, frame_widget, label_widget, entry_widget, grid_widget, dropdown_widget
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
    compile_label, save_label, search_label, id_label = label_widget(frame)
    entries = entry_widget(frame)

    #entries
    fileEntry, saveEntry, searchEntry = entries

    #buttons
    browse_button = Button(frame, text="Browse", command=lambda: browse_file(fileEntry))
    gen_button = Button(frame, text="Generate", command=lambda: gen_data(fileEntry.get(), saveEntry.get()))
    search_button = Button(frame, text="Search", command=lambda: search(searchEntry.get(), option_list.get()))
    subMenu.add_command(label="New", command=lambda: clear_entry(entries))
    subMenu.add_command(label="Exit", command=win.quit)

    #dropdown
    
    om, option_list = dropdown_widget(frame)

    #grid
    widgets = [compile_label, browse_button, save_label, search_label, id_label, fileEntry, saveEntry, searchEntry, gen_button, search_button, om]
    grid_widget(widgets)

    win.mainloop()
