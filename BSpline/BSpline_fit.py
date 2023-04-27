import numpy as np
from scipy import interpolate
from readairfoil import *

# def BSpline_fit(xu_opt,zu_opt,xl_opt,zl_opt,t=None,k=3):
def BSpline_fit(airfoil,N,xdist=None,numcp=15,t=None,k=3):

    N = numcp # number of control points

    #--------------------------------------------------------------------------
    # x-data generation
    #--------------------------------------------------------------------------
    if xdist is not None: # if xdist is provided, use it
            if N!=len(xdist): # if N doesn't match length of xdist, return error
                    print('Error. N doesn\'t match length of xdist')
                    return
    else: # if xdist is not provided, generate it
            xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
            xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ) # generating N-1 x values from 0 to 1 whose distribution follows the formula

    #------------------------------------------------------------------------------
    # Load target airfoil
    #------------------------------------------------------------------------------
    xu_opt,zu_opt,xl_opt,zl_opt = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distribution
        
    # reshape xu_opt, zu_opt, xl_opt, zl_opt to be column vectors
    xu_opt = np.reshape(xu_opt,((len(xu_opt),1))) # reshaping xu_opt to be a column vector
    zu_opt = np.reshape(zu_opt,((len(zu_opt),1))) # reshaping zu_opt to be a column vector
    xl_opt = np.reshape(xl_opt,((len(xl_opt),1))) # reshaping xl_opt to be a column vector
    zl_opt = np.reshape(zl_opt,((len(zl_opt),1))) # reshaping zl_opt to be a column vector

    # Concatenate upper and lower surfaces into one array
    us = np.concatenate((xu_opt,zu_opt),axis=1) 
    ls = np.concatenate((xl_opt,zl_opt),axis=1)

    #--------------------------------------------------------------------------
    # Knot vector generation
    #--------------------------------------------------------------------------
    if t is None:
        t = np.linspace(0, 1, len(xu_opt)) # Define knot vector (uniformly spaced)

    #------------------------------------------------------------------------------
    # Fit BSpline surface to target airfoil
    #------------------------------------------------------------------------------
    # Create B-spline object
    ubs = interpolate.make_interp_spline(t, us, k=k) 
    lbs = interpolate.make_interp_spline(t, ls, k=k)

    if lbs.c[0][1] != 0: # If the first control point of the lower surface is not zero, set it to zero
        lbs.c[0][1] = 0 

    if ubs.c[0][1] != 0: # If the first control point of the upper surface is not zero, set it to zero
        ubs.c[0][1] = 0

    return ubs.c,lbs.c