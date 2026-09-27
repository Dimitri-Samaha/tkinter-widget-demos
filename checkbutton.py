from tkinter import *


def display():
    if x.get() == 1:
        print("You agree")
    else:
        print("You dont agree :(")

window = Tk()

x = IntVar()

icon = PhotoImage(file="download.png")

check_button = Checkbutton(window, 
                            text="I agree",
                            font=("Arial", 20),
                            fg="green",
                            bg = "black",
                            bd = 5,
                            relief= RAISED,
                            activeforeground="green",
                            activebackground="black",
                            padx=25,
                            pady= 10,
                            variable=x,
                            onvalue=1,
                            offvalue=0,
                            command=display,
                            image= icon,
                            compound=LEFT,)
check_button.pack()

window.mainloop()