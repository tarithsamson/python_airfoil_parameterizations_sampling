import numpy as np
import math

def CST(aLw,aUp,N,xdist=None):
    #--------------------------------------------------------------------------
    # Input processing
    #--------------------------------------------------------------------------
    zu = np.zeros((N))
    zl = np.zeros((N))
    teGAP=0
    
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
    
    x = xdist
    
    #--------------------------------------------------------------------------
    # CST airfoil surface generation
    #--------------------------------------------------------------------------
    dp = len(aLw)
    b = np.zeros(dp)
    px = np.zeros(dp)
    px1= np.zeros(dp)
    for i in range(dp):
        b[i] = math.factorial(dp-1)/(math.factorial(i)*math.factorial(dp-i-1))            
        px[i] = i+0.5
        px1[i] = dp-i
        
    for i in range(N):
        for j in range(dp):
            zl[i] += aUp[j]*b[j]*((x[i])**(px[j]))*((1 - x[i])**(px1[j]))+x[i]*teGAP/2
            zu[i] += aLw[j]*b[j]*((x[i])**(px[j]))*((1 - x[i])**(px1[j]))-x[i]*teGAP/2 # NOTE: THERE IS A REPEATED POINT AT (0,0) AND (1,0) IN BOTH SURFACES
    return x,zu,x,zl