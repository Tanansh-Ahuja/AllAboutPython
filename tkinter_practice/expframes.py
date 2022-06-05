from tkinter import *

root=Tk()
root.geometry("400x400")


f1=Frame(root,borderwidth=2,bg="yellow")

f1.pack(side=LEFT,fill=Y)


f2=Frame(root,borderwidth=2,bg="RED")
f2.pack()



Label(f1,text="this is frame 1").pack()
Label(f2,text="this is frame 2").pack()
Label(root,text="center",anchor="center").pack(anchor="center")

root.mainloop()
