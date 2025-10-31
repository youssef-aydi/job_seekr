from tkinter import Tk
from tkinter import Toplevel
from numpy import tan
import main_window as mw

# pip install -r requirements.txt to install all packages necessary.


if __name__ == '__main__':
    main_window = mw.main_window(w=mw.WIDTH, h=mw.HEIGHT, title=mw.TITLE, bg_hex_color=mw.BG_HEX_COLOR, text_color=mw.TEXT_COLOR)

    main_window.add_image(mw.LOGO_PATH)
    text0 = main_window.add_text(mw.WEBSITES_TITLE, 'w')
    dropdown0, varw = main_window.add_dropdown(mw.WEBSITES, 45)
    text1 = main_window.add_text(mw.METHODS_TITLE, 'w')
    text2 = main_window.add_text(mw.CATEGORIES_TITLE, 'w')
    dropdown2, varc = main_window.add_dropdown(mw.CATEGORIES, 45)
    text3 = main_window.add_text(mw.KEYWORD_TITLE, 'w')
    field0 = main_window.add_input_field(width=39)
    dropdown1 = main_window.special_main_window_dropdown(mw.METHODS, 45, dropdown2, field0)
    button0 = main_window.add_button(mw.SEEK_BUTTON_TEXT)

    text1.pack(fill="both")
    dropdown1.pack()
    text0.pack(fill="both")
    dropdown0.pack()
    text2.pack(fill="both")
    dropdown2.pack()
    text3.pack(fill="both")
    field0.pack()
    mw.set_position(button0, 150, 480)

    mw.add_padding(text0, 20, 5)
    mw.add_padding(text1, 20, 5)
    mw.add_padding(text2, 20, 5)
    mw.add_padding(text3, 20, 5)
    mw.add_padding(button0, 10, 10)

    mw.disable_object(dropdown2)
    mw.disable_object(field0)
     
    button0.configure(command=lambda : mw.start_scraping(varw,varc,field0))
    
    main_window.start_window()
