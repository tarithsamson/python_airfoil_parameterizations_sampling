from PARSEC_LHS import *
from visualization import *

#------------------------------------------------------------------------------
# User inputs
#------------------------------------------------------------------------------
airfoil = 'rae2822' # airfoil .dat name
Nfit = 30 # number of points on each surface (upper and lower) of the airfoil that PARSEC should be fit to
Ngen = 30 # number of points on each surface (upper and lower) of the generated airfoil surfaces
n = 100 # number of samples
scale = 0.5 # scale factor for LHS
xu,zu,xl,zl = PARSEC_LHS(airfoil,scale,Nfit,Ngen,n) # LHS of PARSEC design space
visualization(xu,zu,xl,zl,'PARSEC') # visualization of PARSEC design space