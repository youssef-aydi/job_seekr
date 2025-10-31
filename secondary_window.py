from tkinter import *
import pandas as pandas
from pandas.core.frame import DataFrame
from pandastable import Table, TableModel
class secondary_window():
    
    def __init__(self, root, w, h, title, bg_hex_color, text_color):
        self.window = Toplevel(root)
        self.w = w
        self.h = h
        self.title = title
        self.bg_hex_color = bg_hex_color
        self.text_color = text_color
        self.create_window()
        
    def create_window(self):
        pos_w = int(self.window.winfo_screenwidth() / 2 - self.w / 2)
        pos_h = int(self.window.winfo_screenheight() / 2 - self.h / 2)
        size_and_pos = str(self.w) + 'x' + str(self.h) + '+' + str(pos_w) + '+' + str(pos_h)
        self.window.geometry(size_and_pos)
        self.window.title(self.title)
        self.window.resizable(False, False)
        self.window['background'] = self.bg_hex_color
        
        
    def add_table(self, df):
        table = Table(self.window, dataframe=df, editable=True, enable_menus=False, showtoolbar=False, showstatusbar=True, font=("Arial", 8, "bold"),
                      align= 'center', colheadercolor='#4c1b45', colselectedcolor='#4c1b45',cellbackgr=self.bg_hex_color, textcolor='white',
                      rowselectedcolor= '#4c1b45', boxoutlinecolor=self.bg_hex_color)
        table.show()
        table.tablecolheader.colselectedcolor = self.bg_hex_color
        table.rowheader.grid_forget()
        table.rowindexheader.grid_forget()
        return table
    
    def add_text(self, some_text, anchor):  # anchor? align text: 'w' => right 'e' => left 'center' => center
        my_text = Label(self.window, text=some_text, bg=self.bg_hex_color, fg=self.text_color,
                           font=("Arial", 12, "bold"), anchor=anchor)
        return my_text