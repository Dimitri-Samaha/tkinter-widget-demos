from tkinter import *


def submit():
    try:
        print("You ordered")
        for index in listbox.curselection():
            food = listbox.get(index)
            print(food)
    except:
        print("You didn't choose anything to order")

def add():
    content = entry.get()
    listbox.insert(listbox.size()+1, content)
    listbox.config(height=listbox.size())

 
def delete():
    try:
        for index in reversed(listbox.curselection()):
            listbox.delete(index)
        listbox.config(height=listbox.size())
    except:
        print("You didnt choose anything to delete")

window = Tk()

listbox = Listbox(window,
                  bg = "grey",
                  font = ("Arial", 35),
                  width=10,
                  selectmode=MULTIPLE)

listbox.insert(0, "pizza")
listbox.insert(1, "pasta")
listbox.insert(2, "garlic bread")
listbox.insert(3, "soup")
listbox.insert(4, "salad")
listbox.config(height=listbox.size())
listbox.pack()

submit_button = Button(window, text="submit", command=submit)
submit_button.pack()

entry = Entry(window, font=("Arial", 35))
entry.pack()

entry_submit = Button(window, text= "add", command=add)
entry_submit.pack()

delete_button = Button(window, text="delete", command=delete)
delete_button.pack()

window.mainloop()   