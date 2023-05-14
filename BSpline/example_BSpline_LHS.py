import matplotlib.pyplot as plt
import numpy as np
from BSpline_LHS import *
from visualization import *

#------------------------------------------------------------------------------
# Load target airfoil
#------------------------------------------------------------------------------
airfoil = 'rae2822' # airfoil .dat name
numcp = 7 # number of B-Spline control points
k = 3 # degree of BSpline
Nfit = 30 # number of points on each surface (upper and lower) of the airfoil that PARSEC should be fit to
Ngen = 30 # number of points on each surface (upper and lower) of the generated airfoil surfaces
n = 100
dp = 5 # degree of polynomials
scale = 0.5
xu,zu,xl,zl = BSpline_LHS(airfoil,numcp,Nfit,Ngen,k,n)
visualization(xu,zu,xl,zl,'BSpline')