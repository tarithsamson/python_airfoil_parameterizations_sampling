import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from readairfoil import *
from scipy.stats import qmc

def BSpline_fit(xu_opt,zu_opt,xl_opt,zl_opt,t=None,k=3):

    #--------------------------------------------------------------------------
    # Knot vector generation
    #--------------------------------------------------------------------------
    if t is None:
        t = np.linspace(0, 1, len(xu_opt)) # Define knot vector (uniformly spaced)

    xu_opt = np.reshape(xu_opt,((len(xu_opt),1))) # reshaping xu_opt to be a column vector
    zu_opt = np.reshape(zu_opt,((len(zu_opt),1))) # reshaping zu_opt to be a column vector
    xl_opt = np.reshape(xl_opt,((len(xl_opt),1))) # reshaping xl_opt to be a column vector
    zl_opt = np.reshape(zl_opt,((len(zl_opt),1))) # reshaping zl_opt to be a column vector

    # Concatenate upper and lower surfaces into one array
    us = np.concatenate((xu_opt,zu_opt),axis=1) 
    ls = np.concatenate((xl_opt,zl_opt),axis=1)

    # Create B-spline object
    ubs = interpolate.make_interp_spline(t, us, k=k) 
    lbs = interpolate.make_interp_spline(t, ls, k=k)

    if lbs.c[0][1] != 0: # If the first control point of the lower surface is not zero, set it to zero
        lbs.c[0][1] = 0 

    if ubs.c[0][1] != 0: # If the first control point of the upper surface is not zero, set it to zero
        ubs.c[0][1] = 0

    return ubs,lbs