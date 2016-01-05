from matplotlib import use; use('Agg')
import matplotlib.pyplot as plt
from yt.mods import *

pf = load('DD0001/data0001')
ray = pf.h.ortho_ray(0,(0,0))

plt.subplot(411)
plt.semilogy(ray['x'], ray['Density'], c='k', ls='-', marker='.', ms=5)
plt.ylabel(r'Density (cm$^{-3}$)')
plt.xlim(0.42,0.58)

plt.subplot(412)
plt.semilogy(ray['x'], ray['Pressure'], c='k', ls='-', marker='.', ms=5)
plt.ylabel('Temperature (K)')
plt.xlim(0.42,0.58)

plt.subplot(413)
plt.plot(ray['x'], ray['x-velocity'], c='k', ls='-', marker='.', ms=5)
plt.ylabel('Velocity')
plt.xlabel('x')
plt.xlim(0.42,0.58)

plt.subplot(414)
plt.plot(ray['x'], ray['By'], c='k', ls='-', marker='.', ms=5)
plt.ylabel('By')
plt.xlabel('x')
plt.xlim(0.42,0.58)

plt.savefig('ZeldovichPancake.png')
