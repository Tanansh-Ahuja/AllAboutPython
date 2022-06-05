from Tkinter import *

root = Tk()
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill=Y )

E1=Entry(root, bd =1,yscrollcommand = scrollbar.set )

E1.pack(side = RIGHT,fill = BOTH )

scrollbar.config( command = E1.yview )

mainloop()
