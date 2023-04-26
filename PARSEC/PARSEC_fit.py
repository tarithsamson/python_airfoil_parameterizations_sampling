import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import differential_evolution
from PARSEC_fit_obj import *
from PARSEC import *
from readairfoil import *

def PARSEC_fit(xu_opt,zu_opt,xl_opt,zl_opt,N,xdist):
    
        func = lambda x: np.linalg.norm(PARSEC_fit_obj(x,N,xu_opt,zu_opt,xl_opt,zl_opt,xdist)) # defining the objective function

        #------------------------------------------------------------------------------
        # Fit PARSEC surface to target airfoil
        #------------------------------------------------------------------------------
        bounds = np.array([ 
                (1e-4, 0.5),    # x coord of maximum z coord of the upper surface
                (0.0, 0.2),     #  maximum z coord of the upper surface
                (-0.5, 1),      # curvature of upper surface at maximum z-coord
                (1e-4, 0.2),    # LE radius of the upper surface
                (1e-4, 0.5),    # x coord of maximum z coord of the upper surface
                (-0.2, 0.0),    # maximum z coord of the lower surface
                (-0.5, 1),      # curvature of lower surface at minimum z-coord
                (1e-4, 0.1),    # LE radius of the lower surface
                (-30, 30),      # TE angle
                (-30, 30),      # TE wedge angle 
                (-0.02,0.02),   # TE offset
                (-0.05,0.05)])  # TE thickness

        bounds = np.array(bounds) # converting bounds to numpy array
        res = differential_evolution(func, bounds=bounds, tol=1e-5, disp=1) # calling differential evolution

        return res.x