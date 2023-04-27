from scipy.stats import qmc
import numpy as np
from readairfoil import *
from PARSEC import *
from PARSEC_fit import *

def PARSEC_LHS(airfoil,scale,N,n):
    
    #------------------------------------------------------------------------------
    # Load target airfoil
    #------------------------------------------------------------------------------
    xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
    xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ) # generating N-1 x values from 0 to 1 whose distribution follows the formula
    xu_opt,zu_opt,xl_opt,zl_opt = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distribution

    #------------------------------------------------------------------------------
    # Fit PARSEC surface to target airfoil
    #------------------------------------------------------------------------------
    opt_X = PARSEC_fit(xu_opt,zu_opt,xl_opt,zl_opt,N,xdist)
    
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
    
    xu = np.zeros((N,n))
    zu = np.zeros((N,n))
    xl = np.zeros((N,n))
    zl = np.zeros((N,n))
    
    #------------------------------------------------------------------------------
    # Generating PARSEC Airfoils
    #------------------------------------------------------------------------------
    for i in range(n):
        xu[:,i],zu[:,i],xl[:,i],zl[:,i] = PARSEC(X[:,i],N,xdist=xdist)
    
    return xu,zu,xl,zl

