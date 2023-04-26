import matplotlib.pyplot as plt 
import numpy as np  
from readairfoil import * 
from BSpline import * 
from BSpline_fit import * 

#------------------------------------------------------------------------------
# Load target airfoil
#------------------------------------------------------------------------------
airfoil = 'naca0012' # airfoil .dat name
N = 14 # number of points describing each of the airfoil's upper and lower surfaces
xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ); # generating N-1 x values from 0 to 1 whose distribution follows the formula
xu_opt,zu_opt,xl_opt,zl_opt = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distribution

#------------------------------------------------------------------------------
# Fit BSpline to target airfoil
#------------------------------------------------------------------------------
ubs, lbs = BSpline_fit(xu_opt,zu_opt,xl_opt,zl_opt) # fit B-spline to target airfoil

print(ubs.c)
print(lbs.c)

#------------------------------------------------------------------------------
# Evaluate B-Spline at new points
#------------------------------------------------------------------------------
new_points = np.linspace(0, 1, 1000) # 1000 new points from 0 to 1
ubspnts = ubs(new_points) # upper surface points
lbspnts = lbs(new_points) # lower surface points

#------------------------------------------------------------------------------
# Plot BSpline surface and target airfoil
#------------------------------------------------------------------------------
fig = plt.figure(dpi=(2**8)) 
plt.plot(ubs.c[:, 0], ubs.c[:, 1],'--',color='k',linewidth=2) # plot B-spline upper surface control points 
plt.plot(lbs.c[:, 0], lbs.c[:, 1],'--',color='k',linewidth=2) # plot B-spline lower surface control points
plt.scatter(xu_opt, zu_opt,color='orange',label='Orignal Airfoil Upper Surface Points') # plot original upper surface points
plt.scatter(xl_opt, zl_opt,color = 'orange',label='Original Airfoil Lower Surface Points') # plot original lower surface points
plt.scatter(ubs.c[:, 0], ubs.c[:, 1],color='black',label='B-spline Upper Surface Control Points') # plot B-spline upper surface control points
plt.scatter(lbs.c[:, 0], lbs.c[:, 1],color = 'black',label='B-spline Lower Surface Control Points') # plot B-spline lower surface control points
plt.plot(ubspnts[:, 0], ubspnts[:, 1], 'blue', label='B-spline Upper Surface') # plot B-spline upper surface
plt.plot(lbspnts[:, 0], lbspnts[:, 1], 'red', label='B-spline Lower Surface') # plot B-spline lower surface
plt.legend(fontsize=8) 
plt.show() 