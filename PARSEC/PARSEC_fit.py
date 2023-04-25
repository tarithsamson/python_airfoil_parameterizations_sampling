import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import minimize
from scipy.optimize import differential_evolution
from PARSEC_fit_obj import *
from PARSEC import *
from readairfoil import *
from scipy.optimize import fmin_l_bfgs_b

#------------------------------------------------------------------------------
# Load airfoil
#------------------------------------------------------------------------------
airfoil = 'naca0012' # airfoil .dat name
N = 30 # number of points describing each of the airfoil's upper and lower surfaces
xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ) # generating N-1 x values from 0 to 1 whose distribution follows the formula
xu_opt,zu_opt,xl_opt,zl_opt = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distributionc

#------------------------------------------------------------------------------
# Setting minimization arguments
#------------------------------------------------------------------------------
# rae2822
#              xu       zu       z_xxU    R_U      xl       zl       z_xxL    R_L #     t_TE     b_TE
X0 = np.array([0.4306,  0.0629, -0.4272,  0.0081,  0.3438, -0.0589,  0.7008,  0.0085,  -6.7582,  9.1863]) # initial point

# naca0012
#               xu       zu       z_xxU    R_U      xl       zl       z_xxL    R_L #     t_TE     b_TE
#X0 = np.array([0.2984,  0.0594, -0.4441,  0.0145,  0.2984, -0.0594,  0.4441,  0.0145,  -0.0000,  16.4423])

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

# #------------------------------------------------------------------------------
# # Set minimization bounds
# #------------------------------------------------------------------------------
# #           xu          zu          z_xxU       R_U
# bnds_u =  ((None,None),(None,None),(None,None),(None,None)) # upper surface bounds
# #           xl          zl          z_xxL       R_L 
# bnds_l =  ((None,None),(None,None),(None,None),(None,None)) # lower surface bounds
# #           t_TE        b_TE        
# bnds_te = ((None,None),(None,None)) # trailing edge bounds
# bnds = bnds_u+bnds_l+bnds_te # concatenating design variable bounds
# cons = None # setting constraints
# eps=1e-3# setting optimization tolerance
# jac = 'cs'
# options = {
#         'finite_diff_rel_step': np.ones((11))
#     }

# #------------------------------------------------------------------------------
# # Run minimization
# #------------------------------------------------------------------------------
# X_opt = minimize(PARSEC_fit_obj,X0,args=(N,xu_opt,zu_opt,xl_opt,zl_opt,xdist),tol=eps,bounds=bnds,constraints=cons,method='BFGS')
# opt_x = X_opt.x

#              xu       zu       z_xxU    R_U      xl       zl       z_xxL    R_L #     t_TE     b_TE
#X0 = np.array([0.4306,  0.0629, -0.4272,  0.0081,  0.3438, -0.0589,  0.7008,  0.0085,  -6.7582,  9.1863, 0]) # initial point

func = lambda x: np.linalg.norm(PARSEC_fit_obj(x,N,xu_opt,zu_opt,xl_opt,zl_opt,xdist))
bounds = [
        (1e-4, 0.5), # x coord of maximum z coord of the upper surface
        (0.0, 0.2),  #  maximum z coord of the upper surface
        (-0.5, 1), # curvature of upper surface at maximum z-coord
        (1e-4, 0.2), # LE radius of the upper surface
        (1e-4, 0.5), # x coord of maximum z coord of the upper surface
        (-0.2, 0.0), # maximum z coord of the lower surface
        (-0.5, 1),   # curvature of lower surface at minimum z-coord
        (1e-4, 0.1), # LE radius of the lower surface
        (-30, 30),   # TE angle
        (-30, 30)]   # TE wedge angle

bounds = np.array(bounds)
n_restarts = 50
opt_x = None
opt_f = np.inf
x0s = np.random.uniform(bounds[:,0], bounds[:,1], size=(n_restarts, bounds.shape[0]))
i = 0
# for x0 in x0s:
#     print(i)
#     x, f, _ = fmin_l_bfgs_b(PARSEC_fit_obj,X0,args=(N,xu_opt,zu_opt,xl_opt,zl_opt,xdist),approx_grad=1,bounds=bounds,disp=1)
#     if f < opt_f:
#         opt_x = x
#         opt_f = f
    
res = differential_evolution(func, bounds=bounds, disp=1)
opt_x = res.x
opt_f = res.fun
        
print(opt_x)
print(opt_f)

#xu,zu,xl,zl = parsec(X0,N)
xu,zu,xl,zl = PARSEC(opt_x,N,xdist=xdist)

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