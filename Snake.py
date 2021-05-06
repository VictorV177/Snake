
"""
Juego de Snake
Autor: Rafael Valenzuela Zurita, Victor Velazquez
"""
from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

"snake"
head = turtle.Turtle()
head.shape("square")
color = random.choice(['yellow', 'green', 'black'])
head.penup()
head.goto(0, 0)
head.direction = "Stop"

"Food color"
food = turtle.Turtle()
colors = random.choice(['blue', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)
    
def change(x, y):
    """ Cambia la dirección de la serpiente """
    aim.x = x
    aim.y = y


def inside(head):
    """ Detecta si la sepriente esta dentro de la ventana """
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    """ Mueve a la serpiente un lugar
        Comprueba que este dentro del tablero
        Incrementa su tamaño cuando es necesario
        Mueve la comida un paso a la vez sin salir de la ventana
    """
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return
    
    if not inside(food):
        food.x = 0
        food.y = 0

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)
        food.move(randrange(-1,2)*10)

    clear()

    for body in snake:
        square(body.x, body.y, 9, 'black')

    square(food.x, food.y, 9, 'green')
    update()
    ontimer(move, 100)

setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()

