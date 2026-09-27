from tkinter import *

food = ["pizza", "hamburger", "hotdog"]

def order():
    if x.get() == 0:
        print("Pizza")
    elif x.get() == 1:
        print("hamburger")
    elif x.get() == 2:
        print("hotdog")
    else:
        print("huh?")

window = Tk()
 
x = IntVar()

for index in range(len(food)):
    radiobutton = Radiobutton(window,
                                text = food[index],
                                fg = "green",
                                bg = "black",
                                variable = x,
                                value=index,
                                indicatoron=0,
                                width=75,
                                command=order)
    radiobutton.pack(anchor="w")

window.mainloop()