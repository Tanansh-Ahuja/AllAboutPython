from PIL import Image, ImageFilter

img = Image.open('./astro.jpg')
#nimg = img.resize((400,200))
#nimg.save('thumbnail.jpg')

img.thumbnail((400,400))
img.save('thumbnail.png')