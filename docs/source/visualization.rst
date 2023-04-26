.. _visualization:

Visualization
======================


Introduction
-------------    

The BSpline parametrization method is an airfoil parametrization method that is constructed by combining a set of control points with a set of basis functions. The control points determine the shape of the curve, while the basis functions determine how the curve is constructed. The basis functions are defined recursively using a set of knots, which are the points where the B-spline transitions from one basis function to the next.

visualization.py
--------------

This function is used to generate a BSpline given a set of input parameters. 

The input parameters to the BSpline function are:

- **X**: a 1-D list or array where ``X=[x_cp1, x_cp2, x_cp3, ..., z_cp1, z_cp2, z_cp3, ...]``. The first half of the list are the x-coordinates of the control points, while the second half are the z-coordinates of the control points.  
- **N**: an int that specifies the number of points to generate on the upper and lower surfaces
- **d**: an int that specifies the degree of the BSpline the surface
- **k**: a 1-D array of non-decreasing knots that control the B-Spline basis functions
- **xdist**: a 1-D numpy array of x-coordinates at which the upper and lower surfaces are evaluated. If this parameter is not provided, the points will be generated uniformly between 0 and 1.

The outputs of the BSpline function are:

- **xu**: a 1-D numpy array of the x-coordinates of the upper surface
- **zu**: a 1-D numpy array of the z-coordinates of the upper surface
- **xl**: a 1-D numpy array of the x-coordinates of the lower surface
- **zl**: a 1-D numpy array of the z-coordinates of the lower surface

Example: Visualizing the results of using LHS to Sample A PARSEC Design Space
------------------------------------------------------------------------------

Here's an example Python code snippet that uses the BSpline_fit.py to fit a PARSEC surface to an RAE2822 airfoil:

.. code-block::

   # import packages
   from readairfoil import * 
   from BSpline_fit import *
   import numpy as np
   import matplotlib.pyplot as plt
   from readairfoil import *

   airfoil = 'rae2822' # airfoil .dat name
   N = 100 # number of points describing each of the airfoil's upper and lower surfaces
   xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
   xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ); # generating N-1 x values from 0 to 1 whose distribution follows the formula
   xu,zu,xl,zl = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distribution

   X = B_Spline_fit(xu,zu,xl,zl,d,k,ncp) # fit BSpline surface to airfoil