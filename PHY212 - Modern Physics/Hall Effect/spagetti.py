from vpython import *
from IPython import display


scene = display(range=(20,20,20),width=1280,height=800)
scene.background = color.black

Delta_t = 0.02

t = 0

# Set up particle grid
size = 0.15
grid = []
vel0 = vector(0,0.65,0)
colour = (0.7,0.6,0.5)
rad = 0.2
spacing = 0.10
baseangle = 0.2

# Head
pos0 = vector(10,1.0,0)
grid.append(sphere(pos=pos0,radius=2.0*rad, vel=vel0, color=colour))

# Body
pos0 = vector(10,1.0,0)
colour = (0.2,0.4,0.7)
theta = 0.0
for i in range(0,21):
   offset = vector(spacing*i*math.sin(theta+baseangle),-spacing*i*math.cos(theta+baseangle),0)
   grid.append(sphere(pos=pos0+offset,radius=rad, vel=vel0, color=colour))

# Right Arm
colour = (0.2,0.8,0.9)
pos0 = vector(10,0.7,0)
theta = 0.7
for i in range(0,11):
   offset = vector(spacing*i*math.sin(theta+baseangle),
                   -spacing*i*math.cos(theta+baseangle),0)
   grid.append(sphere(pos=pos0+offset,radius=rad,
                   vel=vel0, color=colour))

# Left Arm
theta = -0.7
for i in range(0,11):
   offset = vector(spacing*i*math.sin(theta+baseangle),
                   -spacing*i*math.cos(theta+baseangle),0)
   grid.append(sphere(pos=pos0+offset,radius=rad,
                   vel=vel0, color=colour))

# Right Leg
colour = (0.2,0.2,0.7)
pos0 = vector(10,1.0,0)+2.0*vector(math.sin(baseangle),
                               -math.cos(baseangle),0)
theta = 0.4
for i in range(0,11):
   offset = vector(spacing*i*math.sin(theta+baseangle),
                   -spacing*i*math.cos(theta+baseangle),0)
   grid.append(sphere(pos=pos0+offset,radius=rad,
                   vel=vel0, color=colour))

# Left Leg
theta = -0.4
for i in range(0,11):
   offset = vector(spacing*i*math.sin(theta+baseangle),
                   -spacing*i*math.cos(theta+baseangle),0)
   grid.append(sphere(pos=pos0+offset,radius=rad,
                   vel=vel0, color=colour))



black_hole = sphere(pos = vector(-1,0,0), radius = 1.0, color=(0.3,0.3,0.3))

while 1:
   rate(100)
   t = t + Delta_t
   for thing in grid:
      thing.pos = thing.pos + thing.vel*Delta_t
      Agrav = - 15.0*norm(thing.pos-black_hole.pos)/(mag(thing.pos-
                                                           black_hole.pos)**2)
      thing.vel = thing.vel + Agrav*Delta_t
