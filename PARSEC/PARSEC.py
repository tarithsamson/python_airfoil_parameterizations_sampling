import numpy as np
from numpy.linalg import inv, det, lstsq

def PARSEC(X,N,xdist=None):
    #--------------------------------------------------------------------------
    # x-data generation
    #--------------------------------------------------------------------------
    if xdist is not None: # if xdist is provided, use it
        if N!=len(xdist): # if N doesn't match length of xdist, return error
            print('Error. N doesn\'t match length of xdist')
            return
        elif N==len(xdist): # if N matches length of xdist, use it
            xu = xdist
            xl = xdist
    else: # if xdist is not provided, generate it
        xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
        xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ) # generating N-1 x values from 0 to 1 whose distribution follows the formula
        xu = xdist
        xl = xdist
    
    #--------------------------------------------------------------------------
    # Input parameters
    #--------------------------------------------------------------------------
    # upper surface DVs
    X_U = X[0]      # x coord of maximum z coord of the upper surface
    Z_U = X[1]      # maximum z coord of the upper surface
    Z_xxU = X[2]    # curvature of upper surface at maximum z-coord
    R_U = X[3]      # LE radius of the upper surface 
    # lower surface DVs
    X_L = X[4]      # x coord of maximum z coord of the upper surface
    Z_L = X[5]      # maximum z coord of the upper surface
    Z_xxL = X[6]    # curvature of lower surface at minimum z-coord
    R_L = X[7]      # LE radius of the upper surface
    # TE DVs
    theta_TE = X[8] # TE angle (measured from the horizontal) in degrees
    beta_TE = X[9]  # TE wedge angle in degrees
    t_off = X[10]   # TE offset
    t_TE = X[11]    # TE thickness

    #--------------------------------------------------------------------------
    # PARSEC airfoil surface generation
    #--------------------------------------------------------------------------
    # 'P' coefficient matrix
    P = np.array([[X_U**0.5, X_U**1.5, X_U**2.5, X_U**3.5, X_U**4.5, X_U**5.5], 
                    [0.5*X_U**-0.5, 1.5*X_U**0.5, 2.5*X_U**1.5, 3.5*X_U**2.5, 4.5*X_U**3.5, 5.5*X_U**4.5],
                    [-0.25*X_U**-1.5, 0.75*X_U**-0.5, 3.75*X_U**0.5, 8.75*X_U**1.5, 15.75*X_U**2.5, 24.75*X_U**3.5],
                    [1, 1, 1, 1, 1, 1],
                    [0.5, 1.5, 2.5, 3.5, 4.5, 5.5],
                    [1, 0, 0, 0, 0, 0]                
                    ])

    # 'E' coefficient matrix
    E = np.array([[X_L**0.5, X_L**1.5, X_L**2.5, X_L**3.5, X_L**4.5, X_L**5.5], 
                    [0.5*X_L**-0.5, 1.5*X_L**0.5, 2.5*X_L**1.5, 3.5*X_L**2.5, 4.5*X_L**3.5, 5.5*X_L**4.5],
                    [-0.25*X_L**-1.5, 0.75*X_L**-0.5, 3.75*X_L**0.5, 8.75*X_L**1.5, 15.75*X_L**2.5, 24.75*X_L**3.5],
                    [1, 1, 1, 1, 1, 1],
                    [0.5, 1.5, 2.5, 3.5, 4.5, 5.5],
                    [1, 0, 0, 0, 0, 0]                
                    ])
    
    # 'q' coefficient matrix
    q = np.array([Z_U, 0, Z_xxU, t_off + 0.5*t_TE, np.tan(np.radians(theta_TE-0.5*beta_TE)), np.sqrt(2*R_U)]) 
    
    # 'v' coefficient matrix
    v = np.array([Z_L, 0, Z_xxL, t_off- 0.5*t_TE, np.tan(np.radians(theta_TE+0.5*beta_TE)), -np.sqrt(2*R_L)]) 
    
    a = np.linalg.lstsq(P,q)[0]
    b = np.linalg.lstsq(E,v)[0]

    # if det(P)==0:
    #     #print('det(P)=0')
    #     a = lstsq(P,q)
    # else:
    #     #print('det(P)!=%f'%det(P))
    #     # solve for coefficients of polynomial
    #     a = np.dot(inv(P),q)
    
    # if det(E)==0:
    #     #print('det(E)=0')
    #     b = lstsq(E,v)
    # else:
    #     #print('det(E)!=%f'%det(E))
    #     # solve for coefficients of polynomial
    #     b = np.dot(inv(E),v)
    
    zu = np.zeros(N) # upper surface coords
    zl = np.zeros(N) # lower surface coords

    # calculating the upper and lower surface coords from the sextic polynomial eqn
    zu = a[0]*xu**0.5 + a[1]*xu**1.5 + a[2]*xu**2.5 + a[3]*xu**3.5 + a[4]*xu**4.5 + a[5]*xu**5.5    
    zl = b[0]*xl**0.5 + b[1]*xl**1.5 + b[2]*xl**2.5 + b[3]*xl**3.5 + b[4]*xl**4.5 + b[5]*xl**5.5  # NOTE: THERE IS A REPEATED POINT AT (0,0) AND (1,0) IN BOTH SURFACES
    
    return xu,zu,xl,zl