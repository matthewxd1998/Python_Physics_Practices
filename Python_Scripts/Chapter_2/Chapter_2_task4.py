from vpython import *

g1 = graph(title="Distance vs. Time", xtitle='Time (s)', ytitle='Distance (m)', fast=False)
xap = gcurve(color=color.blue, markers=False)
xbp = gcurve(color=color.red, markers=False)

xa = 0.5
xb = 0
t = 0
va = 0.45
vb = 0
ab = 0.2
dt = 0.01
i = 0

xap.plot(t,xa)
xbp.plot(t,xb)

while t <= 10.5:
    #print("x = {} m at t = {} s".format(x, t))
    if t < 10.5:
        xa += va*dt
        xb = xb + vb*dt + (1/2)*ab*dt**2
        vb = vb + ab*dt
        t += dt
        i +=1
        xap.plot(t,xa)
        xbp.plot(t,xb)
    else:
        break
            
print(i)