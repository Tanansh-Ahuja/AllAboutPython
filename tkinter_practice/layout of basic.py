from tkinter import *

    
def func(event):
    global st1
    global st2
    #global e1
    #global e2
    #st2.set('')
    #st1.set('')
    #e1.update()
    #e2.update()
    print('in func')
    b=''
    a=st1.get()
    print(a)
    for i in a:
        b=b+chr(ord(i)+1)
    e2.insert(0,b)
    e2.update()
    print(b)


def reset(event):
    global st1
    global st2
    st1.set('')
    st2.set('')
    e1.update()
    e2.update()
    



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
b1=Button(f2,text='press me',height=2)
b1.pack(side=TOP)
b1.bind('<Button-1>',func)
b1.bind('<Button-3>',reset)

st1=StringVar()
st1.set('')
st2=StringVar()
st2.set('')
e1=Entry(f1,textvariable=st1,show='*')
e1.pack(side=TOP,fill=X)
e2=Entry(f1,textvariable=st2)
e2.pack(side=TOP,fill=X)

#root.mainloop()

    
