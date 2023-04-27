# python script that reads selig and lednicer airfoil .dat files into upper and lower surfaces
# please note that some as lednicer .dat files have positive y values as part of their lower surface it is recommended to use selig format

import numpy as np
from scipy.interpolate import interp1d

# def readairfoil(airfoil,f='selig',DIR = 'D:/work/uiuc_airfoil_database/',N=None,xdist=None):
def readairfoil(airfoil,f='selig',DIR = '/home/tarith/Documents/work/uiuc_airfoil_database/',N=None,xdist=None):
    
    #--------------------------------------------------------------------------
    # Read lednicer format airfoil
    #--------------------------------------------------------------------------
    if f == 'lednicer':
        airfoil_data = np.loadtxt(airfoil+'.dat',usecols=(0,1),skiprows=2) # use numpy module loadtxt to read x and z coords airfoil.dat file
        #airfoil_desc = np.loadtxt(airfoil+'.dat',dtype=str,max_rows=1) # use numpy module loadtxt to read the descriptive airfoil name from the first row
        S = np.loadtxt(airfoil+'.dat',usecols=(0,1),skiprows=1,max_rows=1) # use numpy module loadtxt to read the numer of points on the upper andlower surface from the second row 
        US = S[0] # index the number of points on the upper surface
        # index the x and z coords from airfoil_data to separate the x and z cords associated with the upper and lower surfaces 
        xu = airfoil_data[:int(US),0]
        zu = airfoil_data[:int(US),1]
        xl = airfoil_data[int(US):,0]
        zl = airfoil_data[int(US):,1]
        
    #--------------------------------------------------------------------------
    # Read selig format airfoil
    #--------------------------------------------------------------------------
    elif f == 'selig':
        airfoil_data = np.loadtxt(DIR+airfoil+'.dat',usecols=(0,1),skiprows=1) # use numpy module loadtxt to read x and z coords airfoil.dat file
        #airfoil_desc = np.loadtxt(airfoil+'.dat',dtype=str,max_rows=1) # use numpy module loadtxt to read the descriptive airfoil name from the first row
        US = np.argmax(airfoil_data[:,1]<0) # finding the index of the point at which the z values become negative; up to this point are points on the upper surface
        # index the x and z coords from airfoil_data to separate the x and z cords associated with the upper and lower surfaces 
        xu = airfoil_data[:int(US),0]
        zu = airfoil_data[:int(US),1]
        xl = airfoil_data[int(US):,0]
        zl = airfoil_data[int(US):,1]

    #--------------------------------------------------------------------------
    # Redistributing airfoil coords
    #--------------------------------------------------------------------------
    if N is None and xdist is None: # if N and xdist aren't specified, return the airfoil coords as is
        return xu,zu,xl,zl
    elif N is None and xdist is not None: # if xdist is specified, redistribute the airfoil coords to match the specified distribution
        fu = interp1d(xu,zu,fill_value="extrapolate") # initializing a 1D interpolation function to fit the upper surface
        zu = fu(xdist) # redistributing the z coords of the upper surface to match the x coord distribution
        xu = xdist # assign xdist values to xu
        fl = interp1d(xl,zl,fill_value="extrapolate") # initializing a 1D interpolation function to fit the lower surface
        zl = fl(xdist) # redistributing the z coords of the lower surface to match the x coord distribution
        xl = xdist # assign xdist values to xl
        return xu,zu,xl,zl
    elif N is not None and xdist is None: # if N is specified and xdist isn't specified,  redistribute the airfoil coords to match the specified distribution
        xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
        xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ) # generating N-1 x values from 0 to 1 whose distribution follows the formula
        fu = interp1d(xu,zu,fill_value="extrapolate") # initializing a 1D interpolation function to fit the upper surface
        zu = fu(xdist) # redistributing the z coords of the upper surface to match the x coord distribution
        xu = xdist # assign xdist values to xu
        fl = interp1d(xl,zl,fill_value="extrapolate") # initializing a 1D interpolation function to fit the lower surface
        zl = fl(xdist) # redistributing the z coords of the lower surface to match the x coord distribution
        xl = xdist # assign xdist values to xl
        return xu,zu,xl,zl
    elif N is not None and xdist is not None: 
        if N!=len(xdist): # if N and xdist are specified but N =/ len(xdist), return an error
            print('Error. N doesn\'t match length of xdist')
            return
        elif N==len(xdist): # if N and xdist are specified and N == len(xdist), redistribute airfoil coords to match the specified distribution
            fu = interp1d(xu,zu,fill_value="extrapolate") # initializing a 1D interpolation function to fit the upper surface
            zu = fu(xdist) # redistributing the z coords of the upper surface to match the x coord distribution
            xu = xdist # assign xdist values to xu
            fl = interp1d(xl,zl,fill_value="extrapolate") # initializing a 1D interpolation function to fit the lower surface
            zl = fl(xdist) # redistributing the z coords of the lower surface to match the x coord distribution
            xl = xdist # assign xdist values to xl
            return xu,zu,xl,zl