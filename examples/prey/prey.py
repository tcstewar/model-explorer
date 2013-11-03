x0 = 1.0
y0 = 0.1
b = 1.0
p = 1.0
r = 1.0
d = 1.0
T = 30
dt = 0.01
noise = 0.1

import modex
log = modex.log()


import random

t=0
x=x0
y=y0
while t<T:
    f = b - p*y + random.gauss(0, noise)
    g = r*x - d + random.gauss(0, noise)
    x += x*f*dt
    y += y*g*dt
    if x<0: x = 0
    if y<0: y = 0
    
    t+=dt

    log.time = t
    log.x = x
    log.y = y
    
