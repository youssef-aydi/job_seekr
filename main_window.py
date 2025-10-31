from os import error
from tkinter import *
from PIL import Image, ImageTk
from scrapers import indeed_scraper as indeed
from scrapers import linkedin_scraper as linkedin
from scrapers import rpj_scraper as rpj
import secondary_window as sw


WIDTH = 400
HEIGHT = 550
TITLE = "Job Seeker - Apply Right"
LOGO_PATH = "./assets/logo.png"
BG_HEX_COLOR = '#eb1087'
TEXT_COLOR = 'white'
WEBSITES = ["RP Jobsite", "LinkedIn", "Indeed"]
WEBSITES_TITLE = "Website to use:"
METHODS = ["Seek everything", "Seek a category", "Seek a keyword"]
METHODS_TITLE = "Method to use:"
CATEGORIES = ["Software & Data", "Science", "Engineering", "Sales & Marketing", "Healthcare", "Business",
              "Education", "Media", "Technology", "Social Services"]
CATEGORIES_TRANSLATE = ["data", "science", "sngineering", "marketing", "health", "business",
              "education", "media", "technology", "social"]
CATEGORIES_TITLE = "Categories / Fields:"
KEYWORD_TITLE = "Seek Keyword:"
SEEK_BUTTON_TEXT = "Seek now!"


current_method = "method_all"
current_website = "RP Jobsite"
current_category = "Software & Data"
current_keyword = ""

class main_window:
    window = Tk()

    def __init__(self, w, h, title, bg_hex_color, text_color):
        self.w = w
        self.h = h
        self.title = title
        self.bg_hex_color = bg_hex_color
        self.text_color = text_color
        self.create_window()

    def start_window(self):
        self.window.mainloop()

    def create_window(self):
        pos_w = int(self.window.winfo_screenwidth() / 2 - self.w / 2)
        pos_h = int(self.window.winfo_screenheight() / 2 - self.h / 2)
        size_and_pos = str(self.w) + 'x' + str(self.h) + '+' + str(pos_w) + '+' + str(pos_h)
        self.window.geometry(size_and_pos)
        self.window.title(self.title)
        self.window.resizable(False, False)
        self.window['background'] = self.bg_hex_color
        image = PhotoImage(file='./assets/logo_icon.png')
        self.window.wm_iconphoto(True, image)

    def get_window_position(self):
        pos_w = int(self.window.winfo_screenwidth() / 2 - self.w / 2)
        pos_h = int(self.window.winfo_screenheight() / 2 - self.h / 2)
        return pos_w, pos_h

    def add_image(self, image_path):
        # tk.Label(self.window, text="Username").place(x=40, y=60)
        data = Image.open(image_path)
        image = ImageTk.PhotoImage(data)
        my_label = Label(self.window, image=image, bg=self.bg_hex_color)
        my_label.image = image
        my_label.pack()

    def add_text(self, some_text, anchor):  # anchor? align text: 'w' => right 'e' => left 'center' => center
        my_text = Label(self.window, text=some_text, bg=self.bg_hex_color, fg=self.text_color,
                           font=("Arial", 12, "bold"), anchor=anchor)
        return my_text

    def add_dropdown(self, my_list, width):
        var = StringVar(self.window)
        var.set(my_list[0])
        dropdown = OptionMenu(self.window, var, *my_list)
        dropdown.config(bg=self.bg_hex_color, fg=self.text_color, font=("Arial", 10, "bold"),
                        activeforeground=self.bg_hex_color, width=width, direction='right')

        dropdown["menu"].configure(bg=self.bg_hex_color, activebackground='#4c1b45', fg=self.text_color)
        return dropdown, var

    def special_main_window_dropdown(self, my_list, width, my_dropdown, my_field):
        var = StringVar(self.window)
        var.set(my_list[0])

        dropdown = OptionMenu(self.window, var, *my_list,
                                 command=lambda x: update_dropdowns(var, my_list, my_dropdown, my_field))

        dropdown.config(bg=self.bg_hex_color, fg=self.text_color, font=("Arial", 10, "bold"),
                        activeforeground=self.bg_hex_color, width=width, direction='right')

        dropdown["menu"].configure(bg=self.bg_hex_color, activebackground='#4c1b45', fg=self.text_color)
        return dropdown

    def add_input_field(self, width):
        field = Entry(self.window, width=width, font=("Arial", 12, "bold"), fg='#4c1b45',
                         disabledbackground='#4c1b45')
        return field

    def add_button(self, button_text):
        button = Button(self.window, text=button_text, bg=self.bg_hex_color, font=("Arial", 10, "bold"),
                           fg=self.text_color, activeforeground=self.bg_hex_color, relief="groove", bd=5)
        return button

def set_position(my_object, x, y):
    my_object.place(x=x, y=y)


def add_padding(my_object, padx, pady):
    my_object.config(padx=padx, pady=pady)


def disable_object(my_object):
    my_object.config(state="disabled")


def enable_object(my_object):
    my_object.config(state="normal")

def update_dropdowns(var, methods, my_dropdown, my_input_field):
    global current_method
    temp = var.get()
    if temp == methods[0]:
        print("0")
        disable_object(my_dropdown)
        disable_object(my_input_field)
        current_method = "method_all"
    elif temp == methods[1]:
        print("1")
        enable_object(my_dropdown)
        disable_object(my_input_field)
        current_method = "method_category"
    elif temp == methods[2]:
        print("2")
        disable_object(my_dropdown)
        enable_object(my_input_field)
        current_method = "method_keyword"

def start_scraping(varw,varc,field):
    global current_method, current_website, current_category, current_keyword
    current_website = varw.get()
    current_category  = varc.get()
    current_keyword = field.get()
    print("Button Clicked:\r\nMethod: " + current_method)
    print("Website: " + current_website)
    print("Category: " + current_category)
    print("Keyword: " + current_keyword)
    if current_method == "method_all":
        scrape_all()
    elif current_method == "method_category":
        scrape_by_category()
    elif current_method == "method_keyword":
        scrape_by_keyword()

def scrape_all():
    global current_website
    if current_website == WEBSITES[0]:
        df = rpj.find_all_jobs()
        t = "Results of: RPJ Search All"
    elif current_website == WEBSITES[1]:
        df = linkedin.find_all_jobs()
        t = "Results of: LINEKDIN Search All"
    elif current_website == WEBSITES[2]:
        df = indeed.find_all_jobs()
        t = "Results of: INDEED Search All"
    else:
        print("Error occured when passing current website")
        df = None
    if df is not None:
        table_window = sw.secondary_window(root=main_window.window,w=1000, h=550, title=t, bg_hex_color=BG_HEX_COLOR, text_color=TEXT_COLOR)
        table_window.add_table(df)
        table_window.window.grab_set()
        
def category_to_keyword(category):
    if category == CATEGORIES[0]:
        return CATEGORIES_TRANSLATE[0]
    if category == CATEGORIES[1]:
        return CATEGORIES_TRANSLATE[1]
    if category == CATEGORIES[2]:
        return CATEGORIES_TRANSLATE[2]    
    if category == CATEGORIES[3]:
        return CATEGORIES_TRANSLATE[3]
    if category == CATEGORIES[4]:
        return CATEGORIES_TRANSLATE[4]
    if category == CATEGORIES[5]:
        return CATEGORIES_TRANSLATE[5]
    if category == CATEGORIES[6]:
        return CATEGORIES_TRANSLATE[6]
    if category == CATEGORIES[7]:
        return CATEGORIES_TRANSLATE[7]
    if category == CATEGORIES[8]:
        return CATEGORIES_TRANSLATE[8]
    if category == CATEGORIES[9]:
        return CATEGORIES_TRANSLATE[9]
def scrape_by_category():
    global current_website
    if current_website == WEBSITES[0]:
        df = rpj.find_keyword_jobs(category_to_keyword(current_category))
        t = "Results of: RPJ Search By Category"
    elif current_website == WEBSITES[1]:
        df = linkedin.find_keyword_jobs(category_to_keyword(current_category))
        t = "Results of: LINEKDIN Search By Category"
    elif current_website == WEBSITES[2]:
        df = indeed.find_keyword_jobs(category_to_keyword(current_category))
        t = "Results of: INDEED Search By Category"
    else:
        print("Error occured when passing current website")
        df = None
    if df is not None:
        table_window = sw.secondary_window(root=main_window.window,w=1000, h=550, title=t, bg_hex_color=BG_HEX_COLOR, text_color=TEXT_COLOR)
        table_window.add_table(df)
        table_window.window.grab_set()


def scrape_by_keyword():
    global current_website
    if current_website == WEBSITES[0]:
        df = rpj.find_keyword_jobs(current_keyword)
        t = "Results of: RPJ Search By Keyword"
    elif current_website == WEBSITES[1]:
        df = linkedin.find_keyword_jobs(current_keyword)
        t = "Results of: LINEKDIN Search By Keyword"
    elif current_website == WEBSITES[2]:
        df = indeed.find_keyword_jobs(current_keyword)
        t = "Results of: INDEED Search By Keyword"
    else:
        print("Error occured when passing current website")
        df = None
    if df is not None:
        table_window = sw.secondary_window(root=main_window.window,w=1000, h=550, title=t, bg_hex_color=BG_HEX_COLOR, text_color=TEXT_COLOR)
        table_window.add_table(df)
        table_window.window.grab_set()
