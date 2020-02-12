import distl
import astropy.units as u

g = distl.gaussian(80, 5) * u.deg

print(g.sample(5, unit=u.rad))
print(g.sample(5, as_quantity=True))


g.plot(show=True)
g.plot(unit=u.rad, show=True)
