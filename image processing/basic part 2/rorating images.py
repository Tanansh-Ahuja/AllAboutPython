from PIL import Image, ImageFilter

img = Image.open("./pikachu.jpg")
#img.show()
fimg = img.convert('L')
rimg=fimg.rotate(180)
rimg.save('upsidedownpickachu.png','png')
img2 = Image.open('./upsidedownpickachu.png')
img2.show()