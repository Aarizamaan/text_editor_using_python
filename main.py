# AText Editor made using Tkinter
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox, filedialog
from tkinter.filedialog import *
from tkinter import colorchooser, font
from tkinter.scrolledtext import ScrolledText
from datetime import datetime, date
import time
import os
import webbrowser
from fpdf import FPDF
import openai

def hover(widget, entrance_fg, exit_fg, on_entrance, on_exit):
    widget.bind("<Enter>", func=lambda e: widget.config(
        bg=on_entrance,
        fg=entrance_fg
    ))

    widget.bind("<Leave>", func=lambda e: widget.config(
        bg=on_exit,
        fg=exit_fg
    ))

def redirect_to_chatgpt():
    chatgpt_url = "https://chat.openai.com/"
    webbrowser.open_new_tab(chatgpt_url)     


def redirect_to_blackbox():
    blackbox_url="https://www.blackbox.ai/"
    webbrowser.open_new_tab(blackbox_url) 

def redirect_to_grammarly():
    grammarly_url="https://app.grammarly.com/"
    webbrowser.open_new_tab(grammarly_url)


def redirect_to_gmail():
    gmail_url="https://mail.google.com/mail/u/0/#inbox?compose=new"
    webbrowser.open_new_tab(gmail_url)    

def convert_to_pdf(text_content, output_filename):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(0, 10, txt=text_content)
    pdf.output(output_filename)


def save_as_pdf():
    text_content = text.get("1.0", "end-1c")
    output_filename = filedialog.asksaveasfilename(defaultextension=".pdf",
                                                   filetypes=[("PDF files", "*.pdf"), ("All Files", "*.*")])
    if output_filename:
        convert_to_pdf(text_content, output_filename)



def set_a4_alignment():
    text.config(width=70)  # Set width suitable for A4 paper size
    text.config(justify='center')  # Set text alignment to center
     
     
def screen_menu():
    menu = Menu(root,font=('Calibri', 10))
    root.config(menu=menu)

    # File menu
    file_menu = Menu(menu, tearoff=False,font=('Calibri', 10))
    menu.add_cascade(label='File', menu=file_menu)

    file_menu.add_command(label=" New ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + N', command=new)
    file_menu.add_command(label=" Save ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + S', command=save)
    file_menu.add_command(label=" Save As ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + Shift + S', command=save_as)
    file_menu.add_command(label=" Open ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + O', command=open_file)
    file_menu.add_separator(background='#0084BA')

    file_menu.add_command(label=" Exit ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + Esc', command=exit_app)

    # Edit menu
    edit_menu = Menu(menu, tearoff=False,font=('Calibri',10))
    menu.add_cascade(label='Edit', menu=edit_menu)

    edit_menu.add_command(label=" Cut ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + X', command=cut)
    edit_menu.add_command(label=" Copy ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + C', command=copy)
    edit_menu.add_command(label=" Paste ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + V', command=paste)
    edit_menu.add_separator(background="#0084BA")

    edit_menu.add_command(label=" Undo ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + Z', command=undo)
    edit_menu.add_command(label=" Redo ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + U', command=redo)
    edit_menu.add_separator(background="#0084BA")

    edit_menu.add_command(label=" Select all ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + A', command=select_all)
    edit_menu.add_command(label=" Find ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + F', command=find_text)
    edit_menu.add_separator(background='#0084BA')

    edit_menu.add_command(label=" Insert date ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + D', command=insert_date)
    edit_menu.add_command(label=" Insert time ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', accelerator='Ctrl + Shift + T', command=insert_time)
    edit_menu.add_command(label=" Insert date and time ", background="#0084BA", foreground="white",
                          activebackground='black', font=('Calibri', 12), compound='left',
                          accelerator='Ctrl+ Shift + T', command=insertDateTime)
    edit_menu.add_separator(background='#0084BA')

    edit_menu.add_command(label=" Convert to Upper case ", background="#0084BA", foreground="white",
                          activebackground='black', font=('Calibri', 12), compound='left', command=upper_case,
                          accelerator='Ctrl + Shift + U')
    edit_menu.add_command(label=" Convert to Lower Case ", background="#0084BA", foreground="white",
                          activebackground='black', font=('Calibri', 12), compound='left', command=lower_case,
                          accelerator='Ctrl + Shift +  L')
    #view menu
    view_menu = Menu(menu, tearoff=False,font=('Calibri', 10))
    menu.add_cascade(label='View', menu=view_menu)
    view_menu.add_command(label=" Dark mode ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', command=dark_mode)

    view_menu.add_command(label=" Light mode ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', command=light_mode)
    view_menu.add_command(label=" Eye protection mode ", background="#0084BA", foreground="white",
                          activebackground='black', font=('Calibri', 12), compound='left', command=eye_protection_mode)

    view_menu.add_command(label=" Toggle Word Wrap ", background="#0084BA", foreground="white",
                          activebackground='black', font=('Calibri', 12), compound='left', command=toggle_word_wrap)
    #text menu
    text_menu = Menu(menu, tearoff=False,font=('Calibri', 10))
    menu.add_cascade(label='Text', menu=text_menu)

    text_menu.add_command(label=" Font Color ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', command=change_font_color)
    text_menu.add_command(label=" Change Font ", background="#0084BA", foreground="white", activebackground='black',
                          font=('Calibri', 12), compound='left', command=change_font_menu)
    text_menu.add_command(label=" Change font size ", background="#0084BA", foreground="white",
                          activebackground='black', font=('Calibri', 12), compound='left',
                          command=change_font_size_menu)
    text_menu.add_command(label=" Text background ", background="#0084BA", foreground="white", command=change_bg_color,
                          activebackground='black', font=('Calibri', 12), compound='left')
    text_menu.add_separator(background="#0084BA")

    text_menu.add_command(label=" Bold ", background="#0084BA", foreground="white", command=bold,
                          activebackground='black', font=('Calibri', 12), compound='left')
    text_menu.add_command(label=" Italic ", background="#0084BA", foreground="white", command=italic,
                          activebackground='black', font=('Calibri', 12), compound='left')
    text_menu.add_command(label=" Underline ", background="#0084BA", foreground="white", command=underline,
                          activebackground='black', font=('Calibri', 12), compound='left')
    text_menu.add_command(label=" Strike ", background="#0084BA", foreground="white", command=over_strike,
                          activebackground='black', font=('Calibri', 12), compound='left')
    #about menu
    about_menu = Menu(menu, tearoff=False,font=('Calibri', 10))
    menu.add_cascade(label='About', menu=about_menu)

    about_menu.add_command(label=" About Editora ", background="#0084BA", foreground="white", activebackground='black',
                           font=('Calibri', 12), compound='left', command=about)
    # about_menu.add_command(label=" Help ", background="#0084BA", foreground="white", activebackground='black',
    #                        font=('Calibri', 12), compound='left', command=help)

    #help menu
    help_menu=Menu(menu,tearoff=False,font=('Calibri', 10))
    menu.add_cascade(label='Help',menu=help_menu)
    help_menu.add_command(label=" Help ", background="#0084BA", foreground="white", activebackground='black',
                           font=('Calibri', 12), compound='left', command=help)
    


def WriteToFile(file):
    try:
        content = text.get(1.0, 'end')
        with open(file, 'w') as the_file:
            the_file.write(content)
    except IOError:
        pass


global filename


def save_as():
    input_file_name = filedialog.asksaveasfilename(defaultextension=".txt",
                                                   filetypes=[("All Files", "*.*"),
                                                              ("Text Documents", "*.txt"),
                                                              ("HTML", "*.html"), ("CSS", "*.css"),
                                                              ("JavaScript", "*.js")])

    if input_file_name:
        global filename
        filename = input_file_name
        x = ('{} - {}'.format(os.path.basename(filename), root.title()))
        root.title(x)

    return "break"


file_path = None

def new():
    global file_path

    message = messagebox.askyesno(
        "Are you sure?",
        "Do you want to save this file before creating a new one?"
    )

    if message:
        save()
        text.delete("1.0", END)

    else:
        text.delete("1.0", END)

    
def open_file():
    global file_path

    file_types = [
        ('Text Documents', "*.txt"),
        ('MS Word files', "*.docx"),
        ('All files', '*.*')
    ]

    file_path = askopenfilename(filetypes=file_types)

    if file_path == '':
        file_path = None
        return


    else:
        try:
            file1 = open(file_path, 'r')
            text.delete("1.0", END)
            data = file1.read()
            text.insert(END, data)
            root.title("AText - " + os.path.basename(file_path))
            file1.close()

        except FileNotFoundError:
            return

    
def save():
    global file_path

    file_types = [
        ('Text Documents', "*.txt"),
        ("MS Word files", '*.docx'),
        ('All files', '*.*')
    ]

    if file_path == None:
        file_path = asksaveasfilename(filetypes=file_types, defaultextension='.txt')

        if file_path == "":
            file_path = None

            return

        else:
            try:
                file1 = open(file_path, 'w')
                data = text.get("1.0", END)
                file1.write(data)
                root.title("AText" + os.path.basename(file_path))

            except FileNotFoundError:
                return


    else:
        file2 = open(file_path, 'w')
        data1 = text.get("1.0", END)
        file2.write(data1)
        root.title("AText" + os.path.basename(file_path))

    
def upper_case():
    content = text.get("1.0", END)
    text.delete("1.0", END)

    upper_content = content.upper()

    text.insert("1.0", upper_content)

def lower_case():
    content = text.get("1.0", END)
    text.delete("1.0", END)

    lower_content = content.lower()

    text.insert("1.0", lower_content)

def find_text():
    search_top_level = Toplevel(root)
    search_top_level.title('Find Text')
    search_top_level.transient(root)
    search_top_level.resizable(False, False)
    Label(search_top_level, text="Find:").grid(row=0, column=0, sticky='e')
    search_entry_widget = Entry(search_top_level, width=25)
    search_entry_widget.grid(row=0, column=1, padx=2, pady=2, sticky='we')
    search_entry_widget.focus_set()
    ignore_case_value = IntVar()
    Checkbutton(search_top_level, text='Ignore Case', variable=ignore_case_value).grid(row=1, column=1, sticky='e',
                                                                                       padx=2, pady=2)
    Button(search_top_level, text="Find", underline=0, relief='solid',
           command=lambda: search_output(
               search_entry_widget.get(), ignore_case_value.get(),
               text, search_top_level, search_entry_widget)
           ).grid(row=0, column=2, sticky='e' + 'w', padx=2, pady=2)

def search_output(needle, if_ignore_case, content_text, search_top_level, search_box):
    content_text.tag_remove('match', '1.0', END)
    matches_found = 0
    if needle:
        start_pos = '1.0'
        while True:
            start_pos = content_text.search(needle, start_pos, nocase=if_ignore_case, stopindex=END)
            if not start_pos:
                break

            end_pos = '{} + {}c'.format(start_pos, len(needle))
            content_text.tag_add('match', start_pos, end_pos)
            matches_found += 1
            start_pos = end_pos
        content_text.tag_config('match', background='yellow', foreground='blue')
    search_box.focus_set()
    matches_found_text = '{} matches found'.format(matches_found)
    search_top_level.title(matches_found_text)

def dark_mode():
    shortcut_bar['bg'] = '#202020'

    bold_button['bg'] = '#202020'
    bold_button['fg'] = 'white'
    hover(bold_button, on_entrance='#202020', on_exit='#202020', entrance_fg='white', exit_fg='white')

    italic_button['bg'] = '#202020'
    italic_button['fg'] = 'white'
    hover(italic_button, on_entrance='#202020', on_exit='#202020', entrance_fg='white', exit_fg='white')

    underline_button['bg'] = '#202020'
    underline_button['fg'] = 'white'
    hover(underline_button, on_entrance='#202020', on_exit='#202020', entrance_fg='white', exit_fg='white')

    over_strike_button['bg'] = '#202020'
    over_strike_button['fg'] = 'white'
    hover(over_strike_button, on_entrance='#202020', on_exit='#202020', entrance_fg='white', exit_fg='white')

    cut_button['bg'] = '#202020'
    cut_button['fg'] = 'white'
    hover(cut_button, on_entrance='#202020', on_exit='#202020', entrance_fg='white', exit_fg='white')

    copy_button['bg'] = '#202020'
    copy_button['fg'] = 'white'
    hover(copy_button, on_entrance='#202020', on_exit='#202020', entrance_fg='white', exit_fg='white')

    paste_button['bg'] = '#202020'
    paste_button['fg'] = 'white'
    hover(paste_button, on_entrance='#202020', on_exit='#202020', entrance_fg='white', exit_fg='white')

    undo_button['bg'] = '#202020'
    undo_button['fg'] = 'white'
    hover(undo_button, on_entrance='#202020', on_exit='#202020', entrance_fg='white', exit_fg='white')

    redo_button['bg'] = '#202020'
    redo_button['fg'] = 'white'
    hover(redo_button, on_entrance='#202020', on_exit='#202020', entrance_fg='white', exit_fg='white')

    select_button['bg'] = '#202020'
    select_button['fg'] = 'white'
    hover(select_button, on_entrance='#202020', on_exit='#202020', entrance_fg='white', exit_fg='white')

    root.config(bg='#565454')
    
def light_mode():
    shortcut_bar['bg'] = 'white'

    bold_button['bg'] = 'white'
    bold_button['fg'] = 'black'
    hover(bold_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')

    italic_button['bg'] = 'white'
    italic_button['fg'] = 'black'
    hover(italic_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')

    underline_button['bg'] = 'white'
    underline_button['fg'] = 'black'
    hover(underline_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')

    over_strike_button['bg'] = 'white'
    over_strike_button['fg'] = 'black'
    hover(over_strike_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')

    cut_button['bg'] = 'white'
    cut_button['fg'] = 'black'
    hover(cut_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')

    copy_button['bg'] = 'white'
    copy_button['fg'] = 'black'
    copy_button.config(highlightthickness=3, highlightbackground='black', default='active', highlightcolor='black')
    hover(copy_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')

    paste_button['bg'] = 'white'
    paste_button['fg'] = 'black'
    cut_button.config(highlightthickness=3, highlightbackground='black', default='active', highlightcolor='black')
    hover(paste_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')

    undo_button['bg'] = 'white'
    undo_button['fg'] = 'black'
    hover(undo_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')

    redo_button['bg'] = 'white'
    redo_button['fg'] = 'black'
    hover(redo_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')

    select_button['bg'] = 'white'
    select_button['fg'] = 'black'
    hover(select_button, on_entrance='#202020', on_exit='white', entrance_fg='white', exit_fg='black')

    root.config(bg='white')
    

def eye_protection_mode():
    root.config(bg='#9EFFF3')
    shortcut_bar.config(bg='#9EFFF3')

def change_font(event=None):
    global current_font_family
    global current_font_size
    current_font_family = font_family.get()
    current_font_size = font_size.get()
    text.configure(font=(current_font_family, current_font_size))
    

def change_font_size_menu():
    messagebox.showinfo(
        "Change font size via the ComboBox",
        "You can change the font size via the Font size ComboBox in the toolbar"
    )

def change_font_menu():
    messagebox.showinfo(
        "Change font via the ComboBox",
        "You can change the font via the Font ComboBox in the toolbar"
    )

def change_font_color():
    color = colorchooser.askcolor()
    text.config(fg=color[1])

def change_bg_color():
    color = colorchooser.askcolor()
    text.config(bg=color[1])


def bold():
    text_property = font.Font(font=text['font'])

    if text_property.actual()['weight'] == 'normal':
        text.configure(font=(current_font_family, current_font_size, 'bold'))

    elif text_property.actual()['weight'] == 'italic':
        text.configure(font=(current_font_family, current_font_size, 'bold', 'italic'))

    elif text_property.actual()['weight'] == 'bold':
        text.configure(font=(current_font_family, current_font_size, 'normal'))

    elif text_property.actual()['weight'] == 'underline':
        text.configure(font=(current_font_family, current_font_size, 'bold', 'underline'))

    

def italic():
    text_property = font.Font(font=text['font'])

    if text_property.actual()['weight'] == 'normal':
        text.configure(font=(current_font_family, current_font_size, 'italic'))

    elif text_property.actual()['weight'] == 'italic':
        text.configure(font=(current_font_family, current_font_size, 'normal'))

    elif text_property.actual()['weight'] == 'bold':
        text.configure(font=(current_font_family, current_font_size, 'italic', 'bold'))

    elif text_property.actual()['weight'] == 'underline':
        text.configure(font=(current_font_family, current_font_size, 'italic', 'underline'))

    

def underline():
    text_property = font.Font(font=text['font'])

    if text_property.actual()['weight'] == 'normal':
        text.configure(font=(current_font_family, current_font_size, 'underline'))

    elif text_property.actual()['weight'] == 'underline':
        text.configure(font=(current_font_family, current_font_size, 'normal'))

    elif text_property.actual()['weight'] == 'italic':
        text.configure(font=(current_font_family, current_font_size, 'normal', 'italic'))

    elif text_property.actual()['weight'] == 'bold':
        text.configure(font=(current_font_family, current_font_size, 'underline', 'bold'))

    
def over_strike():
    text_property = font.Font(font=text['font'])

    if text_property.actual()['weight'] == 'normal':
        text.configure(font=(current_font_family, current_font_size, 'overstrike'))

    elif text_property.actual()['weight'] == 'overstrike':
        text.configure(font=(current_font_family, current_font_size, 'normal'))

    elif text_property.actual()['weight'] == 'italic':
        text.configure(font=(current_font_family, current_font_size, 'overstrike', 'italic'))

    elif text_property.actual()['weight'] == 'bold':
        text.configure(font=(current_font_family, current_font_size, 'overstrike', 'bold'))



def toggle_word_wrap():
    if text['wrap'] == 'word':
        text.config(wrap='none')

    elif text['wrap'] == 'none':
        text.config(wrap='word')


def about():
    messagebox.showinfo(
        "About",
        "Editora is created by Students of CU"
    )


def help():
    messagebox.showinfo(
        "Help",
        """The functions are: \n
        You have several menus in this editor.\n
        You have many functions in the toolbar. \n
        You can change the modes, colors and fonts.\n
        You have many more features!"""
    )




def update_char_length(event=None):
    string_in_text = text.get('1.0', 'end-1c')
    string_length = len(string_in_text)
    chars_label['text'] = f'Total Characters: {string_length}'


def count(event):
    (line, letter) = map(int, event.widget.index("end-1c").split("."))
    words = len(text.get("1.0", "end-1c").split())

    lines_label['text'] = f'Total Lines: {line}'
    words_label['text'] = f'Total Words: {words}'


counter = 66600
running = False


def counter_label(event=None):
    def count_time():
        if running:
            global counter

            if counter == 66600:
                display = "Working time: 00:00:00"

            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("Working time: " + "%H:%M:%S")
                display = string

            time_label['text'] = display
            time_label.after(1000, count_time)
            counter += 1

    count_time()


def exit_app():
    message = messagebox.askyesno(
        "Do you want to exit?",
        "Do you want to save the file? "
    )

    if message:
        save_as()
        root.quit()

    else:
        root.quit()


def start(event=None):
    global running
    running = True
    counter_label(time_label)


def insert_date():
    today = date.today().strftime("%A, %d.%B %Y")
    text.insert("1.0", today)
    

def insert_time():
    today = time.strftime("%H:%M Uhr ")
    text.insert("1.0", today)
    

def insertDateTime():
    insert_date()
    insert_time()
    

def cut():
    text.event_generate("<<Cut>>")
    


def copy():
    text.event_generate("<<Copy>>")
    


def paste():
    text.event_generate("<<Paste>>")
    


def undo():
    text.edit_undo()
    


def redo():
    text.edit_redo()
    

def select_all():
    text.event_generate("<<SelectAll>>")
    


root = Tk()
root.resizable(True,True)
root.title("Editora")
root.geometry("950x600")


frame = Frame(root, bd=3, bg='white')
frame.place(relx=0.5, rely=0.11, relwidth=0.85, relheight=0.85, anchor='n')

text = ScrolledText(frame, height=100, width=150, padx=3, pady=5, undo=True, wrap='word')
text.pack()

default_font_family = "Calibri"
default_font_size = 14

shortcut_bar = Frame(root, height=40, bg='white')
shortcut_bar.pack(expand='no', fill='x')

fonts = font.families()
font_family = StringVar()
font_box = ttk.Combobox(shortcut_bar, width=30, textvariable=font_family, state='readonly')
font_box['values'] = fonts
font_box.current(fonts.index("Calibri"))
font_box.place(x=25, y=5)

current_font_family = 'Calibri'
current_font_size = 14

size_var = IntVar()
size = tuple(range(5, 90))
font_size = ttk.Combobox(shortcut_bar, width=14, textvariable=size_var, state='readonly')
font_size['values'] = size
font_size.current(size.index(14))
font_size.place(x=250, y=5)

lines_label = Label(root, text='Total lines: 0', fg='black', font=('Calibri', 12), relief='ridge', width=15, bg='white')
lines_label.place(x=70, y=45)

chars_label = Label(root, text='Total Characters: 0', fg='black', font=('Calibri', 12), relief='ridge', width=20,
                    bg='white')
chars_label.place(x=200, y=45)

words_label = Label(root, text='Total Words: 0', fg='black', font=('Calibri', 12), relief='ridge', width=15, bg='white')
words_label.place(x=370, y=45)

time_label = Label(root, text='Working time: 00:00', fg='black', font=('Calibri', 12), relief='ridge', width=20,
                   bg='white')
time_label.place(x=500, y=45)

###############BUTTON CREATION########################################
#icon loading
cut_icon = PhotoImage(file="cuticon.png")
copy_icon= PhotoImage(file="copyicon (2).png")
paste_icon= PhotoImage(file="pasteicon.png")
strike_icon=PhotoImage(file="strikeicon.png")
selectall_icon=PhotoImage(file="selectallicon.png")
grammarly_icon=PhotoImage(file="grammarlyicon.png")
chatgpt_icon=PhotoImage(file="chatgpticon2.png")
pdf_icon=PhotoImage(file="pdficon2.png")
gmail_icon=PhotoImage(file="gmailicon.png")
###button

bold_button = Button(shortcut_bar, text='B', relief=FLAT, fg='black', font=('Arial', 12, 'bold'), bg='white',
                     height=1, command=bold)
hover(bold_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
bold_button.place(x=380, y=(-1))

italic_button = Button(shortcut_bar, text='I', relief=FLAT, fg='black', font=('Arial', 12, 'italic'), bg='white',
                       command=italic)
hover(italic_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
italic_button.place(x=410, y=(-1))

underline_button = Button(shortcut_bar, text='U', relief=FLAT, fg='black', font=('Arial', 12, 'underline'), bg='white',
                          command=underline)
hover(underline_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
underline_button.place(x=435, y=(-1))

over_strike_button = Button(root, image=strike_icon, relief=FLAT, fg='black', font=('Arial', 12, 'overstrike'), bg='white',
                            command=over_strike)

hover(over_strike_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
over_strike_button.place(x=470, y=(-1))

cut_button = Button(root, image=cut_icon, relief=FLAT, fg='black', font=('Arial', 12), bg='white', command=cut, height=0,
                    )
hover(cut_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
cut_button.place(x=520, y=(-1))

copy_button = Button(root, image=copy_icon, relief=FLAT, fg='black', font=('Arial', 12), bg='white', command=copy, height=0,
                     )
hover(copy_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
copy_button.place(x=560, y=(-1))

paste_button = Button(root, image=paste_icon, relief=FLAT, fg='black', font=('Arial', 12), bg='white', command=paste,
                      height=0)
hover(paste_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
paste_button.place(x=600, y=(-1))

undo_button = Button(shortcut_bar, text='⬅', relief=FLAT, fg='black', font=('Arial', 15), bg='white',
                     command=undo)
hover(undo_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
undo_button.place(x=640, y=-3)

redo_button = Button(shortcut_bar, text='➡', relief=FLAT, fg='black', font=('Arial', 15), bg='white',
                     command=redo)
hover(redo_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
redo_button.place(x=680, y=-3)

select_button = Button(shortcut_bar, image=selectall_icon, relief=FLAT, fg='black', font=('Arial', 12), bg='white',
                       command=select_all)
hover(select_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
select_button.place(x=720, y=0)

grammarly_button = Button(shortcut_bar,image=grammarly_icon, relief=FLAT, fg='black', font=('Arial', 12), bg='white',
                       command=redirect_to_grammarly)
hover(grammarly_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
grammarly_button.place(x=760, y=0)

chatgpt_button = Button(shortcut_bar,image=chatgpt_icon, relief=FLAT, fg='black', font=('Arial', 12), bg='white',
                       command=redirect_to_chatgpt)
hover(chatgpt_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
chatgpt_button.place(x=790, y=0)

pdf_button=Button(shortcut_bar,image=pdf_icon, relief=FLAT, fg='black', font=('Arial', 12), bg='white',
                       command=save_as_pdf)
hover(pdf_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
pdf_button.place(x=820, y=0)

gmail_button=Button(shortcut_bar,image=gmail_icon, relief=FLAT, fg='black', font=('Arial', 12), bg='white',
                       command=redirect_to_gmail)
hover(gmail_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
gmail_button.place(x=860, y=0)


a4_button=Button(shortcut_bar,text='A4', relief=FLAT, fg='black', font=('Arial', 12), bg='white',
                       command=set_a4_alignment)
hover(a4_button, on_entrance='#0084BA', on_exit='white', entrance_fg='white', exit_fg='black')
a4_button.place(x=890, y=0)


# Define descriptions for each button
button_descriptions = {
    bold_button: "Bold",
    italic_button: "Italic",
    underline_button: "Underline",
    over_strike_button: "Strike Through",
    cut_button: "Cut",
    copy_button: "Copy",
    paste_button: "Paste",
    undo_button: "Undo",
    redo_button: "Redo",
    select_button: "Select All",
    grammarly_button: "Open Grammarly",
    chatgpt_button: "Open ChatGPT",
    pdf_button: "Save as PDF",
    gmail_button: "Go to Gmail"
}

# Function to show tooltip
def show_tooltip(description, x, y):
    tooltip_label.config(text=description)
    tooltip_label.place(x=x, y=y + 30)  # Adjust 30 according to the distance you want from the button

# Function to hide tooltip
def hide_tooltip():
    tooltip_label.config(text="")
    tooltip_label.place_forget()

# Create tooltip label
tooltip_label = Label(root, text="", bg="white", fg="black")

# Bind events to show and hide tooltip when mouse enters and leaves buttons
for button, description in button_descriptions.items():
    button.bind("<Enter>", lambda event, desc=description, btn=button: show_tooltip(desc, btn.winfo_rootx(), btn.winfo_rooty()))
    button.bind("<Leave>", lambda event: hide_tooltip())
# Bindings

bindtags = list(text.bindtags())
bindtags.insert(2, "custom")
text.bindtags(tuple(bindtags))
text.bind_class("custom", "<Key>", count)

font_box.bind("<<ComboboxSelected>>", change_font)
font_size.bind("<<ComboboxSelected>>", change_font)

text.bind('<KeyPress>', update_char_length)
text.bind('<KeyRelease>', update_char_length)

text.bind('<KeyPress>', start(time_label))

#text.bind("<Key>", last_character)

text.config(font=(default_font_family, default_font_size))

screen_menu()
root.protocol("WM_DELETE_WINDOW", exit_app)
root.mainloop()
