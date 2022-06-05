from tkinter import *
from PIL import ImageTk, Image


def focusin(event):
    event.widget.delete(0,END)
    event.widget.config(fg='black')

def focusinpaswrd(event):
    event.widget.delete(0,END)
    event.widget.config(fg='black',show='*')

root=Tk()
root.geometry('1350x700+0+0')
root.title('The Money Manager')

# Making all the frames, atleast as much as possible
f1=Frame(root,bg='sky blue',padx=10)
f1.pack(side=TOP,fill=X,padx=2,pady=2)
f2=Frame(root,bg='red')
f2.pack(side=TOP,fill=BOTH,padx=2,pady=2,expand=1)
f3=Frame(f2,bg='#F5F5F5',padx=5,pady=5)
f3.pack(side=LEFT,fill=BOTH,expand=True)
f4=Frame(f2,bg='#F5F5F5',padx=5,pady=5)
f4.pack(side=LEFT,fill=BOTH,expand=True)

# Now we will make login frame

#variables defination
login_name=StringVar()
login_name.set('')
login_password=StringVar()
login_password.set('')

# Layout of login
l1=Label(f1,bg='blue',text='Money Manager',fg='white',padx=10,pady=5,relief=RAISED,borderwidth=5,font=('Algerian',20,'underline'))
l1.pack(side=LEFT)

f5=Frame(f1,bg='sky blue',padx=2,pady=20)
f5.pack(anchor=E,fill=BOTH,expand=1)

b1=Button(f5,text='Log In',fg='white',bg='blue',padx=3,pady=2,font=('Calibri',10,'bold'))
b1.pack(side=RIGHT, padx=15)

e2=Entry(f5,textvariable=login_password,width=20,fg='grey',font=('times new roman',15,'bold'))
e2.insert(0,'Password')
e2.pack(side=RIGHT,padx=10)
e2.bind('<FocusIn>',focusinpaswrd)

e1=Entry(f5,textvariable=login_name,width=20,fg='grey',font=('times new roman',15,'bold'))
e1.insert(0,'Enrollment No.')
e1.pack(side=RIGHT,padx=10)
e1.bind('<FocusIn>',focusin)

# Now we make signup page


#Variable definations
signup_name=StringVar()
signup_enroll=StringVar()
signup_mobile=StringVar()
signup_password=StringVar()
signup_cnfpassword=StringVar()
signup_name.set('')
signup_enroll.set('')
signup_mobile.set('')
signup_password.set('')
signup_cnfpassword.set('')

#layout
l4=Label(f4,text='New user,huh?',font=('Calibri',15,'bold'),bg='#F5F5F5')
l4.pack(side=TOP,padx=10,pady=20,anchor=W)
l5=Label(f4,text='Create a new Account',font=('Calibri',30,'bold'),bg='#F5F5F5')
l5.pack(side=TOP,padx=10,pady=1,anchor=W)


f6=Frame(f4,bg='#F5F5F5',padx=2,pady=20)
f6.place(relx=0.5,rely=0.5,anchor=CENTER)

f61=Frame(f6,bg='#F5F5F5',padx=5,pady=5)
f61.pack(side=TOP)

f611=Frame(f61,bg='#F5F5F5')
f611.pack(side=TOP,padx=20,pady=10)

e3=Entry(f611,textvariable=signup_name,width=12,fg='grey',font=('times new roman',25,'bold'))
e3.pack(side=LEFT,padx=25)
e3.insert(0,'Name')
e3.bind('<FocusIn>',focusin)

e4=Entry(f611,textvariable=signup_enroll,width=12,fg='grey',font=('times new roman',25,'bold'))
e4.pack(side=LEFT,padx=25)
e4.insert(0,'Enrollment no.')
e4.bind('<FocusIn>',focusin)

e5=Entry(f61,textvariable=signup_mobile,width=15,fg='grey',font=('times new roman',25,'bold'))
e5.pack(side=TOP,padx=20,pady=15)
e5.insert(0,'Mobile number')
e5.bind('<FocusIn>',focusin)

e6=Entry(f61,textvariable=signup_password,width=20,fg='grey',font=('times new roman',25,'bold'))
e6.pack(side=TOP,padx=20,pady=15)
e6.insert(0,'Password.')
e6.bind('<FocusIn>',focusinpaswrd)


e7=Entry(f61,textvariable=signup_cnfpassword,width=20,fg='grey',font=('times new roman',25,'bold'))
e7.pack(side=TOP,padx=20,pady=15)
e7.insert(0,'Confirm Password')
e7.bind('<FocusIn>',focusinpaswrd)

l6=Button(f4,text='Sign-up',font=('Calibri',20,'bold'),bg='green',fg='white',padx=10,pady=5)
l6.place(relx=0.5,rely=0.8,anchor=CENTER)

img=Image.open('money.gif')
imgq=ImageTk.PhotoImage(img)

l7=Label(f3,image=imgq)
l7.place(relx=0.5,rely=0.5,anchor=CENTER)

root.mainloop()
