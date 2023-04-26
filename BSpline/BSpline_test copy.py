import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from readairfoil import *
from scipy.stats import qmc

#def Bspline(d, knots=knots, cp):
#------------------------------------------------------------------------------
# Load airfoil
#------------------------------------------------------------------------------
airfoil = 'rae2822' # airfoil .dat name
N = 7 # number of points describing each of the airfoil's upper and lower surfaces
xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ); # generating N-1 x values from 0 to 1 whose distribution follows the formula
xu,zu,xl,zl = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distribution

xu = np.reshape(xu,((len(xu),1)))
zu = np.reshape(zu,((len(zu),1)))
xl = np.reshape(xl,((len(xl),1)))
zl = np.reshape(zl,((len(zl),1)))

# Load airfoil data from file (x, y coordinates)
#airfoil_data = np.loadtxt('airfoil.dat')
us = np.concatenate((xu,zu),axis=1)
ls = np.concatenate((xl,zl),axis=1)

# Define knot vector (uniformly spaced)
knots = np.linspace(0, 1, len(us))

# Define degree of B-spline curve
degree = 3

# Create B-spline object
ubs = interpolate.make_interp_spline(knots, us, k=degree)
lbs = interpolate.make_interp_spline(knots, ls, k=degree)

# Evaluate B-spline at new points
new_points = np.linspace(0, 1, 100)
ubspnts = ubs(new_points)
lbspnts = lbs(new_points)

fig = plt.figure(dpi=(2**8))
#plt.grid(visible=None, which='both', axis='both')
plt.plot(ubs.c[:, 0], ubs.c[:, 1],'--',color='k',linewidth=2)
plt.plot(lbs.c[:, 0], lbs.c[:, 1],'--',color='k',linewidth=2)
plt.scatter(xu, zu,color='orange',label='Orignal Airfoil Points')
plt.scatter(xl, zl,color = 'orange')
plt.scatter(ubs.c[:, 0], ubs.c[:, 1],color='black',label='B-spline Control Points')
plt.scatter(lbs.c[:, 0], lbs.c[:, 1],color = 'black')
plt.plot(ubspnts[:, 0], ubspnts[:, 1], 'blue', label='B-spline Upper Surface')
plt.plot(lbspnts[:, 0], lbspnts[:, 1], 'red', label='B-spline Lower Surface')
plt.xlabel('x/c')
plt.ylabel('y/c')
plt.legend()
plt.show()