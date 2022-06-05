from PIL import Image
import os

#convert images to jpeg
for filename in os.listdir('pokedex'):
    img = Image.open(f'pokedex\{filename}')
    cleanname = os.path.splitext(filename)
    img.save(f'new\{cleanname[0]}.png','png')
print('all done!')
#save to the new folder