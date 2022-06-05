from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')
f_img = img.filter(ImageFilter.BLUR)
f_img.save("blur.png",'png')