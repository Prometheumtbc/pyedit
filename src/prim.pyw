import sys

try:
    # for Python2
    from Tkinter import *
except ImportError:
    # for Python3
    from tkinter import *
    import tkinter.filedialog

root = Tk("PyEdit")
root.title("PyEdit")
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

"""def load():

    global text

    t = text
    loadlocation = tkinter.filedialog.askopenfilename()
    file1 = open(loadlocation, "w+")

    file2 = file1.read()
    text.insert(file2)
    file1.close()

loadButton = Button(root, text="Load", command=load) 
loadButton.grid()"""

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