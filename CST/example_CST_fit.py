import matplotlib.pyplot as plt
from readairfoil import *
from readairfoil import *
from CST import *
from CST_fit import *

#------------------------------------------------------------------------------
# User inputs
#------------------------------------------------------------------------------
airfoil = 'naca4412' # airfoil .dat name
N = 30 # number of points describing each of the airfoil's upper and lower surfaces
dp = 5 # degree of polynomials

#------------------------------------------------------------------------------
# Fit CST surface to target airfoil
#------------------------------------------------------------------------------
aLw, aUp = CST_fit(airfoil,dp,N)  

#------------------------------------------------------------------------------
# Plot CST surface and target airfoil
#------------------------------------------------------------------------------
xu,zu,xl,zl = CST(aLw,aUp,N) # generating airfoil with optimal design point

xu_opt,zu_opt,xl_opt,zl_opt = readairfoil(airfoil,N=N) # load target airfoil 

# plotting
fig = plt.figure(figsize=(6,9),dpi=(2**8))
plt.plot(xu_opt,zu_opt,marker="o",label='Target Airfoil Upper Surface')
plt.plot(xl_opt,zl_opt,marker="o",label='Target Airfoil Lower Surface')
plt.plot(xu,zu,linewidth=0.5,color='purple',marker="o",markersize=2,label='Optimal CST Airfoil Upper Surface')
plt.plot(xl,zl,linewidth=0.5,color='black',marker="o",markersize=2,label='Optimal CST Airfoil Lower Surface')
plt.xlabel('x/c')
plt.ylabel('y/c')
plt.grid()
plt.legend()
plt.show()