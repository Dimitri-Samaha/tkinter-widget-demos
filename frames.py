from tkinter import *
import time

window = Tk()

frame = Frame(window, bg="pink", bd=5, relief=SUNKEN)
frame.place(x=100, y=100)

Button(frame, text="W", font=("Consolas",25), width=3).pack(side="top")
Button(frame, text="A", font=("Consolas",25), width=3).pack(side="left")
Button(frame, text="S", font=("Consolas",25), width=3).pack(side="left")
Button(frame, text="D", font=("Consolas",25), width=3).pack(side="left")


window.mainloop()