from display import *


def draw_line( screen, x0, y0, x1, y1, color ):
    dx = x1 - x0
    dy = y1 - y0

    if dx>=0 and dy>=0:
        if dx >= dy:
            octant1( screen, x0, y0, x1, y1, color )
        else:
            octant2( screen, x0, y0, x1, y1, color )

    if dx>=0 and dy<=0:
        if dx >= -1*dy:
            octant8( screen, x0, y0, x1, y1, color )
        else:
            octant7( screen, x0, y0, x1, y1, color )

    if dx<=0 and dy>=0:
        if -1*dx >= dy:
            octant8( screen, x1, y1, x0, y0, color )
        else:
            octant7( screen, x1, y1, x0, y0, color )
            
    if dx<=0 and dy<=0:
        if -1*dx >= -1*dy:
            octant1( screen, x1, y1, x0, y0, color )
        else:
            octant2( screen, x1, y1, x0, y0, color )

    '''
    A = y1 - y0
    B = x0 - x1
    x=x0
    y=y0
    d = 2*A + B
    while (x < x1):
        plot(screen,color,x,y)
        
        if(d > 1):
            y += 1
            d += 2*B
        x += 1
        d += 2*A
    plot(screen,color,x1,y1)
'''

def octant1( screen, x0, y0, x1, y1, color ):

    A = y1 - y0
    B = x0 - x1
    x=x0
    y=y0
    d = 2*A + B
    while (x < x1):
        plot(screen,color,x,y)
        
        if(d > 0):
            y += 1
            d += 2*B
        x += 1
        d += 2*A
    plot(screen,color,x1,y1)

def octant2( screen, x0, y0, x1, y1, color ):

    A = y1 - y0
    B = x0 - x1
    x=x0
    y=y0
    d = 2*B + A
    while (y < y1):
        plot(screen,color,x,y)
        
        if(d < 0):
            x += 1
            d += 2*A
        y += 1
        d += 2*B
    plot(screen,color,x1,y1)

def octant8(screen, x0, y0, x1, y1, color ):

    A = y1 - y0
    B = x0 - x1
    x=x0
    y=y0
    d = - 2*A + B
    while (x < x1):
        plot(screen,color,x,y)
        
        if(d < 0):
            y -= 1
            d -= 2*B
        x += 1
        d += 2*A
    plot(screen,color,x1,y1)

def octant7(screen, x0, y0, x1, y1, color ):

    A = y1 - y0
    B = x0 - x1
    x=x0
    y=y0
    d = A - 2*B
    while (y > y1):
        plot(screen,color,x,y)

        if(d > 0):
            x += 1
            d += 2*A
        y -= 1
        d -= 2*B
    plot(screen,color,x1,y1)
