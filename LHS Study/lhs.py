from scipy.stats import qmc
import numpy as np

def lhs(l_bounds,u_bounds,n):
    
        d = len(l_bounds) # number of dimensions; DVs
        sampler = qmc.LatinHypercube(d) # asssigning d dimensions to an LHS sampler
        sample = sampler.random(n) # number of random samples = 1000*n, due to most airfoil being infeasible
        X = qmc.scale(sample,l_bounds,u_bounds) # creates matrix of samples, n rows by d columns
        X = np.transpose(X)
        
        return X