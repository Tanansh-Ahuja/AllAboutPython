from Tkinter import *
import tkMessageBox
import Tkinter

top = Tk()
def p_sel():
    for inx in Lb1.curselection():
        print inx
    

Lb1 = Listbox(top,selectmode='multiple')
Lb1.insert(0, "Python")
Lb1.insert(1, "Perl")
Lb1.insert(2, "C")
Lb1.insert(3, "PHP")
Lb1.insert(4, "JSP")
Lb1.insert(5, "Ruby")

Lb1.pack()
b = Button(top, text="GET",command=p_sel)
b.pack()
top.mainloop()
