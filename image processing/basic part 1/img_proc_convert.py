from PIL import Image, ImageFilter

img = Image.open('./pikachu.jpg')
f_img=img.convert('L')
f_img.save('grey.png','png')