from tkinter import *

root = Tk()

root.geometry("800x600")
root.title("My first GUI")
a="Hello world\n  kaise ho"

tl=Label(text=a,bg="red",fg="white",padx=100,pady=100,font=("times new roman",19,"underline","bold"),borderwidth=50)
#font="times new roman 19 bold"
tl.pack(anchor="se",side=BOTTOM,padx=10,pady=10,fill=X)



root.mainloop()
