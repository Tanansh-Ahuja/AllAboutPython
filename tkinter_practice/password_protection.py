from tkinter import *

root=Tk()

root.geometry('600x600')
root.title('Experiments')

st1=StringVar()
st1.set('')

e1=Entry(root,textvariable=st1,show='*')
e1.pack(side=TOP,fill=X)

root.mainloop()
