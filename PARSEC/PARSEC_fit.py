import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import differential_evolution
from PARSEC_fit_obj import *
from PARSEC import *
from readairfoil import *

#------------------------------------------------------------------------------
# Load airfoil
#------------------------------------------------------------------------------
airfoil = 'rae2822' # airfoil .dat name
N = 30 # number of points describing each of the airfoil's upper and lower surfaces
xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ) # generating N-1 x values from 0 to 1 whose distribution follows the formula
xu_opt,zu_opt,xl_opt,zl_opt = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distribution

#------------------------------------------------------------------------------
# Setting minimization arguments
#------------------------------------------------------------------------------
# rae2822
#              xu       zu       z_xxU    R_U      xl       zl       z_xxL    R_L #     t_TE     b_TE
# X0 = np.array([0.4306,  0.0629, -0.4272,  0.0081,  0.3438, -0.0589,  0.7008,  0.0085,  -6.7582,  9.1863, 0, 0]) # initial point

# naca0012
#               xu       zu       z_xxU    R_U      xl       zl       z_xxL    R_L #     t_TE     b_TE
X0 = np.array([0.2984,  0.0594, -0.4441,  0.0145,  0.2984, -0.0594,  0.4441,  0.0145,  -0.0000,  16.4423, -0.05, 0.05])

#xu,zu,xl,zl = parsec(X0,N)
xu,zu,xl,zl = PARSEC(X0,N,xdist=xdist)

#------------------------------------------------------------------------------
# Plot target and initial airfoil
#------------------------------------------------------------------------------
# plotting
parametrization = 'PARSEC'
fig = plt.figure(figsize=(6,9),dpi=(2**8))
plt.plot(xu_opt,zu_opt,marker="o",label='Optimal Airfoil Upper Surface')
plt.plot(xl_opt,zl_opt,marker="o",label='Optimal Airfoil Lower Surface')
plt.plot(xu,zu,linewidth=0.5,color='purple',marker="o",markersize=2,label='Initial Airfoil Upper Surface')
plt.plot(xl,zl,linewidth=0.5,color='black',marker="o",markersize=2,label='Initial Airfoil Lower Surface')
plt.xlabel('x/c')
plt.ylabel('y/c')
plt.grid()
#plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()

func = lambda x: np.linalg.norm(PARSEC_fit_obj(x,N,xu_opt,zu_opt,xl_opt,zl_opt,xdist)) # defining the objective function
bounds = np.array([ 
        (1e-4, 0.5),    # x coord of maximum z coord of the upper surface
        (0.0, 0.2),     #  maximum z coord of the upper surface
        (-0.5, 1),      # curvature of upper surface at maximum z-coord
        (1e-4, 0.2),    # LE radius of the upper surface
        (1e-4, 0.5),    # x coord of maximum z coord of the upper surface
        (-0.2, 0.0),    # maximum z coord of the lower surface
        (-0.5, 1),      # curvature of lower surface at minimum z-coord
        (1e-4, 0.1),    # LE radius of the lower surface
        (-30, 30),      # TE angle
        (-30, 30),      # TE wedge angle 
        (-0.02,0.02),   # TE offset
        (-0.05,0.05)])  # TE thickness

bounds = np.array(bounds) # converting bounds to numpy array
opt_x = None # initializing optimal design point
opt_f = np.inf # initializing optimal objective function value
res = differential_evolution(func, bounds=bounds, disp=1) # calling differential evolution
opt_x = res.x # optimal design point
opt_f = res.fun # optimal objective function value
        
print(opt_x)
print(opt_f)

xu,zu,xl,zl = PARSEC(opt_x,N,xdist=xdist) # generating airfoil with optimal design point

#------------------------------------------------------------------------------
# Plot target and initial airfoil
#------------------------------------------------------------------------------
# plotting
parametrization = 'PARSEC'
fig = plt.figure(figsize=(6,9),dpi=(2**8))
plt.plot(xu_opt,zu_opt,marker="o",label='Target Airfoil Upper Surface')
plt.plot(xl_opt,zl_opt,marker="o",label='Target Airfoil Lower Surface')
plt.plot(xu,zu,linewidth=0.5,color='purple',marker="o",markersize=2,label='Optimal PARSEC Airfoil Upper Surface')
plt.plot(xl,zl,linewidth=0.5,color='black',marker="o",markersize=2,label='Optimal PARSEC Airfoil Lower Surface')
plt.xlabel('x/c')
plt.ylabel('y/c')
plt.grid()
#plt.gca().set_aspect('equal', adjustable='box')
plt.legend()
plt.show()