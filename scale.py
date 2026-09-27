from tkinter import *

def submit():
    print(f"The tempreture is {scale.get()} degrees C")


window = Tk()

scale = Scale(window, 
                from_=0, 
                to=100,
                length=300,
                orient="horizontal",
                font = ("Arial", 10),
                tickinterval=10,
                showvalue=1,
                resolution=5,
                troughcolor="blue",
                fg = "red",
                bg = 'black')
scale.set((scale['from']+scale['to'])/2)
scale.pack()


button = Button(window, text="submit", command=submit)
button.pack()

window.mainloop()
