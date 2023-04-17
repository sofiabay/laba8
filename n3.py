from PIL import Image, ImageDraw, ImageFont

alp = {'1': 'static/НГ.jpg',
       '2': 'static/23.jpg',
       '3': 'static/8.jpg'}

n = input("\n\n1. новый год\n2. 23 февраля\n3. 8 марта\n\nВведите номер нужного праздника: ")

if n in alp:
    href = alp[n]
    img = Image.open(href)
    #img.show()

name = input("\nНапишите имя, кого бы вы хотели поздравить: ")

draw_text = ImageDraw.Draw(img)
font = ImageFont.truetype("arial.ttf", 30)
draw_text.text(
    (100,10),
    name+', Поздравляю!!!',
    font=font,
    fill=('red'),
    stroke_width=1,
    stroke_fill="red" )
img.show()
img.save('Поздравляю.png', quality=95)