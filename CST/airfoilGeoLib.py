import matplotlib.pyplot as plt
import numpy as np

def CST_airfoil(aLw,aUp,NP,dist="cos",teGAP=0):
    import numpy as np
    import math
    dp = len(aLw)
    b = np.zeros(dp)
    px = np.zeros(dp)
    px1= np.zeros(dp)
    for i in range(dp):
        b[i] = math.factorial(dp-1)/(math.factorial(i)*math.factorial(dp-i-1))            
        px[i] = i+0.5
        px1[i] = dp-i
    dTheta = 2*np.pi/(NP)
    theta = 0
    NP1 = NP+1
    x0 = np.zeros(NP1)
    z0 = np.zeros(NP1)
    # Cosine Distribution
    if dist=='cos':
        for i in range(NP1):
            x0[i] = math.cos(theta)/2+0.5
            if theta<np.pi:
                z0[i] = 0
                for j in range(dp):
                    z0[i] += aLw[j]*b[j]*((x0[i])**(px[j]))*((1 - x0[i])**(px1[j]))-x0[i]*teGAP/2
            else:
                z0[i] = 0
                for j in range(dp):
                    z0[i] += aUp[j]*b[j]*((x0[i])**(px[j]))*((1 - x0[i])**(px1[j]))+x0[i]*teGAP/2
            theta += dTheta 
    return x0, z0

def redist(x0,z0,dp,N2):
    import numpy as np
    import math
    #----------------------------------
    # Seperate lower and upper surface
    #----------------------------------
    N = len(x0)
    xLW = []; zLW = []
    xUP = []; zUP = []
    N_lw = 0
    for i in range(N):
        xLW.append(x0[i])
        zLW.append(z0[i])        
        if z0[i]*z0[i+1]<=0 and x0[i] < x0[i+1]:
            N_lw = i+1
            break
    N_up = N-N_lw
    if xLW[N_lw-1] != 0 and zLW[N_lw-1] != 0:
        xLW.append(0)
        zLW.append(0)
        N_lw += 1 
    if x0[N_lw] != 0 and z0[N_lw] != 0:
        xUP.append(0)
        zUP.append(0)
        N_up += 1
    for i in range(N_lw,N):
        xUP.append(x0[i])
        zUP.append(z0[i])
    #----------------------------------
    # Berstein polynomail coefficients by method of least squares
    #----------------------------------
    aLw = MLS_bernstein(xLW,zLW,dp)
    aUp = MLS_bernstein(xUP,zUP,dp)
    #----------------------------------
    # Redistribution wrt given number of points
    #----------------------------------
    x,z = CST_airfoil(aLw,aUp,N2)
    return x,z,aLw,aUp

def MLS_bernstein(x,z,dp):
    #-------------------------
    # Method of Least Squares algorithm
    # to find coef. of Bernstein Polynomial
    #-------------------------
    import math
    N = len(x)
    b = np.zeros(dp)
    p_x = np.zeros(dp)
    p_1_x= np.zeros(dp)
    for i in range(dp):
        b[i] = math.factorial(dp-1)/(math.factorial(i)*math.factorial(dp-i-1))            
        p_x[i] = i+0.5
        p_1_x[i] = dp-i
    b_2 = np.zeros(dp);  p_x_2 = np.zeros(dp); p_1_x_2 = np.zeros(dp)
    b_3 = np.zeros(dp);  p_x_3 = np.zeros(dp); p_1_x_3 = np.zeros(dp)
    de = np.zeros((dp,dp))
    Rhs = np.zeros(dp)
    for i in range(dp):
        b_2[i] = b[i]
        p_x_2[i] = p_x[i]
        p_1_x_2[i] = p_1_x[i]
        for j in range(dp):
            b_3[j] = b_2[i]*b[j]
            p_x_3[j] = p_x_2[i]+p_x[j]
            p_1_x_3[j] = p_1_x_2[i]+p_1_x[j]
            de[i,j] = 0
            for m in range(N):
                de[i,j] = de[i,j] + ((x[m])**(p_x_3[j])) * ((1 - x[m])**(p_1_x_3[j]))*b_3[j]
            Rhs[i] = 0
        for m in range(N):
            Rhs[i] = Rhs[i] + ((x[m])**(p_x_2[i]))*((1 - x[m])**(p_1_x_2[i]))*b_2[i]*(z[m])
    
    from scipy import linalg

    a = linalg.solve(de, Rhs)
    return a

def readAirfoil(air_path, extent='dat'):
    with open(air_path + "." + extent, "r") as f:
        airfoil_x, airfoil_z = [], []
        for row in f:
            if extent == "csv":
                row = str(row).split(",")        
            else:                                      
                row = str(row).split()
            try:
                airfoil_x.append(float(row[0]))
                airfoil_z.append(float(row[1]))
            except ValueError:
                print(row)        
    return airfoil_x, airfoil_z

def checkIntersection(x0,z0):
    #----------------------------------
    # Seperate lower and upper surface
    #----------------------------------
    N = len(x0)
    xLW = []; zLW = []
    xUP = []; zUP = []
    N_lw = 0
    for i in range(N):
        xLW.append(x0[i])
        zLW.append(z0[i])        
        if z0[i]*z0[i+1]<=0 and x0[i] < x0[i+1]:
            N_lw = i+1
            break
    N_up = N-N_lw
    if xLW[N_lw-1] != 0 and zLW[N_lw-1] != 0:
        xLW.append(0)
        zLW.append(0)
        N_lw += 1 
    if x0[N_lw] != 0 and z0[N_lw] != 0:
        xUP.append(0)
        zUP.append(0)
        N_up += 1
    for i in range(N_lw,N):
        xUP.append(x0[i])
        zUP.append(z0[i])
    eps = 0
    NI = len(xUP)
    NJ = len(xLW)
    xSH = None     
    for i in range(1,NI-2):
        xUP1 = xUP[i]; xUP2 = xUP[i+1]; zUP1 = zUP[i]; zUP2 = zUP[i+1]
        m_i = (zUP2-zUP1)/(xUP2-xUP1); n_i = zUP1-m_i*xUP1            
        for j in range(i,NJ-2):
            xLW1 = xLW[j]; xLW2 = xLW[j+1]; zLW1 = zLW[j]; zLW2 = zLW[j+1]                
            m_j = (zLW2-zLW1)/(xLW2-xLW1); n_j = zLW1-m_j*xLW1                    
            x_int = (n_j-n_i)/(m_i-m_j)               
            flg_i = 0; flg_j = 0
            if x_int-xUP1<eps and x_int-xUP2>eps:
                flg_i = 1
            elif x_int-xUP1>eps and x_int-xUP2<eps:
                flg_i = 1                                    
            if x_int-xLW1<eps and x_int-xLW2>eps:
                flg_j = 1
            elif x_int-xLW1>eps and x_int-xLW2<eps:
                flg_j = 1    
            if flg_i == 1 and flg_j == 1:                   
                xSH = x_int                     
                iSH = i     
                jSH = j                    
                break
    if xSH == None:
        interSec = False
    else:
        interSec = True          
    return interSec