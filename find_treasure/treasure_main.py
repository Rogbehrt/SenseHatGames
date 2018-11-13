from sense_hat import *
from time import sleep as sp
from random import randint

import colors as c
import treasure_main.functions as f

s = SenseHat()
s.clear()

score = 0

for turnos in range(10):
    cx = randint(0,7) #cx = coin x
    cy = randint(0,7) #cy = coin y

    s.set_pixel(cx,cy,yellow)
    sp(1.5)
    s.clear()

    x = randint(0,7)
    y = randint(0,7)

    s.set_pixel(x,y,white)

    while True:
        e = f.move()
        if e.direction == DIRECTION_MIDDLE:
            if x == cx and y == cy:
                s.set_pixel(x,y,green)
                score =+ 1
            else:
                s.set_pixel(x,y,red)
            sp(1)
            s.clear()
            break;
        s.clear()
        if e.direction == DIRECTION_UP and y > 0:
            y = y - 1
        elif e.direction == DIRECTION_DOWN and y < 7:
            y = y + 1
        elif e.direction == DIRECTION.LEFT and x > 0:
            x = x - 1
        elif e.direction == DIRECTION.RIGHT and x < 7:
            x = x + 1
        s.set_pixel(x,y,white)

s.show_message("Score: "+str(score))
