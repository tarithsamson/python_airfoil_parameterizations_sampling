import matplotlib.pyplot as plt 
import numpy as np  
from readairfoil import * 
from BSpline import * 
from BSpline_fit import * 

#------------------------------------------------------------------------------
# User inputs
#------------------------------------------------------------------------------
airfoil = 'rae2822' # airfoil .dat name
N = 30 # number of points describing each of the airfoil's upper and lower surfaces
k = 3 # degree of B-spline
numcp = 7 # number of control points per surface

# #------------------------------------------------------------------------------
# # Fit BSpline to target airfoil
# #------------------------------------------------------------------------------
# ubs, lbs = BSpline_fit(airfoil,N,numcp=numcp,k=k) # fit B-spline to target airfoil

# #------------------------------------------------------------------------------
# # Evaluate B-Spline at new points
# #------------------------------------------------------------------------------
# new_points = np.linspace(0, 1, N) # 1000 new points from 0 to 1
# ubspnts = ubs(new_points) # upper surface points
# lbspnts = lbs(new_points) # lower surface points
# xu = ubspnts[:, 0] # x-coordinates of upper surface points
# zu = ubspnts[:, 1] # z-coordinates of upper surface points
# xl = lbspnts[:, 0] # x-coordinates of upper surface points
# zl = lbspnts[:, 1] # z-coordinates of upper surface points

#------------------------------------------------------------------------------
# Fit BSpline to target airfoil
#------------------------------------------------------------------------------
cp_u, cp_l = BSpline_fit(airfoil,N,numcp=numcp,k=k) # fit B-spline to target airfoil
print(cp_u)
xu,zu,xl,zl = BSpline(cp_u,cp_l,N,k=3) 

#------------------------------------------------------------------------------
# Plot BSpline surface and target airfoil
#------------------------------------------------------------------------------
xu_opt,zu_opt,xl_opt,zl_opt = readairfoil(airfoil,N=N) # load target airfoil 

# plotting
fig = plt.figure(figsize=(6,9),dpi=(2**8))
plt.plot(xu_opt,zu_opt,marker="o",label='Target Airfoil Upper Surface') # plot target airfoil upper surface
plt.plot(xl_opt,zl_opt,marker="o",label='Target Airfoil Lower Surface') # plot target airfoil lower surface
# plt.plot(ubs.c[:, 0], ubs.c[:, 1],'--',color='grey',marker='o',markersize=2,linewidth=0.7,label='B-spline Upper Surface Control Points') # plot B-spline upper surface control points
# plt.plot(lbs.c[:, 0], lbs.c[:, 1],'--',color='grey',marker='o',markersize=2,linewidth=0.7,label='B-spline Lower Surface Control Points') # plot B-spline lower surface control points
plt.plot(xu,zu,linewidth=0.5,color='purple',marker="o",markersize=2,label='Optimal BSpline Airfoil Upper Surface') # plot optimal B-spline upper surface
plt.plot(xl,zl,linewidth=0.5,color='black',marker="o",markersize=2,label='Optimal BSpline Airfoil Lower Surface') # plot optimal B-spline lower surface
plt.xlabel('x/c')
plt.ylabel('y/c')
plt.grid()
plt.legend(fontsize=6) 
plt.show()