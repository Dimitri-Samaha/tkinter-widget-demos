from tkinter import * 
from tkinter import filedialog

def openFile():
    file_path = filedialog.askopenfilename(initialdir="_",
                                            title="Open file",
                                            filetypes=(("text files", "*.txt"), ("python files", "*.py"), ("All files", "*.*")))
    try:
        file = open(file_path, "r")
        print(file.read())
        file.close()
    except FileNotFoundError :
        print("No such file")

window = Tk()

button = Button(window, text="Open", command=openFile)
button.pack()

window.mainloop()