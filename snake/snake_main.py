from sense_hat import SenseHat
from time import sleep

import snake.variables as v
import snake.colors as c
import snake.functions as f

sense = SenseHat()

## MAIN

sense.clear()
f.draw_slug()
sense.stick.direction_any = f.joystick_moved
while v.dead == False:
	f.move()
	sleep(v.pause)
	if len(v.vegetables) < 4 and randint(1,5) > 4:
	  f.make_veg()

#picture = sense.get_pixels
#i = 0
#while i < 3:
#  sense.clear()
#  sleep(0.3)
#  sense.set_pixels(picture) #AQUI HAY UN ERROR, pendiente revisar
#  sleep(0.3)
#  i =+ 1
msg = "Game Over... your score is: " + str(v.score)
sense.show_message(msg,scroll_speed=0.07)
