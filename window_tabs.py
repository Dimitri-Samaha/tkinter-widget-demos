from tkinter import *
from tkinter import ttk

window = Tk()

note_book = ttk.Notebook(window)

tab1 = Frame(note_book) # new frame for tab1
tab2 = Frame(note_book) # new frame for tab2

note_book.add(tab1, text="tab1")
note_book.add(tab2, text="tab2")
note_book.grid() # Expands and fills any space not otherwise used

Label(tab1, text="Hello this is tab 1", width=50, height = 25).pack()
Label(tab2, text="Hello this is tab 2", width=50, height = 25).pack()


window.mainloop()