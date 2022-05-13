"""
Author 1: Rodrigo García
Author 2: Misael Chávez
"""
from ast import Break
from random import *
from turtle import *

from freegames import path


car = path('car.gif')
#lista de simbolos de la nueva lista en vez de numeros.
tiles = ["☺", '☻','♥','♦','♣','♠','•','○','◙','♂','♀','♪','♫','☼','►','◄','↕','‼','¶','§','@','↨','↑','↓','→','←','∟','↔','▲','▼','©']*2
Taps = {'taps': 0}
state = {'mark': None}
hide = [True] * 64
#Variables para las funciones futuras.
writer = Turtle(visible=True)
finish = Turtle(visible=True)
GameOver = {'YouWin' : 0, 'Message': 'YOU WIN', 'stop': 'YOU LOSE'}



def square(x, y):
    """Draw white square with black outline at (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convert (x, y) coordinates to tiles index."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convert tiles count to (x, y) coordinates."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


def tap(x, y):
    """Update mark and hidden tiles based on tap."""
    spot = index(x, y)
    mark = state['mark']
    

    writer.undo()
    writer.write(Taps['taps'])
    
    #Se tiene el contador de "taps" para detectar cuantas veces a presionado el mouse, y se mostrara el contador.
    #Se tiene la funcion de GameOver para cuando no se completo antes de los 128 taps. (Se puede quitar o modificar el limite)
    if Taps['taps'] == 128:
        finish.goto(0, 210)
        finish.color("black")
        finish.undo()
        finish.write(GameOver['stop'], font=('Arial', 55, 'normal'))
        Break
    elif mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
        Taps['taps'] += 1
        writer.goto(220, 170)
        writer.color('black')
        writer.write(Taps['taps'], font=('Arial', 30, 'normal'))
    else:
        GameOver['YouWin'] += 1         
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        Taps['taps'] += 1
        writer.goto(220, 170)
        writer.color('black')
        writer.write(Taps['taps'], font=('Arial', 30, 'normal'))

    
    #Tras tener las 64 casillas liberadas se soltara el mensaje
    if GameOver['YouWin'] == 32:
        finish.goto(0, 210)
        finish.color("black")
        finish.undo()
        finish.write(GameOver['Message'], font=('Arial', 55, 'normal'))


def draw():
    """Draw image and tiles."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        #Se cambio la posicion en X para que estubieran lo más centrado posibles.
        goto(x+10, y)
        color('black')
        write(tiles[mark],font=('Arial', 30, 'normal'))

    
    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
