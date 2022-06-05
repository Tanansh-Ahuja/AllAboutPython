from tkinter import *

def click(event):
    #print(event)
    #print(event.widget)
    #print(event.widget.cget('text'))

    global scvalue
    value=0
    text=event.widget.cget('text')

    if text == '=':

        if scvalue.get().isdigit():
            value=int(scvalue().get())

        else:

            try:
                value=eval(screen.get())
                scvalue.set(value)
                screen.update()

            except Exception as e:
                print(e)
                scvalue.set('ERROR!!')
                screen.update()

        


    elif text == 'C':
        scvalue.set("")
        value=0
        screen.update()


    else:
        #print('old scvalue: ',scvalue.get())
        #print('text: ',text)
        #print('new scvalue: ',scvalue.get()+text)
        #print('\n')
        scvalue.set(scvalue.get()+text)
        screen.update()
    


#main
root=Tk()

root.geometry("700x700")
root.title("Calculator")
#root.wm_iconbitmap("C:\\Users\\com\\Desktop\\download.png")
scvalue=StringVar()
#scvalue=''
scvalue.set("")

screen=Entry(root,textvariable=scvalue,font=('times new roman', 20 ,'bold'))
screen.pack(fill=X,padx=10,pady=10,ipady=5)

framex=Frame(root,bg="orange",padx=6,pady=20,relief=GROOVE,borderwidth=8)
framex.pack(fill=X)

frame1=Frame(framex,bg='red',padx=10,pady=10,relief=RIDGE,borderwidth=5)
frame1.pack(side=LEFT,expand=1)

frame2=Frame(framex,bg='yellow',padx=10,pady=10,relief=SUNKEN,borderwidth=5)
frame2.pack(side=LEFT,expand=1)


f=Frame(frame1,bg="pink")

b=Button(f,text="9",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text="8",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text="7",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)
f.pack()

f=Frame(frame1,bg="white")
b=Button(f,text="6",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text="5",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text="4",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)
f.pack()

f=Frame(frame1,bg="black")
b=Button(f,text="3",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text="2",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text="1",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)
f.pack()

f=Frame(frame1,bg="grey")
b=Button(f,text="0",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text="C",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text=".",padx=29,pady=25,font=('times new roman', 10 ,'bold'))
b.pack(side=LEFT,padx=5,pady=5)
b.bind('<Button-1>',click)
f.pack()

f=Frame(frame2,bg="grey")
b=Button(f,text="+",padx=28,pady=75,font=('times new roman', 10 ,'bold'))
b.grid(row=0,column=0,padx=5,pady=5,rowspan=2)
b.bind('<Button-1>',click)
b=Button(f,text="-",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.grid(row=2,column=0,padx=5,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text="*",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.grid(row=3,column=0,padx=5,pady=5)
b.bind('<Button-1>',click)

b=Button(f,text="/",padx=28,pady=25,font=('times new roman', 10 ,'bold'))
b.grid(row=0,column=1,padx=5,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text="%",padx=25,pady=25,font=('times new roman', 10 ,'bold'))
b.grid(row=1,column=1,padx=5,pady=5)
b.bind('<Button-1>',click)
b=Button(f,text="=",padx=28,pady=75,font=('times new roman', 10 ,'bold'))
b.grid(row=2,column=1,padx=5,pady=5,rowspan=2)
b.bind('<Button-1>',click)
f.pack(side=LEFT)
#print('before loop')
root.mainloop()
#print('sfter loop')
