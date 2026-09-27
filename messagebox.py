from tkinter import *
from tkinter import messagebox 

def click():
    # messagebox.showinfo(title="Info message", message="Hello")
    # messagebox.showwarning(title='Warning', message="YOU HAVE A VIRAUS!")
    # messagebox.showerror(title="ERROR", message="You got an error :(")
    # messagebox.askokcancel(title="Question?", message="Do you want to do a thing?")
    # messagebox.askretrycancel(title="Question?", message="Do you want to retry a thing?")
    # messagebox.askyesno(title="Question?", message="Do you agree?")
    # messagebox.askquestion(title="Yes or No?", message="Do you like me?")
    # messagebox.askyesnocancel(title="Yes, No or Cancel", message="Are you gay?")
    pass


window = Tk()

button = Button(window, command=click, text="Click me")
button.pack()

window.mainloop()