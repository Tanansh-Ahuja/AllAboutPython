from PIL import Image, ImageFilter

img = Image.open("./pikachu.jpg")
#img.show()
#fimg = img.convert('L')
fimg=img.rotate(180)
fimg.save('aaaa.png','png')

