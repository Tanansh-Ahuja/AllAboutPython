from tkinter import *

def printf():
    print(user_value.get(),",",pass_value.get() )

root=Tk()
root.geometry("600x600")

user=Label(text="Username").grid(row=0,column=0)
password=Label(text="Password").grid(row=1,column=0)

user_value=StringVar()
pass_value=StringVar()


Entry(root,textvariable=user_value).grid(row=0,column=1)
Entry(root,textvariable=pass_value).grid(row=1,column=1)

Button(text="print",bg="black",fg="yellow",relief=RAISED,command=printf).grid(row=2,column=1)


root.mainloop()
