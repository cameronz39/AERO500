from vpython import *

# floor = box(pos=vector(0,0,0), length = 4, height = 0.5, width = 4)
# floor.color = color.blue

# ball = sphere(pos=vector(0,4,0), radius = 1, color=color.red)
# ball.velocity = vector(0,1,0)
# dt = 0.01

# while(1):
#     rate(100)
#     ball.pos = ball.pos + ball.velocity*dt
#     if ball.pos.y < ball.radius:
#         ball.velocity.y = abs(ball.velocity.y)
#     else:
#         ball.velocity.y = ball.velocity.y - 9.8*dt

sun = sphere(pos=vector(0,0,0), radius = 0.1, color=color.yellow)

earth = sphere(pos=vector(1,0,0), radius = 0.1, color=color.blue)
earth.velocity = vector(0,1,0)

dt = 0.01

while(1):
    rate(100)
    earth.pos = earth.pos + earth.velocity*dt
    accel = (sun.pos - earth.pos)*2
    earth.velocity = earth.velocity + accel