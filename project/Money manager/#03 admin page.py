from tkinter import *




root=Tk()
root.geometry('1350x700+0+0')
root.title('Admin')

f0=Frame(root,bg='black')
f0.pack(fill=BOTH,expand=True)
f1=Frame(f0,bg='sky blue',padx=10)
f1.pack(side=TOP,fill=X,padx=10,pady=5)
f2=Frame(f0,bg='red',padx=5,pady=5)
f2.pack(side=TOP,fill=BOTH,padx=2,pady=2,expand=1)
f3=Frame(f2,bg='yellow',padx=5,pady=5)
f3.pack(side=LEFT,fill=BOTH,expand=True,padx=2)
f4=Frame(f2,bg='sky blue',padx=5,pady=5)
f4.pack(side=LEFT,fill=BOTH,expand=True,padx=2)

l1=Label(f1,text='Hey!! Welcome back Tanansh. What are you planning to do today?',
         font=('Times new Roman',30,'bold'),bg='sky blue')
l1.pack(side=TOP, fill=X)






root.mainloop()



