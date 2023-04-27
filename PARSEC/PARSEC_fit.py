import numpy as np
from scipy.optimize import differential_evolution
from PARSEC_fit_obj import *
from readairfoil import *

def PARSEC_fit(airfoil,N,xdist=None):
# def PARSEC_fit(xu_opt,zu_opt,xl_opt,zl_opt,N,xdist):

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
    
        #------------------------------------------------------------------------------
        # Fit PARSEC surface to target airfoil
        #------------------------------------------------------------------------------
        func = lambda x: np.linalg.norm(PARSEC_fit_obj(x,N,xu_opt,zu_opt,xl_opt,zl_opt,xdist)) # defining the objective function to be minimized
        
        # defining the bounds for the design variables
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