import numpy as np
from PARSEC import *

def PARSEC_fit_obj(X,N,xu_opt,zu_opt,xl_opt,zl_opt,xdist):

    xu,zu,xl,zl = PARSEC(X,N,xdist=xdist) # calling PARSEC to generate the surface from the current design point
    
    Eu = 0 # initializing error for upper surface
    El = 0 # initializing error for lower surface   
    
    for i in range(N):
        du = abs(zu_opt[i]-zu[i])
        dl = abs(zl_opt[i]-zl[i])
        Eu = Eu + du
        El = El + dl

    E = Eu + El  # summing the errors to return a single scalar objective function value

    return E