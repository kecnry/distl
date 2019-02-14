import npdists
import numpy as np
import astropy.units as units

a = npdists.uniform(5, 10) * units.solRad
i = npdists.gaussian(45, 8) * units.deg

asini = a * np.sin(i)

print("asini = {}".format(asini))

asini.plot(show=True)
