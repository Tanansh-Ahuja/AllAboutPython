from tkinter import *


root=Tk()
root.geometry('600x600')
f=Frame(root,bg='yellow',padx=20,pady=10)
f.pack(side=TOP,padx=10,pady=10,fill=X)

text=Text(f)
text.pack()
f1=Frame(root,bg='red',padx=10,pady=10)
f1.pack(side=TOP,padx=5,pady=5,fill=X)
l=Label(f1,text='namaste')
l.pack()
root.mainloop()
