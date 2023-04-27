import matplotlib.pyplot as plt
import numpy as np
from BSpline_LHS import *
from visualization import *

#------------------------------------------------------------------------------
# Load target airfoil
#------------------------------------------------------------------------------
airfoil = 'rae2822' # airfoil .dat name
N = 30 # number of points describing each of the airfoil's upper and lower surfaces
n = 100
dp = 5 # degree of polynomials
scale = 0.5
xu,zu,xl,zl = CST_LHS(airfoil,scale,N,n,dp)
visualization(xu,zu,xl,zl,'CST')