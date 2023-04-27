import matplotlib.pyplot as plt
import numpy as np
from PARSEC_LHS import *
from visualization import *

#------------------------------------------------------------------------------
# Load target airfoil
#------------------------------------------------------------------------------
airfoil = 'rae2822' # airfoil .dat name
N = 30 # number of points describing each of the airfoil's upper and lower surfaces
n = 100
scale = 0.5
xu,zu,xl,zl = PARSEC_LHS(airfoil,scale,N,n)
visualization(xu,zu,xl,zl,'PARSEC')