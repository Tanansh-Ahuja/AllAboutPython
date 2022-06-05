from tkinter import *

root = Tk()

root.geometry("800x600")
root.maxsize(1000,700)
root.minsize(300,100)

f1=Frame(root, borderwidth=2,bg="yellow",relief=SUNKEN)
f1.pack(side=TOP,fill="y")

l=Label(f1,text="Project")
l.pack(pady=142)



root.mainloop()
