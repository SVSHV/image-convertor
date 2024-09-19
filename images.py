from PIL import Image, ImageFilter

img = Image.open('./rocks.jpg')

img.thumbnail((400, 400))
img.save('rock.jpg')
