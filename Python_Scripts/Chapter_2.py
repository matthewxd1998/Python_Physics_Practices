from vpython import *

task = input('Which task you want to perform? ')

if task == 1:
    test_plot = gdots()
    test_plot.plot(1,1)
    test_plot.plot(-1,-1)


if task == 2:
    #x0 = 0m, t0 = 0s, v = 0.45m/s, a = 0.5m/s^2, where is the cart after 1.5s
    #Break it in to small steps,dt=0.01

    g1 = graph(title="Distance vs. Time", xtitle='Time (s)', ytitle='Distance (m)', fast=True)
    x1 = gcurve(color=color.blue, markers=False)
    g2 = graph(title="Velocity vs. Time", ytitle= 'Velocity (m/s)', xtitle='Time (s)', fast=True)
    v1 = gcurve(color=color.red, markers=False)

    x = 0
    t = 0
    v = 0.45
    a = 0.5
    dt = 0.01
    i = 0

    x1.plot(t,x)
    v1.plot(t,v)

    while t <= 1.5:
        print("x = {} m at t = {} s".format(x, t))
        if t < 1.5:
            x = x + v*dt + (1/2)*a*dt**2
            t += dt
            v += a*dt
            i +=1
            x1.plot(t,x)
            v1.plot(t,v)
        else:
            break
            
    print(i)

if task == 3:
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

if task == 4:
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

if task == 5:
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

    while xa > xb:
        #print("x = {} m at t = {} s".format(x, t))
        if xa > xb:
            xa += va*dt
            xb = xb + vb*dt + (1/2)*ab*dt**2
            vb = vb + ab*dt
            t += dt
            i +=1
            xap.plot(t,xa)
            xbp.plot(t,xb)
        else:
            break
            
    print("xA = xB = {} at t = {}".format(xa, t))