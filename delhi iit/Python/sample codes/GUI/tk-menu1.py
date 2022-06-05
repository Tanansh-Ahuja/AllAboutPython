from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()

def p_h():
    print 'hello'
mb=  Menubutton ( top, text="condiments", relief=RAISED )
mb.grid()
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
    
mayoVar  = IntVar()
ketchVar = IntVar()

mb.menu.add_checkbutton ( label="mayo",variable=mayoVar,command=p_h )
mb.menu.add_checkbutton ( label="ketchup",variable=ketchVar )

mb.pack()
top.mainloop()
