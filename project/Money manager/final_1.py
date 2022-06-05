from tkinter import *
from playsound import playsound
from time import *

class creation:

    def __init__(slfc,rootarg):
        slfc.root=rootarg

    def des_first_page(slfc):
        playsound('money manager.mp3')
        slfc.frootfirst_page .destroy()
        slfc.login_signup()

    def first_page(slfc):
        i=0
        while i<=1:
            root.attributes('-alpha',i)
            root.update()
            sleep(0.05)
            i=i+0.02

        slfc.frootfirst_page=Frame(root,bg='black')
        slfc.frootfirst_page.pack(fill=BOTH,expand=True)
        f1=Frame(slfc.frootfirst_page,padx=5,pady=5)
        f1.pack(anchor=NE)
        l1=Label(slfc.frootfirst_page,text='Created By\nTanansh Ahuja',bg='black',fg='yellow',font=('Times New Roman',15,'bold'))
        l1.pack(anchor='ne')
        l2=Label(slfc.frootfirst_page,text='Welcome\nTo\nThe Money Manager',bg='black',fg='#FF3636',font=('Jester',30,'bold'))
        l2.place(relx=0.5,rely=0.5,anchor=CENTER)
        l2.after(500,slfc.des_first_page)
        root.mainloop()

    def login_signup(slfc):

        slfc.froot_login_signup=Frame(root,bg='white')
        slfc.froot_login_signup.pack(fill=BOTH,expand=True)

        f1=Frame(slfc.froot_login_signup,bg='sky blue',padx=10)
        f1.pack(side=TOP,fill=X,padx=2,pady=2)
        f2=Frame(slfc.froot_login_signup,bg='red')
        f2.pack(side=TOP,fill=BOTH,padx=2,pady=2,expand=1)
        f3=Frame(f2,bg='white',padx=5,pady=5)
        f3.pack(side=LEFT,fill=BOTH,expand=True)
        f4=Frame(f2,bg='grey',padx=5,pady=5)
        f4.pack(side=LEFT,fill=BOTH,expand=True)
        login_name=StringVar()
        login_name.set('')
        login_password=StringVar()
        login_password.set('')
        l1=Label(f1,bg='blue',text='Money Manager',fg='white',padx=10,pady=5,relief=RAISED,borderwidth=5,font=('Algerian',20,'underline'))
        l1.pack(side=LEFT)
        f5=Frame(f1,bg='sky blue',padx=2,pady=20)
        f5.pack(anchor=E,fill=BOTH,expand=1)
        b1=Button(f5,text='Log In',fg='white',bg='light green',padx=3,pady=2,font=('Calibri',15,'bold'))
        b1.pack(side=RIGHT, padx=15)
        e2=Entry(f5,textvariable=login_password,width=20,show='*',font=('times new roman',15,'bold'))
        e2.pack(side=RIGHT)
        l3=Label(f5,text='Password: ',font=('arial black',10),bg='sky blue',padx=10)
        l3.pack(side=RIGHT)
        e1=Entry(f5,textvariable=login_name,width=10,font=('times new roman',15,'bold'))
        e1.pack(side=RIGHT)
        l2=Label(f5,text='Enroll: ',font=('arial black',10),bg='sky blue',padx=10)
        l2.pack(side=RIGHT)
        root.mainloop()

#main
root=Tk()
root.geometry('1350x700+0+0')
root.title('The Money Manager')
obj=creation(root)
obj.first_page()

