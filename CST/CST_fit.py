import os
import numpy as np
import airfoilGeoLib as geo


def CST_fit(airfoil,dp,N,xdist=None):
  
    #------------------------------------------------------------------------------
    # Read airfoil and redistribute coords
    #------------------------------------------------------------------------------
    codePath = os.path.dirname(os.path.realpath(__file__)); os.chdir(codePath)
    #Read airfoil from file with .dat extension
    x0, z0 = geo.readAirfoil(air_path=codePath+"/"+airfoil)
    x,z,aLw,aUp = geo.redist(x0, z0,dp,N) #Redistribute coordinates
    flag = geo.checkIntersection(x,z)
    print(flag)

    return aLw, aUp