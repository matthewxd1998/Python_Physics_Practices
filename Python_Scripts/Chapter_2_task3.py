from vpython import *

#x0 = 0m, t0 = 0s, v = 0.45m/s, a = -0.1m/s^2, where is the cart after 1.5s
#Break it in to small steps,dt=0.01

g1 = graph(title="Distance vs. Time", xtitle='Time (s)', ytitle='Distance (m)', fast=True)
x1 = gcurve(color=color.blue, markers=False)
g2 = graph(title="Velocity vs. Time", ytitle= 'Velocity (m/s)', xtitle='Time (s)', fast=True)
v1 = gcurve(color=color.red, markers=False)

x = 0
t = 0
v = 0.45
a = -0.1
dt = 0.01
i = 0

x1.plot(t,x)
v1.plot(t,v)

while t <= 10.5:
    print("x = {} m at t = {} s".format(x, t))
    if t < 10.5:
        x = x + v*dt + (1/2)*a*dt**2
        t += dt
        v += a*dt
        i +=1
        x1.plot(t,x)
        v1.plot(t,v)
    else:
        break
            
print(i)