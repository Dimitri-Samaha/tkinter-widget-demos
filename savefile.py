from tkinter import *
from tkinter import filedialog

def saveFile():
    try:
        file = filedialog.asksaveasfile(initialdir="_",
                                        defaultextension=".txt", 
                                        filetypes=(("Text file", ".txt"), ("Html file", ".html"), ("All files", ".*")))
        file_text = str(text.get(1.0, END))
        file.write(file_text)
        file.close()
    except :
        return

    

window = Tk()

button = Button(window, text="save", command=saveFile)
button.pack()

text = Text(window)
text.pack()

window.mainloop()