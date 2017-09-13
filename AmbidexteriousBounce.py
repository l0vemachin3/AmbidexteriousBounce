from tkinter import *
import random
import time

class Ball:
    def __init__(self, canvas, paddle, paddle2, color):
         self.canvas = canvas
         self.paddle = paddle
         self.paddle2 = paddle2
         self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
         self.canvas.move(self.id, 245, 100)
         starts = [-3, -2, -1, 1, 2, 3]
         random.shuffle(starts)
         self.x = starts[0]
         self.y = -3
         self.canvas_height = self.canvas.winfo_height()
         self.canvas_width = self.canvas.winfo_width()
         self.hit_bottom = False

    def draw(self):        
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if self.hit_paddle2(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def hit_paddle2(self, pos):
        paddle2_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle2_pos[0] and pos[0] <= paddle2_pos[2]:
            if pos[3] >= paddle2_pos[1] and pos[3] <= paddle2_pos[3]:
                return True
            return False
         
class Ball2:
    def __init__(self, canvas, paddle, paddle2, color):
         self.canvas = canvas
         self.paddle = paddle
         self.paddle2 = paddle2
         self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
         self.canvas.move(self.id, 245, 100)
         starts = [-3, -2, -1, 1, 2, 3]
         random.shuffle(starts)
         self.x = starts[0]
         self.y = -3
         self.canvas_height = self.canvas.winfo_height()
         self.canvas_width = self.canvas.winfo_width()
         self.hit_bottom = False         

    def draw(self):        
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        if self.hit_paddle(pos) == True:
            self.y = -3
        if self.hit_paddle2(pos) == True:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
            return False

    def hit_paddle2(self, pos):
        paddle2_pos = self.canvas.coords(self.paddle2.id)
        if pos[2] >= paddle2_pos[0] and pos[0] <= paddle2_pos[2]:
            if pos[3] >= paddle2_pos[1] and pos[3] <= paddle2_pos[3]:
                return True
            return False

class Paddle:
    def __init__(self, canvas, color):
      self.canvas = canvas
      self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
      self.canvas.move(self.id, 200, 300)
      self.x = 0
      self.canvas_width = self.canvas.winfo_width()
      self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
      self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
      self.canvas.bind_all('<KeyPress-Button_1>')
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

class Paddle2:
    def __init__(self, canvas, color):
      self.canvas = canvas
      self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
      self.canvas.move(self.id, 200, 300)
      self.x = 0
      self.canvas_width = self.canvas.winfo_width()
      self.canvas.bind_all('<KeyPress-a>', self.turn_left)
      self.canvas.bind_all('<KeyPress-d>', self.turn_right)

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2
        
tk = Tk()
tk.title("Ambidexterious Bounce")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)
canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

paddle2 = Paddle2(canvas, 'blue')
paddle = Paddle(canvas, 'red')
ball2 = Ball2(canvas, paddle, paddle2, 'yellow')
ball = Ball(canvas, paddle, paddle2, 'green')

while 1:
    if ball.hit_bottom == False:
        if ball2.hit_bottom == False:
            ball2.draw()
            ball.draw()
            paddle.draw()
            paddle2.draw()
            tk.update_idletasks()
            tk.update()
            time.sleep(0.01)
