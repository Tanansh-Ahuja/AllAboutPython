
from tkinter import *

root=Tk()
root.geometry("700x500")

f2=Frame(root,bg="yellow",borderwidth=3,relief=GROOVE)
f2.pack(side=TOP,fill=X,pady=10)

f1=Frame(root,bg="red",borderwidth=8,relief=RIDGE)
f1.pack(side=LEFT,fill=Y,padx=10,pady=10)

l1=Label(f1,text="This is frame 1",bg="orange",relief=SUNKEN)
l1.pack(side=BOTTOM,fill=X)

l2=Label(f2,text="This is frame 2",bg="black",fg="yellow",relief=RIDGE)
l2.pack(side=RIGHT,fill=Y)

root.mainloop()
