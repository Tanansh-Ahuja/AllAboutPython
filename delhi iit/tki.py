import tkinter

root=tkinter.Tk()
s=tkinter.Scrollbar(root)
T=tkinter.Text(root)
T.focus_set()
s.pack(side=tkinter.RIGHT, fill=tkinter.Y)
T.pack(side=tkinter.LEFT, fill=tkinter.Y)
s.config(command=T.yview)
T.config(yscrollcommand=s.set)
top = tkinter.Tk()
for i in range(40):
    T.insert(tkinter.END, "This is line %d\n" % i)
    T.yview(tkinter.MOVETO,1.0)


top.mainloop()
    
