from tkinter import *
from PIL import ImageTk, Image

root = Tk()

imgorg=Image.open("images.jpg")
img = ImageTk.PhotoImage(imgorg)

'''
imgresize=imgorg.resize((100,100))
img = ImageTk.PhotoImage(imgresize)
'''

'''
imgorg=Image.open("money.gif")
img = ImageTk.PhotoImage(imgorg)
'''

'''
Ab bhai dekho aisa hai ki python tkinter me tum gif add kar sakte ho but mehenat lagegi.
to panga ye hai ki gif ek baar me ek frame hi show karega.
to agar tumhe poora gif chahie to frame by frame photo lagani padegi aur after() function
ka istemal karna padega aur aise utni pics ka input dena padega jitne frames hai.
frame 10 bhi ho sakte hai aur 100 bhi.
so i dont thing its a good idea so i havent tried it yet.
but tumko karna hai to karo
'''

panel = Label(root, image = img,bg='red')
panel.pack(side = "bottom", fill = "both", expand = "yes")

root.mainloop()
