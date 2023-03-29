from dat_gen import *

#------------------------------------------------------------------------------
# Defining list of design space sizes
#------------------------------------------------------------------------------
n = [500] # array of design space sizes 
runs = 1 # number of runs per sample space
N = 100 # number of points describing each airfoil surface
parametrizations = ['PARSEC','CST', 'BSpline']
airfoil = 'rae2822' # initial airfoil to fit the parametrization methods to
scale = 0.5 # how much each fitted parametrization method must be scaled by to conduct LHS on

#------------------------------------------------------------------------------
# Call data genereation function
#------------------------------------------------------------------------------
dat_gen(n,runs,N,parametrizations,airfoil=airfoil,scale=scale)


