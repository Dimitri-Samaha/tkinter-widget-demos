from tkinter import *


def submit():
    user_name = entry.get()
    print("Hello  " + user_name)
    entry.config(state=DISABLED)
    return

def delete():
    entry.delete(0, END)
    return

def backspace():
    entry.delete(len(entry.get())-1, END)
    return

window = Tk()

entry = Entry(window, 
              font=("Arial", 50),
              fg="green",
              bg="black",
              show='.')
entry.insert(0, "SpongeBob")
entry.pack(side="left")

submit_button = Button(window, text="Submit", command=submit)
submit_button.pack(side="right")

delete_button = Button(window, text="Delete", command=delete)
delete_button.pack(side="right")

backspace = Button(window, text="Backspace", command= backspace)
backspace.pack(side="right")

window.mainloop()
