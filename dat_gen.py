import os
import numpy as np
import statistics as stat
from lhsbounds import *
from lhs import *
from postprocess import *
from visualization import *
from PARSEC import *
from CST import *
from BSpline import *


def dat_gen(n,runs,N,parametrizations,airfoil='naca0012',scale=0.5):
    
    for parametrization in parametrizations:
        # make a new directory for the airfoils and allow for a new directory even if there is already one with the same name
        os.makedirs(parametrization + ' Data',exist_ok=True)
    
    # for loop to loop through all design space sizes for all run lengths
    for i in range(0,len(n)):
        for j in range(0,runs):
            for parametrization in parametrizations:
                print('%s Parametrization Method, n = %i, Run %i' %(parametrization,n[i],j+1))
                
                #--------------------------------------------------------------------------
                # Generate LHS vector for each parametrization method
                #--------------------------------------------------------------------------
                l_bounds,u_bounds = lhsbounds(parametrization,airfoil,scale)
                X = lhs(l_bounds,u_bounds,n[i])
                
                #------------------------------------------------------------------------------
                # Airfoil surface generation and processing
                #------------------------------------------------------------------------------
                xu,zu,xl,zl = eval(parametrization+'(X,N)') # call respective parametrization method and store its output
                xu,zu,xl,zl,X,n_rej_max_wloc,n_rej_max_u,n_rej_max_l,n_rej_max_w,n_rej_intersec = postProcess(xu,zu,xl,zl,X,parametrization)
                visualization(xu,zu,xl,zl,parametrization)
    
    return
