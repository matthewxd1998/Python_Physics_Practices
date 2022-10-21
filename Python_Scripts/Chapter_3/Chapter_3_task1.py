from vpython import *

ball = sphere(pos=vector(0,0.1,0), radius=0.05, color=color.yellow, make_trail=True)
print(ball.pos)

ground = box(pos=vector(0,0,0), size=vector(5,0.02,0.25))

g = vector(0,-9.8,0)
ball.m = 0.05
v0 = 3.5
theta = 73*pi/180
ball.v = v0 * vector(cos(theta),sin(theta),0)
varrow = arrow(pos=ball.pos, axis=0.1 * ball.v, color=color.cyan)

t = 0
dt = 0.001

g1 = graph(xtitle='Time (s)', ytitle='Height (m)')
positon_plot = gcurve(color=color.blue)
positon_plot.plot(t, ball.pos.y)

while t < 1:
    rate(125)
    if ball.pos.y <= ground.pos.y + ball.radius + ground.size.y:
        break
    F = ball.m * g
    a = F/ball.m
    ball.pos = ball.pos + ball.v * dt + (1/2) * a * dt**2
    ball.v = ball.v + a*dt
    t += dt
    varrow.pos = ball.pos
    varrow.axis = 0.1 * ball.v
    positon_plot.plot(t, ball.pos.y)