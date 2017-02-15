from display import *
from draw import *
import random

screen = new_screen()
color = [ 0, 255, 0 ]

draw_line(screen,0,0,500,500,color)

for n in range(50):
    color = [ random.randint(0,256), random.randint(0,256), random.randint(0,256) ]
    draw_line(screen,250,250,500,500-n*10,color)

for n in range(50):
    color = [ random.randint(0,256), random.randint(0,256), random.randint(0,256) ]
    draw_line(screen,250,250,500-n*10,500,color)

for n in range(50):
    color = [ random.randint(0,256), random.randint(0,256), random.randint(0,256) ]
    draw_line(screen,250,250,500-n*10,0,color)

for n in range(50):
    color = [ random.randint(0,256), random.randint(0,256), random.randint(0,256) ]
    draw_line(screen,250,250,0,500-n*10,color)

'''
for n in range(50):
    color = [ random.randint(0,256), random.randint(0,256), random.randint(0,256) ]
    draw_line(screen,0,n*10,500-n*10,500,color)
'''

display(screen)
save_extension(screen, 'img.png')
