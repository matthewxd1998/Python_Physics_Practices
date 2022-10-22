from vpython import *

def test_max_range(v0, y):
    g1 = graph(title='Horizontal Distance vs Angle Launching at y = {}m'.format(y) ,xtitle='Angle \u00B0', ytitle='Horizontal Distance (m)')
    c1 = gcurve(color=color.cyan)
    
    g = vector(0,-9.81,0)
    mass = 0.5
    dt = 0.0001
    for ang in range(0,91):
        theta = ang * (pi/180)
        vel = v0 * vector(cos(theta), sin(theta), 0)
        mass = 0.5
        t = 0
        r = vector(0,y,0)

        while r.y >= 0:
            F = mass * g
            a = F/mass
            r = r + vel * dt + (1/2)*a*dt**2
            vel += a*dt
            t += dt
            if r.y < 0:
                break
        
        c1.plot(ang, r.x)
        print('Range = {}m at {}\u00B0'.format(r.x, ang))

test_max_range(3.5, 2)