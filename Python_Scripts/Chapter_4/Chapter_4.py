from vpython import *

ball = sphere(pos=vector(0,0.1,0), radius=0.05, color=color.yellow, make_trail=True)
#print(ball.pos)
ball_no_air = sphere(pos=vector(0,0.1,0), radius=0.05, color=color.red, make_trail=True)

ground = box(pos=vector(0,0,0), size=vector(7,0.02,0.25))

g = vector(0,-9.8,0)

ball.m = 0.05
ball_no_air.m = 0.05

v0 = 7.2

theta = 73*pi/180

ball.v = v0 * vector(cos(theta),sin(theta),0)
ball_no_air.v = v0 * vector(cos(theta),sin(theta),0)

varrow = arrow(pos=ball.pos, axis=0.1 * ball.v, color=color.cyan)
varrow_no_air = arrow(pos=ball_no_air.pos, axis=0.1 * ball_no_air.v, color=color.green)

t = 0
dt = 0.001

g1 = graph(xtitle='Time (s)', ytitle='Height (m)')
positon_plot = gcurve(color=color.blue)
positon_plot.plot(t, ball.pos.y)

positon_plot_no_air = gcurve(color=color.red)
positon_plot_no_air.plot(t, ball_no_air.pos.y)

while ball_no_air.pos.y >= ground.pos.y + ball.radius + ground.size.y:
    rate(250)
    if ball_no_air.pos.y <= ground.pos.y + ball.radius + ground.size.y:
        break
    F = ball.m * g - ((1/2) * (1.2) * (pi * ball.radius**2) * (0.47) * (ball.v.mag**2) *  ball.v.norm())
    F_no_air = ball_no_air.m * g
    
    a = F/ball.m
    a_no_air = F_no_air/ball_no_air.m

    ball.pos = ball.pos + ball.v * dt + (1/2) * a * dt**2
    ball.v = ball.v + a*dt

    ball_no_air.pos = ball_no_air.pos + ball_no_air.v * dt + (1/2) * a_no_air * dt**2
    ball_no_air.v = ball_no_air.v + a_no_air*dt

    t += dt
    
    varrow.pos = ball.pos
    varrow.axis = 0.1 * ball.v

    varrow_no_air.pos = ball_no_air.pos
    varrow_no_air.axis = 0.1 * ball_no_air.v

    positon_plot_no_air.plot(t, ball_no_air.pos.y)
    positon_plot.plot(t, ball.pos.y)