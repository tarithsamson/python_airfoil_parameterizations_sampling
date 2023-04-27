import matplotlib.pyplot as plt
import numpy as np
from CST_LHS import *
from visualization import *

#------------------------------------------------------------------------------
# User inputs
#------------------------------------------------------------------------------
airfoil = 'rae2822' # airfoil .dat name
N = 30 # number of points describing each of the airfoil's upper and lower surfaces
n = 100 # number of samples
dp = 5 # degree of polynomials
scale = 0.5 # scale factor for LHS
xu,zu,xl,zl = CST_LHS(airfoil,scale,N,n,dp) # LHS of CST design space
visualization(xu,zu,xl,zl,'CST') # visualization of CST design space