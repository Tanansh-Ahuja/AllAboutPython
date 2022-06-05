from PIL import Image, ImageFilter

img = Image.open("./pikachu.jpg")
#img.show()
fimg = img.convert('L')
rimg=fimg.resize((300,300))
rimg.save('resized.png','png')