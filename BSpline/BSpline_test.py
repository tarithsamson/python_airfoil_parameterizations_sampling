import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from readairfoil import *
from scipy.stats import qmc
from visualization import *


#def Bspline(d, knots=knots, cp):
#------------------------------------------------------------------------------
# Load airfoil
#------------------------------------------------------------------------------
airfoil = 'rae2822' # airfoil .dat name
N = 7 # number of points describing each of the airfoil's upper and lower surfaces
xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ); # generating N-1 x values from 0 to 1 whose distribution follows the formula
xu,zu,xl,zl = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distribution

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

ubscp = ubs.c
lbscp = lbs.c

l_bounds_1 = [0] * N
u_bounds_1 = [0] * N
l_bounds_2 = [0] * N
u_bounds_2 = [0] * N

scale = 0.5
for i in range(len(ubscp)):
    if ubscp[i][1] > 0:
        u_bounds_1[i] = ubscp[i][1]*(1+scale)
        l_bounds_1[i] = ubscp[i][1]*(1-scale)
    else:
        u_bounds_1[i] = ubscp[i][1]*(1-scale)
        l_bounds_1[i] = ubscp[i][1]*(1+scale)
    if lbscp[i][1] > 0:
        u_bounds_2[i] = lbscp[i][1]*(1+scale)
        l_bounds_2[i] = lbscp[i][1]*(1-scale)
    else:
        u_bounds_2[i] = lbscp[i][1]*(1-scale)
        l_bounds_2[i] = lbscp[i][1]*(1+scale)

u_bounds_1[0] = 0.00000001
l_bounds_1[0] = 0.0

n = 100
d = len(l_bounds_1) # number of dimensions; DVs
sampler = qmc.LatinHypercube(d) # asssigning d dimensions to an LHS sampler
sample = sampler.random(n) # number of random samples = 1000*n, due to most airfoil being infeasible
X1 = qmc.scale(sample,l_bounds_1,u_bounds_1) # creates matrix of samples, n rows by d columns
X1 = np.transpose(X1)
X2 = qmc.scale(sample,l_bounds_2,u_bounds_2) # creates matrix of samples, n rows by d columns
X2 = np.transpose(X2)

N = len(new_points)
xu = np.zeros((N,n))
zu = np.zeros((N,n))
xl = np.zeros((N,n))
zl = np.zeros((N,n))

for i in range(n):
    for j in range(1,len(ubscp)-1):
        ubscp[j][1] = X1[j,i]
        lbscp[j][1] = X2[j,i]

ubs.c = ubscp
lbs.c = lbscp

ubspnts = ubs(new_points)
lbspnts = lbs(new_points)

xu[:,i] = ubspnts[:,0]
zu[:,i] = ubspnts[:,1]
xl[:,i] = lbspnts[:,0]
zl[:,i] = lbspnts[:,1]

fig = plt.figure(dpi=(2**8))
#plt.grid(visible=None, which='both', axis='both')
plt.plot(ubs.c[:, 0], ubs.c[:, 1],'--',color='k',linewidth=2)
plt.plot(lbs.c[:, 0], lbs.c[:, 1],'--',color='k',linewidth=2)
plt.scatter(ubs.c[:, 0], ubs.c[:, 1],color='black',label='B-spline Control Points')
plt.scatter(lbs.c[:, 0], lbs.c[:, 1],color = 'black')
plt.plot(ubspnts[:, 0], ubspnts[:, 1], 'blue', label='B-spline Upper Surface')
plt.plot(lbspnts[:, 0], lbspnts[:, 1], 'red', label='B-spline Lower Surface')
plt.xlabel('x/c')
plt.ylabel('y/c')
plt.legend()
#plt.gca().set_aspect('equal', adjustable='box')
plt.show()

#visualization(xu,zu,xl,zl,'BSpline')