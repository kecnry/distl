import distl
import numpy as np
import astropy.units as units

a = distl.uniform(5, 10, label='sma') * units.solRad
i = distl.gaussian(45, 8, label='incl') * units.deg
d = distl.delta(10, label='d')

dasini = d * a * np.sin(i)

print("d*asini = {}".format(dasini))

dasini.plot(show=True)
