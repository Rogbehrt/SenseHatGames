from sense_hat import *

s = SenseHat()

def move():
    while True:
        e = s.stick.move()
        if e.action != ACTION_RELEASED:
            return e
