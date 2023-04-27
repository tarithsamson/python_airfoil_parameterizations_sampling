import numpy as np
from scipy import interpolate

def BSpline(cp_u,cp_l,N,xdist=None,t=None,k=3):

    #--------------------------------------------------------------------------
    # x-data generation
    #--------------------------------------------------------------------------
    if xdist is not None: # if xdist is provided, use it
        if N!=len(xdist): # if N doesn't match length of xdist, return error
            print('Error. N doesn\'t match length of xdist')
            return
        elif N==len(xdist): # if N matches length of xdist, use it
            xu = xdist
            xl = xdist
    else: # if xdist is not provided, generate it
        xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
        xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ) # generating N-1 x values from 0 to 1 whose distribution follows the formula
        xu = xdist
        xl = xdist

    zu = np.ones(N) # upper surface coords
    zl = np.ones(N) # lower surface coords

    # reshape xu, zu, xl, zl to be column vectors
    xu = np.reshape(xu,((len(xu),1))) # reshaping xu to be a column vector
    zu = np.reshape(zu,((len(zu),1))) # reshaping zu to be a column vector
    xl = np.reshape(xl,((len(xl),1))) # reshaping xl to be a column vector
    zl = np.reshape(zl,((len(zl),1))) # reshaping zl to be a column vector

    # Load airfoil data from file (x, y coordinates)
    #airfoil_data = np.loadtxt('airfoil.dat')
    us = np.concatenate((xu,zu),axis=1)
    ls = np.concatenate((xl,zl),axis=1)

    #--------------------------------------------------------------------------
    # Knot vector generation
    #--------------------------------------------------------------------------
    if t is None:
        t = np.linspace(0, 1, len(xu)) # Define knot vector (uniformly spaced)

    #--------------------------------------------------------------------------
    # BSpline airfoil generation
    #--------------------------------------------------------------------------
    # Create B-spline object
    ubs = interpolate.make_interp_spline(t,us,k=k)
    lbs = interpolate.make_interp_spline(t,ls,k=k)

    # change the control points of the B-spline to equal the surface points of the airfoil
    ubs.c = cp_u
    lbs.c = cp_l

    # Evaluate B-spline at new points
    # new_points = np.linspace(0, 1, 100)
    zu = ubs(xu)
    zl = lbs(xl)

    # Evaluate B-spline at new points
    new_points = np.linspace(0, 1, 100)
    ubspnts = ubs(new_points)
    lbspnts = lbs(new_points)

    xu = new_points
    xl = new_points
    zu = ubspnts
    zl = lbspnts

    return xu,zu,xl,zl