from tkinter import *
import cv2

from click import open_file

def open_file():
    print("File has been opened")

def save_file():
    print("File has been saved")

def cut():
    print("You cut something")

def copy():
    print("You copied something")

def paste():
    print("You pasted something")


window = Tk()

paste_icon = PhotoImage(file="download.png")

menu_bar = Menu(window)
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0, font=("MV Boli", 10))
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0, font=("MV Boli", 10))
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_separator()
edit_menu.add_command(label="Paste", command=paste, image=paste_icon, compound="left")



window.mainloop()