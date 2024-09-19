import sys
import os
from PIL import Image

# grab the first and second argument
image_folder = sys.argv[1]
output_folder = sys.argv[2]


#check if new exists, if not, create it.
if not os.path.exists(output_folder):
	os.makedirs(output_folder)

for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    #added the / in case user doesn't enter it. You may want to check for this and add or remover it. 
    img.save(f'{output_folder}/{clean_name}.png', 'png')
    print('all done!')

#loop through Pokedex, 
#convert images to PNG
#save to new folder