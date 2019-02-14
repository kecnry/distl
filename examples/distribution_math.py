import npdists
import numpy as np
import astropy.units as units

g = npdists.gaussian(10, 2) * units.solRad
print("g = {}".format(g))
print("g*2 = {}".format(g*2))

g.plot(show=True)

u = npdists.uniform(5, 8) * units.solRad
print("u = {}".format(u))

u.plot(show=True)

c = g*u
print("c = g*u = {}".format(c))

c.plot(show=True)

s = g*np.sin(u)
print("s = g*sin(u) = {}".format(s))

s.plot(show=True)
