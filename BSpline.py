import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt
from readairfoil import *
from scipy.stats import qmc
from visualization import *

# def BSpline(X,N,xdist=None):    
#     #--------------------------------------------------------------------------
#     # Input processing
#     #--------------------------------------------------------------------------
#     if len(X.shape)==1:
#         n=1
#     else:
#         nc,n = X.shape # number of airfoils is the length of the input matrix X
        
#     zu = np.zeros((N,n)) # initializing an (n samples) x (N airfoil points) matrix of zeros for the airfoil upper surface
#     zl = np.zeros((N,n)) # initializing an (n samples) x (N airfoil points) matrix of zeros for the airfoil lower surface
    
#     #--------------------------------------------------------------------------
#     # x-data generation
#     #--------------------------------------------------------------------------
#     if xdist is not None:
#         if N!=len(xdist):
#             print('Error. N doesn\'t match length of xdist')
#             return
#         elif N==len(xdist):
#             xu = xdist
#             xl = xdist
#     else:
#         xdist = np.linspace(0,1,N)
#         xu = xdist
#         xl = xdist

#     tck, u = interpolate.splprep(X.T, k=3)
#     xnew = np.linspace(0, 1, N)
#     out = interpolate.splev(xnew, tck)
#     x, z = out[0], out[1]

#     return x, z

num_points = 10
x_coords = np.linspace(0, 1, num_points)
y_coords = np.sin(x_coords * np.pi)

n_points = 100
X = np.column_stack((x_coords, y_coords))
tck, u = interpolate.splprep(X.T, k=3)
xnew = np.linspace(0, 1, n_points)
out = interpolate.splev(xnew, tck)
x, z = out[0], out[1]

plt.plot(x,z)