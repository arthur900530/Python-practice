from tkinter import *
from random import *
import time

class Ball:
    def __init__(self, canvas, color, w, h, racket):
        self.canvas = canvas
        self.racket = racket
        self.id = canvas.create_oval(0,0,20,20,fill=color)
        self.canvas.move(self.id,w/2,h/2)
        startPos = [-20, -15, -10, -5, 5, 10, 15, 20]
        shuffle(startPos)
        self.x = startPos[0]
        self.y = -step
        self.notTouchBound = True
    def move(self):
        position = self.canvas.coords(self.id)
        if position[0] <= 0:
            self.x = step
        if position[2] >= w:
            self.x = -step
        if position[1] <= 0:
            self.y = step
        if position[3] >= h:
            self.y = -step
        if self.hitRacket(position):
            self.y = -step
        if position[3] >= h:
            self.notTouchBound = False

        self.canvas.move(self.id, self.x, self.y)

    def hitRacket(self,position):
        rPos = self.canvas.coords(self.racket.id)
        if position[2] >= rPos[0] and position[0] <= rPos[2]:
            if position[3] >= rPos[1] and position[3] <= rPos[3]:
                return True
            return False

class Racket:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,15,fill = color)
        self.canvas.move(self.id, 270, 400)
        self.x = 0
        self.canvas.bind_all('<KeyPress-Right>',self.moveRight)
        self.canvas.bind_all('<KeyPress-Left>', self.moveLeft)

    def moveLeft(self,event):
        self.x = -20
    def moveRight(self,event):
        self.x = 20;
    def racketMove(self):
        self.canvas.move(self.id,self.x,0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= w:
            self.x = 0

w = 640
h = 480
step = 15
speed = 0.015

tk = Tk()
tk.title('Bouncing Ball')
tk.wm_attributes('-topmost',1)
canvas = Canvas(tk, width = w, height = h)
canvas.pack()
# tk.update()

racket = Racket(canvas, 'purple')
ball = Ball(canvas, 'yellow', w, h, racket)

while ball.notTouchBound:
    try:
        ball.move()
    except:
        break
    racket.racketMove()
    tk.update()
    time.sleep(speed)
print('You Lose')
