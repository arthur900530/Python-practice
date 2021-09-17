from PIL import Image, ImageColor, ImageDraw

# r = Image.open('rushmore.jpg')
# print(type(r))
# w, h = r.size
# print(f'Name: {r.filename}')
# print(f'Filename extension: {r.format}')
# print(f'Description: {r.format_description}')
# print(f'Width: {w}')
# print(f'Height: {h}')
# r.show()
# r.save('out1.png')

# pic = Image.new('RGB', (300, 180), color='#FFEE88')
# pic.save('out2.jpg')

# r = Image.open('rushmore.jpg')
# r = r.rotate(45, expand = True)
# r.save('out4.jpg')

# i = Image.new('RGBA', (300, 100), 'Yellow')
# print(i.getpixel((150, 50)))
# i.save('out5.png')

# i = Image.new('RGBA', (300, 300), 'Yellow')
# for x in range(50, 251):
#     for y in range(50, 151):
#         i.putpixel((x, y), (0, 255, 255, 100))
# i.save('out6.png')
# for x in range(50, 251):
#     for y in range(151, 251):
#         i.putpixel((x, y), (0, 255, 255, 255))
# i.save('out7.png')

# p = Image.open('rushmore.jpg')
# cropp = p.crop((80, 30, 150, 100))
# # cropp.save('out8.jpg')
# copyp = p.copy()
# copyp.paste(cropp, (20, 20))
# copyp.paste(cropp, (20, 100))
# copyp.save('out9.jpg')

# image = Image.new('RGBA', (300, 300), 'Yellow')
# dobj = ImageDraw.Draw(image)
# for x in range(100, 200, 3):
#     for y in range(100, 200, 3):
#         dobj.point([(x, y)], fill='green')
# dobj.line([(0,0),(299,0),(299,299),(0,299),(0,0)], fill = 'Black')
# for x in range(150, 300, 10):
#     dobj.line([(x,0),(300,x-150)], fill='blue')
# for y in range(150, 300, 10):
#     dobj.line([(0,y),(y-150,300)], fill='blue')
# image.save('out10.png')

import qrcode

# img = qrcode.make('恭喜中獎')
# print(type(img))
# img.save('out11.jpg')

# qr = qrcode.QRCode(version=20,
#                    error_correction=qrcode.constants.ERROR_CORRECT_H,
#                    box_size=10,
#                    border=8
#                    )
# qr.add_data('https://www.facebook.com/profile.php?id=100006726992151')
# img = qr.make_image(fill_color='blue',back_color='white')
# img.save('out12.jpg')

# ch17_23_4.py

# vc_str = '''
# BEGIN:VCARD
# FN:錢雨杭
# TEL;CELL:0909756966
# ORG:政治大學
# TITLE:學生
# EMAIL:moneychien20639@gmail.com
# URL:https://www.facebook.com/profile.php?id=100006726992151
# ADR:台北市指南路
# END:VCARD
# '''
#
# img = qrcode.make(vc_str)
# img.save("VCARD.jpg")

# import pytesseract
# from PIL import Image
# pytesseract.pytesseract.tesseract_cmd = r'C:\Users\user\AppData\Local\Tesseract-OCR\tesseract.exe'
# text = pytesseract.image_to_string(Image.open('d:\\pycharm\\Ch17\\atq9305.jpg'))
# print(type(text), text)

from wordcloud import WordCloud
import jieba
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

# with open('text17_29.txt') as fp:
#     txt = fp.read()
# cut_text = ' '.join(jieba.cut(txt))         # 產生分詞的字串
# wd = WordCloud(                             # 建立詞雲物件
#     font_path="C:/Windows/Fonts\mingliu",
#     background_color="white",width=1000,height=880).generate(cut_text)
#
# imageCloud = wd.to_image()          # 由WordCloud物件建立詞雲影像檔
# imageCloud.show()                   # 顯示詞雲影像檔

with open('text17_29.txt') as fp:
    txt = fp.read()
ct = ''.join(jieba.cut(txt))
bg = np.array(Image.open('star.gif'))
wd = WordCloud(font_path='C:/Windows/Fonts\mingliu',
               background_color='white',
               mask=bg
               ).generate(ct)
print(type(wd))
plt.imshow(wd)
plt.axis('off')
plt.show()