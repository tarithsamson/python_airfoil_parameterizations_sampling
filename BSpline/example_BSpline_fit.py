import matplotlib.pyplot as plt 
import numpy as np  
from readairfoil import * 
from BSpline import * 
from BSpline_fit import * 

#------------------------------------------------------------------------------
# User inputs
#------------------------------------------------------------------------------
airfoil = 'naca0012' # airfoil .dat name
N = 7 # number of points describing each of the airfoil's upper and lower surfaces
k = 3 # degree of B-spline
numcp = 12 # number of control points

#------------------------------------------------------------------------------
# Fit BSpline to target airfoil
#------------------------------------------------------------------------------
ubs, lbs = BSpline_fit(airfoil,N,numcp=numcp,k=k) # fit B-spline to target airfoil

#------------------------------------------------------------------------------
# Evaluate B-Spline at new points
#------------------------------------------------------------------------------
new_points = np.linspace(0, 1, 100) # 1000 new points from 0 to 1
ubspnts = ubs(new_points) # upper surface points
lbspnts = lbs(new_points) # lower surface points
xu = ubspnts[:, 0] # x-coordinates of upper surface points
zu = ubspnts[:, 1] # z-coordinates of upper surface points
xl = lbspnts[:, 0] # x-coordinates of upper surface points
zl = lbspnts[:, 1] # z-coordinates of upper surface points

#------------------------------------------------------------------------------
# Plot BSpline surface and target airfoil
#------------------------------------------------------------------------------
xu_opt,zu_opt,xl_opt,zl_opt = readairfoil(airfoil,N=30) # load target airfoil 

# plotting
fig = plt.figure(figsize=(6,9),dpi=(2**8))
plt.plot(ubs.c[:, 0], ubs.c[:, 1],'--',color='black',linewidth=2) # plot B-spline upper surface control points 
plt.plot(lbs.c[:, 0], lbs.c[:, 1],'--',color='black',linewidth=2) # plot B-spline lower surface control points
plt.scatter(xu_opt, zu_opt,color='orange',label='Orignal Airfoil Upper Surface Points') # plot original upper surface points
plt.scatter(xl_opt, zl_opt,color = 'orange',label='Original Airfoil Lower Surface Points') # plot original lower surface points
plt.scatter(ubs.c[:, 0],ubs.c[:, 1],color='black',label='B-spline Upper Surface Control Points') # plot B-spline upper surface control points
plt.scatter(lbs.c[:, 0],lbs.c[:, 1],color = 'black',label='B-spline Lower Surface Control Points') # plot B-spline lower surface control points
plt.plot(ubspnts[:, 0],ubspnts[:, 1],color='blue', label='B-spline Upper Surface') # plot B-spline upper surface
plt.plot(lbspnts[:, 0], lbspnts[:, 1],color='red', label='B-spline Lower Surface') # plot B-spline lower surface
plt.xlabel('x/c')
plt.ylabel('y/c')
plt.grid()
plt.legend(fontsize=8) 
plt.show()

# # plotting
# fig = plt.figure(figsize=(6,9),dpi=(2**8))
# plt.plot(xu_opt,zu_opt,marker="o",label='Target Airfoil Upper Surface')
# plt.plot(xl_opt,zl_opt,marker="o",label='Target Airfoil Lower Surface')
# plt.plot(xu,zu,linewidth=0.5,color='purple',marker="o",markersize=2,label='Optimal BSpline Airfoil Upper Surface')
# plt.plot(xl,zl,linewidth=0.5,color='black',marker="o",markersize=2,label='Optimal BSpline Airfoil Lower Surface')
# plt.xlabel('x/c')
# plt.ylabel('y/c')
# plt.grid()
# plt.legend()
# plt.show()