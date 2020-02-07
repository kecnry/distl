import distl
import numpy as np
import astropy.units as units

def customfunc(a, b):
   return a + b + np.random.random()

a = distl.uniform(5,10)
b = distl.gaussian(3, 2)

cf = distl.function(customfunc, None, a, b)
print("cf = customfunc(a, b) = {}".format(cf))

cf.plot(show=True)

cf.to_file('custom_func.npdist')

cfl = distl.from_file('custom_func.npdist')

cfl.plot(show=True)
