from tkinter import *
from PIL import Image, ImageTk

count = 0
def click():
    print("You clicked thee button" + count)
    count += 1
    return

window = Tk()

photo = PhotoImage(file="download.png")

button = Button(window, 
                text = "Click me!",
                command=click,
                font=("Comic Sans", 30),
                fg = "green",
                bg = "black",
                activeforeground="green", 
                activebackground="black",
                state=ACTIVE,
                image=photo,
                compound="bottom")
button.pack()

window.mainloop()