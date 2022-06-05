from tkinter import *


def func(event):
    global st1
    global text
    global text1
    a=text.get('1.0',END)
    for i in a:
        text1.insert(END,i)

def reset(event):
    global text
    global text1
    print('in reset')

    #text.insert(END,'')
    text.delete('1.0',END)

def delete(event):
    global f1
    f1.destroy()
    

    
root=Tk()
root.geometry('700x700+2+2')

f=Frame(root,bg='yellow',padx=5,pady=5,relief= RIDGE, borderwidth=3)
f.pack(anchor=N,padx=5,pady=5,fill=BOTH,expand=1)

f1=Frame(root,bg='Yellow',padx=5,relief=RIDGE, borderwidth=3)
f1.pack(anchor=N,padx=5,pady=5,fill=BOTH,expand=1)

f2=Frame(root,bg='blue',padx=5,pady=5,relief=RIDGE, borderwidth=3)
f2.pack(side=TOP,padx=5,pady=5)

l1=Label(f,text='Please enter your text here: ',padx=5,pady=5,font=('Calibri',10,'bold'),relief=GROOVE, borderwidth=3,bg='orange')
l1.pack(anchor=NW,padx=15,pady=5)

l2=Label(f1,text='Your crypted text is: ',padx=5,pady=5,font=('Calibri',10,'bold'),relief=GROOVE, borderwidth=3,bg='orange')
l2.pack(anchor=NW,padx=15,pady=5)


text=Text(f,height=11,width=80,bg='black',font=('Times new roman',12,'bold'),fg='yellow')
text.place(relx=0.5,rely=0.5,anchor=CENTER)

text1=Text(f1,height=11,width=80,bg='grey',font=('Times new roman',12,'bold'),fg='black')
text1.place(relx=0.5,rely=0.5,anchor=CENTER)

b=Button(f2,text='text',padx=10,pady=10,bg='sky blue')
b.pack()
b.bind('<Button-1>',func)
b.bind('<Button-3>',reset)

b1=Button(f2,text='delete frame',padx=5,pady=5)
b1.pack()
b1.bind('<Button-1>',delete)
root.mainloop()
