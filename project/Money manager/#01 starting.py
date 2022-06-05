from tkinter import *
import time
import playsound

def des():
    global f0
    #playsound.playsound('money manager.mp3')
    f0.destroy()
    


root=Tk()
root.geometry('1350x700+0+0')
root.title('The Money Manager')

i=0
while i<=1:
    root.attributes('-alpha',i)
    root.update()
    time.sleep(0.05)
    i=i+0.02

f0=Frame(root,bg='black')
f0.pack(fill=BOTH,expand=True)
f1=Frame(f0,padx=5,pady=5)
f1.pack(anchor=NE)
l1=Label(f0,text='Created By\nTanansh Ahuja',bg='black',fg='yellow',font=('Times New Roman',15,'bold'))
l1.pack(anchor='ne')
l2=Label(f0,text='Welcome\nTo\nThe Money Manager',bg='black',fg='#FF3636',font=('Jester',30,'bold'))
l2.place(relx=0.5,rely=0.5,anchor=CENTER)
#playsound.playsound('money manager.mp3')
root.after(1000,des)

root.mainloop()
