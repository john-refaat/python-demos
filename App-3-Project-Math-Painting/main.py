from PIL import Image
import numpy as np
from random import randint

class Canvas:
    def __init__(self, width, height, color):
        self.width = width
        self.height = height
        self.color = color
        self.data = np.zeros((self.height, self.width, 3), dtype=np.uint8)
        self.data[:] = self.color

    def make(self, image_path):
        img = Image.fromarray(self.data, 'RGB')
        img.save(image_path)

class Rectangle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.height, self.y:self.y + self.width] = self.color

class Square:
    def __init__(self, x, y, side, color):
        self.x = x
        self.y = y
        self.side = side
        self.color = color

    def draw(self, canvas):
        canvas.data[self.x:self.x + self.side, self.y:self.y + self.side] = self.color


def randomRectangle(width, height):
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    w = randint(10, width//2)
    h = randint(10, height//2)
    x = randint(0, height - h)
    y = randint(0, width - w)
    rectangle = Rectangle(x, y, w, h, color)
    rectangle.draw(canvas)

def randomSquare(canvas_width, canvas_height):
    color = (randint(0, 255), randint(0, 255), randint(0, 255))
    side = randint(10, min(canvas_width, canvas_height) // 2)
    x = randint(0, canvas_width - side)
    y = randint(0, canvas_height - side)
    square = Square(x, y, side, color)
    square.draw(canvas)

width =  600
height = 400
bg_color = (255, 255, 255)
canvas = Canvas(width, height, bg_color)

for _ in range(3):
    randomRectangle(width=width, height=height)
    randomSquare(canvas_width= width, canvas_height=height)

canvas.make('canvas.png')
