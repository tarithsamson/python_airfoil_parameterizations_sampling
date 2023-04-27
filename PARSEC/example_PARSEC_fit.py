import matplotlib.pyplot as plt
from readairfoil import *
from PARSEC import *
from PARSEC_fit import *

#------------------------------------------------------------------------------
# User inputs
#------------------------------------------------------------------------------
airfoil = 'naca0010' # airfoil .dat name
N = 30 # number of points describing each of the airfoil's upper and lower surfaces

#------------------------------------------------------------------------------
# Fit PARSEC surface to target airfoil
#------------------------------------------------------------------------------
opt_x = PARSEC_fit(airfoil,N) # calling the optimizer to find the optimal design point

#------------------------------------------------------------------------------
# Plot PARSEC surface and target airfoil
#------------------------------------------------------------------------------
xu,zu,xl,zl = PARSEC(opt_x,N) # generating airfoil with optimal design point

xu_opt,zu_opt,xl_opt,zl_opt = readairfoil(airfoil,N=N) # load target airfoil 

# plotting
fig = plt.figure(figsize=(6,9),dpi=(2**8))
plt.plot(xu_opt,zu_opt,marker="o",label='Target Airfoil Upper Surface')
plt.plot(xl_opt,zl_opt,marker="o",label='Target Airfoil Lower Surface')
plt.plot(xu,zu,linewidth=0.5,color='purple',marker="o",markersize=2,label='Optimal PARSEC Airfoil Upper Surface')
plt.plot(xl,zl,linewidth=0.5,color='black',marker="o",markersize=2,label='Optimal PARSEC Airfoil Lower Surface')
plt.xlabel('x/c')
plt.ylabel('y/c')
plt.grid()
plt.legend()
plt.show()