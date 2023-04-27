from PARSEC_LHS import *
from visualization import *

#------------------------------------------------------------------------------
# User inputs
#------------------------------------------------------------------------------
airfoil = 'naca0012' # airfoil .dat name
N = 50 # number of points describing each of the airfoil's upper and lower surfaces
n = 100 # number of samples
scale = 0.5 # scale factor for LHS
xu,zu,xl,zl = PARSEC_LHS(airfoil,scale,N,n) # LHS of PARSEC design space
visualization(xu,zu,xl,zl,'PARSEC') # visualization of PARSEC design space