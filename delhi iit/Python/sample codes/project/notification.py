import Tkinter
import tkMessageBox

top = Tkinter.Tk()
top.title("Hello")
def hello():
   tkMessageBox.showinfo("Say Hello", "Hello World")


hello()
top.mainloop()
