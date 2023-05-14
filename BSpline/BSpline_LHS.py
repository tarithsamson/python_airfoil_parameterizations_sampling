from scipy.stats import qmc
import numpy as np
from readairfoil import *
from BSpline import *
from BSpline_fit import *

def BSpline_LHS(airfoil,numcp,Nfit,Ngen,k,n):
    
    # #------------------------------------------------------------------------------
    # # Load target airfoil
    # #------------------------------------------------------------------------------
    # xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
    # xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ) # generating N-1 x values from 0 to 1 whose distribution follows the formula
    # xu_opt,zu_opt,xl_opt,zl_opt = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distribution

    #------------------------------------------------------------------------------
    # Fit BSpline to target airfoil
    #------------------------------------------------------------------------------
    ubs, lbs = BSpline_fit(airfoil,Nfit,numcp=numcp,k=k) # fit B-spline to target airfoil
        
    ubscp = ubs.c
    lbscp = lbs.c

    u_bounds_1 = [0] * Ngen
    l_bounds_1 = [0] * Ngen
    l_bounds_2 = [0] * Ngen
    u_bounds_2 = [0] * Ngen

    scale = 0.5
    for i in range(len(ubscp)):
        if ubscp[i][1] > 0:
            u_bounds_1[i] = ubscp[i][1]*(1+scale)
            l_bounds_1[i] = ubscp[i][1]*(1-scale)
        else:
            u_bounds_1[i] = ubscp[i][1]*(1-scale)
            l_bounds_1[i] = ubscp[i][1]*(1+scale)
        if lbscp[i][1] > 0:
            u_bounds_2[i] = lbscp[i][1]*(1+scale)
            l_bounds_2[i] = lbscp[i][1]*(1-scale)
        else:
            u_bounds_2[i] = lbscp[i][1]*(1-scale)
            l_bounds_2[i] = lbscp[i][1]*(1+scale)

    u_bounds_1[0] = 0.00000001
    l_bounds_1[0] = 0.0

    n = 100
    d = len(l_bounds_1) # number of dimensions; DVs
    sampler = qmc.LatinHypercube(d) # asssigning d dimensions to an LHS sampler
    sample = sampler.random(n) # number of random samples = 1000*n, due to most airfoil being infeasible
    X1 = qmc.scale(sample,l_bounds_1,u_bounds_1) # creates matrix of samples, n rows by d columns
    X1 = np.transpose(X1)
    X2 = qmc.scale(sample,l_bounds_2,u_bounds_2) # creates matrix of samples, n rows by d columns
    X2 = np.transpose(X2)

    N = len(new_points)
    xu = np.zeros((Ngen,n))
    zu = np.zeros((Ngen,n))
    xl = np.zeros((Ngen,n))
    zl = np.zeros((Ngen,n))

    for i in range(n):
        for j in range(1,len(ubscp)-1):
            ubscp[j][1] = X1[j,i]
            lbscp[j][1] = X2[j,i]

        ubs.c = ubscp
        lbs.c = lbscp

        ubspnts = ubs(new_points)
        lbspnts = lbs(new_points)
        
        xu[:,i] = ubspnts[:,0]
        zu[:,i] = ubspnts[:,1]
        xl[:,i] = lbspnts[:,0]
        zl[:,i] = lbspnts[:,1]
    
    return xu,zu,xl,zl
