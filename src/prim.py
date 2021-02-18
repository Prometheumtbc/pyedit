import sys

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
    import tkinter.filedialog

root = Tk("PyEdit")
text = Text(root) 
text.grid() 

def saveAs():

    global text

    t = text.get("1.0", "end-1c")

    savelocation = tkinter.filedialog.asksaveasfilename()

    file1 = open(savelocation, "w+")

    file1.write(t)

    file1.close()

button = Button(root, text="Save", command=saveAs) 
button.grid()

def fontHelvetica():

    global text

    text.config(font="Helvetica")

def fontCourier():

    global text

    text.config(font="Courier")


font = Menubutton(root, text="Font") 
font.grid() 
font.menu = Menu(font, tearoff=0) 
font["menu"] = font.menu
Helvetica = IntVar() 
arial = IntVar() 
times = IntVar() 
Courier = IntVar()
font.menu.add_checkbutton(label="Courier", variable=Courier, 
command=fontCourier)
font.menu.add_checkbutton(label="Helvetica", variable=Helvetica,
command=fontHelvetica) 
root.mainloop()