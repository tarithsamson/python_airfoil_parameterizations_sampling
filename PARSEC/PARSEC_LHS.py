from scipy.stats import qmc
import numpy as np
from readairfoil import *
from PARSEC import *
from PARSEC_fit import *

def PARSEC_LHS(airfoil,scale,Nfit,Ngen,n):
    #------------------------------------------------------------------------------
    # Fit PARSEC surface to target airfoil
    #------------------------------------------------------------------------------
    opt_X = PARSEC_fit(airfoil,Nfit) # calling the optimizer to find the optimal design point
    
    #------------------------------------------------------------------------------
    # Get bounds for PARSEC surface
    #------------------------------------------------------------------------------
    l_bounds = np.zeros((len(opt_X)))
    u_bounds = np.zeros((len(opt_X)))
    
    for i in range(len(opt_X)):
        if opt_X[i]>=0:
            l_bounds[i] = opt_X[i]*(1-scale)
            u_bounds[i] = opt_X[i]*(1+scale)
        else:
            l_bounds[i] = opt_X[i]*(1+scale)
            u_bounds[i] = opt_X[i]*(1-scale)
        
    #------------------------------------------------------------------------------
    # Doing LHS within bounds
    #------------------------------------------------------------------------------
    d = len(l_bounds) # number of dimensions; DVs
    sampler = qmc.LatinHypercube(d) # asssigning d dimensions to an LHS sampler
    sample = sampler.random(n) # number of random samples = 1000*n, due to most airfoil being infeasible
    X = qmc.scale(sample,l_bounds,u_bounds) # creates matrix of samples, n rows by d columns
    X = np.transpose(X)
    
    xu = np.zeros((Ngen,n))
    zu = np.zeros((Ngen,n))
    xl = np.zeros((Ngen,n))
    zl = np.zeros((Ngen,n))
    
    #------------------------------------------------------------------------------
    # Generating PARSEC Airfoils
    #------------------------------------------------------------------------------
    for i in range(n):
        xu[:,i],zu[:,i],xl[:,i],zl[:,i] = PARSEC(X[:,i],Ngen)
    
    return xu,zu,xl,zl
