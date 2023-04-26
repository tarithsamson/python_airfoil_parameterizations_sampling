import numpy as np
from scipy import interpolate

def BSpline(cp_u,cp_l,N,xdist=None,t=None,k=3):

    #--------------------------------------------------------------------------
    # x-data generation
    #--------------------------------------------------------------------------
    if xdist is not None:
        if N!=len(xdist):
            print('Error. N doesn\'t match length of xdist')
            return
        elif N==len(xdist):
            xu = xdist
            xl = xdist
    else:
        xdist = np.linspace(0,1,N)
        xu = xdist
        xl = xdist

    #--------------------------------------------------------------------------
    # Knot vector generation
    #--------------------------------------------------------------------------
    if t is None:
        t = np.linspace(0, 1, len(cp_u)) # Define knot vector (uniformly spaced)

    #--------------------------------------------------------------------------
    # BSpline airfoil generation
    #--------------------------------------------------------------------------
    # Create B-spline object
    ubs = interpolate.make_interp_spline(t, cp_u[:,1], k=k)
    lbs = interpolate.make_interp_spline(t, cp_l[:,1], k=k)

    # Evaluate B-spline at new points
    # new_points = np.linspace(0, 1, 100)
    zu = ubs(xu)
    zl = lbs(xl)

    return xu,zu,xl,zl