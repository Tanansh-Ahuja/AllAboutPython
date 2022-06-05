from tkinter import *




root=Tk()
root.title('ERROR!!!')
root.geometry('300x100+500+300')
root.maxsize(300,100)
root.minsize(300,100)

l1=Label(root,text="The Passwords dont match! \n Re-enter the password", bg='white',font=('Calibri',15))
l1.pack(side=TOP,fill=X)
b1=Button(root,text="Ok",relief=RAISED,borderwidth=5,bg='light grey',padx=20,pady=2)
b1.pack(padx=5,pady=10)

root.mainloop()
