import numpy as np
from numpy.linalg import inv, det, lstsq

def PARSEC(X,N,xdist=None):
    
    #--------------------------------------------------------------------------
    # Input processing
    #--------------------------------------------------------------------------
    if len(X.shape)==1:
        n=1
    else:
        nc,n = X.shape # number of airfoils is the length of the input matrix X
        
    zu = np.zeros((N,n)) # initializing an (n samples) x (N airfoil points) matrix of zeros for the airfoil upper surface
    zl = np.zeros((N,n)) # initializing an (n samples) x (N airfoil points) matrix of zeros for the airfoil lower surface
    
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
    
    X = np.transpose(X)
    
    #--------------------------------------------------------------------------
    # PARSEC airfoil surface generation
    #--------------------------------------------------------------------------
    for i in range(n):
        
        if len(X.shape)==1: # if X is an unstructured list; (10,), then initialize the variables as follows
            x_U = X[0]  # x coord of maximum z coord of the upper surface
            z_U = X[1] # maximum z coord of the upper surface
            z_xxU = X[2] # curvature of upper surface at maximum z-coord
            R_U = X[3] # LE radius of the upper surface 
            # lower surface DVs
            x_L = X[4] # x coord of maximum z coord of the upper surface
            z_L = X[5] # maximum z coord of the upper surface
            z_xxL = X[6] # curvature of upper surface at maximum z-coord
            R_L = X[7] # LE radius of the upper surface
            # TE DVs
            theta_TE = X[8] # TE angle (measured from the horizontal?) in radians
            beta_TE = X[9] # TE wedge angle in radians
            T_off = 0.0  # TE offset
            T_TE = 0.0   # TE thickness
            
        else: # if X is a structured list; (10,n), then initialize the variables as follows
            # upper surface DVs
            x_U = X[i,0]  # x coord of maximum z coord of the upper surface
            z_U = X[i, 1] # maximum z coord of the upper surface
            z_xxU = X[i, 2] # curvature of upper surface at maximum z-coord
            R_U = X[i, 3] # LE radius of the upper surface 
            # lower surface DVs
            x_L = X[i, 4] # x coord of maximum z coord of the upper surface
            z_L = X[i, 5] # maximum z coord of the upper surface
            z_xxL = X[i, 6] # curvature of upper surface at maximum z-coord
            R_L = X[i, 7] # LE radius of the upper surface
            # TE DVs
            theta_TE = X[i, 8] # TE angle (measured from the horizontal?) in radians
            beta_TE = X[i, 9] # TE wedge angle in radians
            T_off = 0.0  # TE offset
            T_TE = 0.0   # TE thickness
            
        # 'P' coefficient matrix
        P = np.array([[x_U**0.5, x_U**1.5, x_U**2.5, x_U**3.5, x_U**4.5, x_U**5.5], 
                     [0.5*x_U**-0.5, 1.5*x_U**0.5, 2.5*x_U**1.5, 3.5*x_U**2.5, 4.5*x_U**3.5, 5.5*x_U**4.5],
                     [-0.25*x_U**-1.5, 0.75*x_U**-0.5, 3.75*x_U**0.5, 8.75*x_U**1.5, 15.75*x_U**2.5, 24.75*x_U**3.5],
                     [1, 1, 1, 1, 1, 1],
                     [0.5, 1.5, 2.5, 3.5, 4.5, 5.5],
                     [1, 0, 0, 0, 0, 0]                
                     ])
        
        # 'E' coefficient matrix
        E = np.array([[x_L**0.5, x_L**1.5, x_L**2.5, x_L**3.5, x_L**4.5, x_L**5.5], 
                     [0.5*x_L**-0.5, 1.5*x_L**0.5, 2.5*x_L**1.5, 3.5*x_L**2.5, 4.5*x_L**3.5, 5.5*x_L**4.5],
                     [-0.25*x_L**-1.5, 0.75*x_L**-0.5, 3.75*x_L**0.5, 8.75*x_L**1.5, 15.75*x_L**2.5, 24.75*x_L**3.5],
                     [1, 1, 1, 1, 1, 1],
                     [0.5, 1.5, 2.5, 3.5, 4.5, 5.5],
                     [1, 0, 0, 0, 0, 0]                
                     ])
    
        # 'q' coefficient matrix
        q = np.array([z_U, 0, z_xxU, T_off + 0.5*T_TE, np.tan(np.radians(theta_TE-0.5*beta_TE)), np.sqrt(2*R_U)]) 
        
        # 'v' coefficient matrix
        v = np.array([z_L, 0, z_xxL, T_off- 0.5*T_TE, np.tan(np.radians(theta_TE+0.5*beta_TE)), -np.sqrt(2*R_L)]) 
        
        if det(P)==0:
            #print('det(P)=0')
            a = lstsq(P,q)
        else:
            #print('det(P)!=%f'%det(P))
            # solve for coefficients of polynomial
            a = np.dot(inv(P),q)
        
        if det(E)==0:
            #print('det(E)=0')
            b = lstsq(E,v)
        else:
            #print('det(E)!=%f'%det(E))
            # solve for coefficients of polynomial
            b = np.dot(inv(E),v)
            
        #print(a)
        #print(b)
        
        # calculating the upper and lower surface coords from the sextic polynomial eqn
        zu[:,i] = a[0]*xu**0.5 + a[1]*xu**1.5 + a[2]*xu**2.5 + a[3]*xu**3.5 + a[4]*xu**4.5 + a[5]*xu**5.5 # replacing zeros with surface coords after the label column
        zl[:,i] = b[0]*xl**0.5 + b[1]*xl**1.5 + b[2]*xl**2.5 + b[3]*xl**3.5 + b[4]*xl**4.5 + b[5]*xl**5.5 # replacing zeros with surface coords after the label column

    return xu,zu,xl,zl