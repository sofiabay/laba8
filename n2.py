from PIL import Image

alp = {'1': 'static/НГ.jpg',
       '2': 'static/23.jpg',
       '3': 'static/8.jpg'}

n = input("\n\n1. новый год\n2. 23 февраля\n3. 8 марта\n\nВведите номер нужного праздника: ")

if n in alp:
    href = alp[n]
    img = Image.open(href)
    img.show()