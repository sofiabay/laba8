from PIL import Image

img = Image.open('static/image.jpg')

img_crop = img.crop((50, 75, 600, 250)) #обрезает картинку (x1,y1,x2,y2) x1,y1 - левый верхний угол, x2,y2 - правый нижний
img_crop.save('image_crop.jpg', quality=95)


img_crop.show()