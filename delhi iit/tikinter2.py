#from tkinter import *
#import tkmessagebox
import tkinter as tk

top=tk.Tk()

def p_h():
    print("Hello")
    mb=Menubutton( top, text="Condiments", relief=RAISED)
    mb.grid()
    mb.menu = Menu(mb, tearoff=0)
    mb["menu"]=mb.menu
    mayoVar=IntVar()
    ketchVar=IntVar()
    mb.menu.add_checkbutton(label="mayo",variable=mayoVar,command=p_h)
    mb.menu.add_checkbutton(label="ketchup",variable=KetchVar)
    mb.pack()
    top.mainloop()
