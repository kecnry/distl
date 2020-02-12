import distl
import numpy as np
import astropy.units as units

a = distl.uniform(5, 10) * units.solRad
i = distl.gaussian(45, 8) * units.deg

asini = a * np.sin(i)

print("asini = {}".format(asini))

asini.plot(show=True)
