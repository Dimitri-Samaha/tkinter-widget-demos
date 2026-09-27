from tkinter import *
## for png file only
from PIL import ImageTk, Image

window = Tk()
window.geometry("620x420")
window.title("First GUI program")
window.config(background="blue") ## String or hex value vcolor
icon = ImageTk.PhotoImage(Image.open("sunset.jpg")) ## icon to photoimage for png
window.iconphoto(True, icon) ## chenge icon
label = Label(window, 
              text="Label", 
              font=('Arial', 40, 'bold'), 
              fg="green", 
              bg="black",
              relief="raised",
              bd= 10,
              padx= 20,
              pady= 20,
              compound = 'bottom',
              image = icon)
label.place(x=0, y=0)
##label.pack()  

window.mainloop()
