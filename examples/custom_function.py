import npdists
import numpy as np
import astropy.units as units

def customfunc(a, b):
   return a + b + np.random.random()

a = npdists.uniform(5,10)
b = npdists.gaussian(3, 2)

cf = npdists.function(customfunc, None, a, b)
print("cf = customfunc(a, b) = {}".format(cf))

cf.plot(show=True)

cf.to_file('custom_func.npdist')

cfl = npdists.from_file('custom_func.npdist')

cfl.plot(show=True)
