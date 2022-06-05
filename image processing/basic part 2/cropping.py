from PIL import Image, ImageFilter

img = Image.open("./pikachu.jpg")
#img.show()
fimg = img.convert('L')
box=(100,100,400,400)
region = fimg.crop(box)
region.save('cropped.png','png')