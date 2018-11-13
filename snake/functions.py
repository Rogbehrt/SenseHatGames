from sense_hat import SenseHat
from random import randint

import variables as v
import colors as c

sense = SenseHat()

def draw_slug():
  for segment in v.slug:
		sense.set_pixel(segment[0],segment[1],c.white)

def draw_veg():
  for veg in v.vegetables:
    sense.set_pixel(veg[0],veg[1],c.green)

def move():
  global score
  global pause
  global dead
  remove = True
  # Busca el primer y el último item de la lista (slug)
  last = v.slug[-1]
  first = v.slug[0]
  head = list(last) # Crea una copia del último item

  if v.direction == "right": # Busca el siguiente pixel en la direccion que se esta moviendo el slug
    if last[0] + 1 == 8: # Se mueve a través de la columna
    	head[0] = 0
    else:
    	head[0] = last[0] + 1

  if v.direction == "left":
    if last[0] - 1 == -1:
    	head[0] = 7
    else:
    	head[0] = last[0] - 1

  if v.direction == "down":
    if last[1] + 1 == 8:
    	head[1] = 0
    else:
    	head[1] = last[1] + 1

  if v.direction == "up":
    if last[1] - 1 == -1:
    	head[1] = 7
    else:
    	head[1] = last[1] - 1

  if head in v.slug:
    v.dead = True

  v.slug.append(head) # Agrega este pixel al final de la lista
  sense.set_pixel(head[0], head[1], c.blue) # Pone el nuevo pixel del mismo color que los demas
  body = []
  for segment in v.slug:
    body.append(segment)
  if head in body:
    body.remove(head)
  for segment in body:
		sense.set_pixel(segment[0],segment[1],c.white)

  if head in v.vegetables:
    v.vegetables.remove(head)
    v.score += 1
    if v.score % 5 == 0:
      remove = False
      v.pause = v.pause * 0.8

  if remove:
    sense.set_pixel(first[0], first[1], c.blank) # Pone el primer pixel de la lista en blanco
    v.slug.remove(first) # Elimina el primer pixel de la lista

def joystick_moved(event):
  global direction
  v.direction = event.direction

def make_veg():
  new = v.slug[0]
  while new in v.slug:
    x = randint(0,7)
    y = randint(0,7)
    new = [x,y]
  v.vegetables.append(new)
  draw_veg()
