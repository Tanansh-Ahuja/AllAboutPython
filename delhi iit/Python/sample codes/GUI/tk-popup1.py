import Tkinter
import tkMessageBox

top = Tkinter.Tk()
top.title("Hello")
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello World")

B1 = Tkinter.Button(top, text = "Say Hello", command = hello)
B1.pack()

top.mainloop()
