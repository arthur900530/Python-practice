from random import randint
from tkinter import *
import time
from PIL import Image, ImageTk
import math

# tk = Tk()
# canvas = Canvas(tk, width=640, height=480)
# canvas.pack()
# x_center, y_center, r = 320, 240, 100
# x,y = [],[]
#
# for i in range(12):
#     x.append(x_center+r*math.cos(30*i*math.pi/180))
#     y.append(y_center+r*math.sin(30*i*math.pi/180))
# for i in range(12):
#     for j in range(12):
#         canvas.create_line(x[i],y[i],x[j],y[j],width=3,fill='blue')
# # for i in range(11):
# #     canvas.create_line(x[i],y[i],x[i+1],y[i+1])
# # canvas.create_line(x[11],y[11],x[0],y[0])
#
# canvas.create_line(30,400,580,400,width=20,stipple='hourglass')
# help(canvas.create_line)
# tk.mainloop()

# tk = Tk()
# tk.title('Octogon')
# tk.geometry('1000x1000')
#
# canvas = Canvas(tk, width = 800, height = 800, bg = 'lightgrey')
# canvas.pack()
# canvas.create_polygon(
#     350,350-50*math.sqrt(2),
#     450,350-50*math.sqrt(2),
#     450+50*math.sqrt(2),350,
#     450+50*math.sqrt(2),450,
#     450,450+50*math.sqrt(2),
#     350,450+50*math.sqrt(2),
#     350-50*math.sqrt(2),450,
#     350-50*math.sqrt(2),350,
#     width=10,
#     fill='#d30909',
#     outline='black'
# )
# canvas.create_text(400,400,text='UFC',font=('',33,'bold'))
# # canvas.create_line(400,400,350,350-50*math.sqrt(2))
# img = Image.open('tony.png')
# img = img.resize((200,200))
#
# tony = ImageTk.PhotoImage(img)
# canvas.create_image(700,700,image=tony)
#
# tk.mainloop()

# tk = Tk()
# canvas = Canvas(tk, width = 500, height = 500)
# canvas.pack()
# yb = canvas.create_oval(10, 50, 60, 100,fill='yellow',outline='lightgray')
# aqb = canvas.create_oval(10, 350, 60, 400,fill='aqua',outline='lightgray')
# # for x in range(0,80):
# #     canvas.move(yb, 2, 6)
# #     canvas.move(aqb, 2, -5)
# #     tk.update()
# #     # canvas.after(50)
# #     time.sleep(0.05)
#
# for x in range(500):
#     if randint(1,100)>30:
#         canvas.move(yb,2,0)
#     else:
#         canvas.move(aqb,2,0)
#     tk.update()
#     time.sleep(0.001)
#
# tk.mainloop()

def ballMove(event):
    if event.keysym == 'Left':
        canvas.move(rb,-20,0)
    if event.keysym == 'Right':
        canvas.move(rb, 20,0)
    if event.keysym == 'Up':
        canvas.move(rb, 0,-20)
    if event.keysym == 'Down':
        canvas.move(rb,0,20)

tk = Tk()
canvas = Canvas(tk, width = 500, height = 500)
canvas.pack()
rb = canvas.create_oval(225,225,275,275,fill='red')
canvas.bind_all('<KeyPress-Left>',ballMove)
canvas.bind_all('<KeyPress-Right>',ballMove)
canvas.bind_all('<KeyPress-Up>',ballMove)
canvas.bind_all('<KeyPress-Down>',ballMove)

tk.mainloop()