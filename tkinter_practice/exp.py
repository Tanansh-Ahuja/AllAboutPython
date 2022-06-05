from tkinter import *

class one:

    def __init__(self,starg):
        self.st=starg

    def func(self,event):
        print(self.st)
    
#main
root=Tk()



root.geometry('600x600')
root.title('Experiments')

f1=Frame(root,padx=5,pady=5,bg='red',borderwidth=8,relief=SUNKEN,height=300)
f1.pack(side=TOP,fill=X,padx=5,pady=5)
f2=Frame(root,padx=5,pady=5,bg='orange',borderwidth=8,relief=RIDGE)
f2.pack(side=TOP,fill=X,padx=5,pady=5)
l1=Label(f1,padx=2,pady=2,text='Label 1',font=('Times new roman',20,'bold'),borderwidth=2,relief=RAISED)
l1.pack(side=TOP)
l2=Label(f2,padx=2,pady=2,text='Label 2',font=('Times new roman',20,'bold'),borderwidth=2,relief=RAISED)
l2.pack(side=TOP)

#st=""
st=StringVar()
st.set('')
e1=Entry(f1,textvariable=st)
e1.pack(side=TOP,fill=X)

b1=Button(f2,text='press me',height=2)
b1.pack(side=TOP)
b1.bind('<Button-1>',func)



root.mainloop()
