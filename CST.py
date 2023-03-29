import numpy as np
import math

def CST(X,N,xdist=None):
    #--------------------------------------------------------------------------
    # Input processing
    #--------------------------------------------------------------------------
    dp2,n = X.shape
    zu = np.zeros((N,n))
    zl = np.zeros((N,n))
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
    dp = int(dp2/2)
    b = np.zeros(dp)
    px = np.zeros(dp)
    px1= np.zeros(dp)
    for i in range(dp):
        b[i] = math.factorial(dp-1)/(math.factorial(i)*math.factorial(dp-i-1))            
        px[i] = i+0.5
        px1[i] = dp-i
        
    for k in range(n):
        aUp = X[0:int(dp),k]
        aLw = X[int(dp):,k]
        
        for i in range(N):
            for j in range(dp):
                zl[i,k] += aUp[j]*b[j]*((x[i])**(px[j]))*((1 - x[i])**(px1[j]))+x[i]*teGAP/2
                zu[i,k] += aLw[j]*b[j]*((x[i])**(px[j]))*((1 - x[i])**(px1[j]))-x[i]*teGAP/2 # NOTE: THERE IS A REPEATED POINT AT (0,0) AND (1,0) IN BOTH SURFACES
    return x,zu,x,zl