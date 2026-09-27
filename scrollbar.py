from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Learn to code SCROLLBAR')
window.geometry("500x400")

# create a main frame
main_frame = Frame(window)
main_frame.pack(expand=1, fill="both")
Label(main_frame, text="HEHEHEHA").pack()
# create a canvas
my_canvas = Canvas(main_frame)
my_canvas.pack(side=LEFT, fill="both", expand = 1)
# add scroll to canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview)
my_scrollbar.pack(side=RIGHT, fill='y')
# config the canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("all")))
# create another frame inside the canvas
second_frame = Frame(my_canvas)
# add that frame to a window in the canvas
my_canvas.create_window((0, 0), window=second_frame, anchor="nw")

for i in range(100):
    Button(second_frame, text=f"Button {i}!").grid(row=i, column=0, pady=5)

Label(second_frame, text="It's not friday.").grid(row=3, column=2)

window.mainloop()