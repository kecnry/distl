import npdists
import numpy as np
import astropy.units as units

a = npdists.uniform(5, 10, label='sma') * units.solRad
i = npdists.gaussian(45, 8, label='incl') * units.deg
d = npdists.delta(10, label='d')

dasini = d * a * np.sin(i)

print("d*asini = {}".format(dasini))

dasini.plot(show=True)
