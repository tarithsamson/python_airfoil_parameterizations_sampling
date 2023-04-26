import matplotlib.pyplot as plt
import numpy as np
from PARSEC import *
from readairfoil import *
from PARSEC_fit import *
from PARSEC_fit_obj import *

#------------------------------------------------------------------------------
# Load target airfoil
#------------------------------------------------------------------------------
airfoil = 'rae2822' # airfoil .dat name
N = 30 # number of points describing each of the airfoil's upper and lower surfaces
xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ) # generating N-1 x values from 0 to 1 whose distribution follows the formula
xu_opt,zu_opt,xl_opt,zl_opt = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distribution

#------------------------------------------------------------------------------
# Fit PARSEC surface to target airfoil
#------------------------------------------------------------------------------
opt_x = PARSEC_fit(xu_opt,zu_opt,xl_opt,zl_opt,N,xdist)

print(opt_x)

#------------------------------------------------------------------------------
# Plot PARSEC surface and target airfoil
#------------------------------------------------------------------------------
xu,zu,xl,zl = PARSEC(opt_x,N,xdist=xdist) # generating airfoil with optimal design point
# plotting
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