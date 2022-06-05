from tkinter import *

def printf():
    print("Its printing!!")


root=Tk()
root.geometry("700x400")

f1=Frame(root,borderwidth=2,bg="grey",relief=SUNKEN)
f1.pack(side=LEFT,anchor="nw")

b1=Button(f1,fg="red",text="print now",command=printf)
b1.pack(side=LEFT)

b2=Button(f1,fg="red",text="print now",command=printf)
b2.pack(side=RIGHT)

b3=Button(f1,fg="red",text="print now",command=printf)
b3.pack(side=LEFT)

b4=Button(f1,fg="red",text="print now",command=printf)
b4.pack(side=LEFT)

root.mainloop()
