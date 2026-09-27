from tkinter import *

window = Tk()

first_name_label = Label(window, text="First name: ", width = 15).grid(row=0, column=0)
first_name_entry = Entry(window).grid(row=0, column=1)

last_name_label = Label(window, text="last name: ").grid(row=1, column=0)
last_name_entry = Entry(window).grid(row=1, column=1)

email_label = Label(window, text="Email: ").grid(row=2, column=0)
email_entry = Entry(window).grid(row=2, column=1)

submit_button = Button(window, text="submit").grid(row=3, column=0, columnspan=2)

window.mainloop()