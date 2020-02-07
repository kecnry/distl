
import distl

plot = True

gaussian = distl.normal(80, 3)
print(gaussian.sample(5))
if plot: gaussian.plot(1000, show=True)

boxcar = gaussian.to_uniform(sigma=3)
print(boxcar.sample(5))
if plot: boxcar.plot(1000, show=True)

hist = gaussian.to_histogram()
print(hist.sample(5))
if plot: hist.plot(1000, show=True)

gaussian_from_hist = hist.to_gaussian()
print(gaussian_from_hist.sample(5))
if plot: gaussian_from_hist.plot(1000, show=True)

boxcar_from_hist = hist.to_uniform(sigma=3)
print(boxcar_from_hist.sample(5))
if plot: boxcar_from_hist.plot(1000, show=True)
