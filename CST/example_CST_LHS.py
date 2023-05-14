from CST_LHS import *
from visualization import *

#------------------------------------------------------------------------------
# User inputs
#------------------------------------------------------------------------------
airfoil = 'rae2822' # airfoil .dat name
Nfit = 30 # number of points on each surface (upper and lower) of the airfoil that CST should be fit to
Ngen = 30 # number of points on each surface (upper and lower) of the generated airfoil surfaces
n = 100 # number of samples
scale = 0.5 # scale factor for LHS
dp = 5 # degree of polynomials
xu,zu,xl,zl = CST_LHS(airfoil,scale,dp,Nfit,Ngen,n) # LHS of CST design space
visualization(xu,zu,xl,zl,'CST') # visualization of CST design space