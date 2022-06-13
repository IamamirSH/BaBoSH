import turtle
import time
import random

delay = 0.1
score = 0

# firt setting
win = turtle.Screen()
win.title("ShiShi's game")
win.bgcolor('green')
win.setup(width=600, height=600)
win.tracer(0)

# snake head
head = turtle.Turtle()
head.speed(0)
head.shape('square')
head.color('white')
head.penup()
head.goto(0, 0)
head.direction = 'stop'

# food
food = turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('red')
food.penup()
food.goto(0, 100)

# segments
segments = []

# functions
def goup():
    head.direction = 'up'

def godown():
    head.direction = 'down'

def goright():
    head.direction = 'right'

def goleft():
    head.direction = 'left'

def move():
    if head.direction == 'up':
        y = head.ycor()
        head.sety(y+20)

    if head.direction == 'down':
        y = head.ycor()
        head.sety(y-20)

    if head.direction == 'right':
        x = head.xcor()
        head.setx(x+20)

    if head.direction == 'left':
        x = head.xcor()
        head.setx(x-20)

# bindings
win.listen()
win.onkeypress(goup, 'w')
win.onkeypress(godown, 's')
win.onkeypress(goright, 'd')
win.onkeypress(goleft, 'a')

while True:
    win.update()

    # wall happend
    if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
        time.sleep(1)
        print('GameOver')
        head.goto(0,0)
        head.direction = 'stop'

        # hide segments
        for segment in segments:
            segment.goto(1000, 1000)

        # clear segments
        segments.clear()
        score = 0
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

    # eat happend
    if head.distance(food) < 20:
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x, y)

        # add segments
        newsegment = turtle.Turtle()
        newsegment.speed(0)
        newsegment.shape('square')
        newsegment.color('black')
        newsegment.penup()
        segments.append(newsegment)
        score = score + 1
        print(score)
    # move segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # move 0 segment
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()
    time.sleep(delay)

win.mainloop()