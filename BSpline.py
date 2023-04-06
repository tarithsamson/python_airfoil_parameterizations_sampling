import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from readairfoil import *
from scipy.stats import qmc
from visualization import *

def Bspline(cp_u, cp_l, knots=None, degree=3)

    if knots is None:
        knots = np.linspace(0, 1, len(cp_u)) # Define knot vector (uniformly spaced)

    # Create B-spline object
    ubs = interpolate.make_interp_spline(knots, us, k=degree)
    lbs = interpolate.make_interp_spline(knots, ls, k=degree)

    # Evaluate B-spline at new points
    new_points = np.linspace(0, 1, 100)
    ubspnts = ubs(new_points)
    lbspnts = lbs(new_points)

    return ubspnts, lbspnts