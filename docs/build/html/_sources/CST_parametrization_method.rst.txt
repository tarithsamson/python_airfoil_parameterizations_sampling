.. _CST_parametrization_method:

CST Airfoil Parametrization Method
======================================

Introduction
------------   

The CST (Class Shape Transformation) airfoil parametrization method is a mathematical model that describes the shape of an airfoil using a set of control points. The shape of the airfoil is defined by a polynomial curve that passes through these control points.

The CST method assumes that the airfoil shape can be described by two separate functions: one for the upper surface and one for the lower surface. These functions are defined using the Bernstein polynomial basis and are expressed as linear combinations of Bernstein polynomials.

CST.py
--------------

This function is used to generate a CST airfoil given a set of input parameters. 

The input parameters to the CST function are:

- **X**: a 1-D list or array where ``X=[uc1, uc2, uc3, ..., lc1, lc2, lc3, ...]``. The first half of the list are the coefficients of the upper surface, while the second half are the coefficients of the lower surface.
- **N**: an int that specifies the number of points to generate on the upper and lower surfaces
- **xdist**: a 1-D numpy array of x-coordinates at which the upper and lower surfaces are evaluated. If this parameter is not provided, the points will be generated uniformly between 0 and 1.

The outputs of the CST function are:

- **xu**: a 1-D numpy array of the x-coordinates of the upper surface
- **zu**: a 1-D numpy array of the z-coordinates of the upper surface
- **xl**: a 1-D numpy array of the x-coordinates of the lower surface
- **zl**: a 1-D numpy array of the z-coordinates of the lower surface

Example: Creating an airfoil with CST.py
----------------------------------------------------

Here's an example Python code snippet that uses the CST pararmetrization method to generate points for the RAE 2822 airfoil with an arbirtary x point distribution function with 30 points on each surface:

.. code-block::

   # import packages
   from readairfoil import *   
   from CST import *
   import numpy as np
   import matplotlib.pyplot as plt

   # define CST coefficients for rae2822 airfoil            
    #               aUp1        aUp2        aUp3        aUp4        aUp5       aLw1       aLw2       aLw3      aLw4       aLw5                                                             
    X0 = np.array([-0.130048,  -0.133146,  -0.228736,  -0.0734107,  0.0378001, 0.127495,  0.140408,  0.1886,   0.194971,  0.200752])

   N = 30 # number of points on each surface

   xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
   xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ) # generating N-1 x values from 0 to 1 whose distribution follows the formula

   xu,zu,xl,zl = CST(X,N,d,k,xdist) # generate surface points using the CST parametrization method

   plt.plot(xu,zu,marker='o',label='Upper Surface') # upper surface points          
   plt.plot(xl,zl,marker='o',label='Lower Surface') # lower surface points          
   plt.legend()
   plt.show()


CST_fit.py
----------------

This function is used to fit a CST to a set of airfoil coordinates. 

The input parameters to the CST_fit function are:

- **xu**: a 1-D numpy array of the x-coordinates of the upper surface of the target airfoil
- **zu**: a 1-D numpy array of the z-coordinates of the upper surface of the target airfoil
- **xl**: a 1-D numpy array of the x-coordinates of the lower surface of the target airfoil
- **zl**: a 1-D numpy array of the z-coordinates of the lower surface of the target airfoil
- **nc**: an int that specifies the number of coefficients of the CST parametrization method

The outputs of the CST_fit function are:

- **X**: a 1-D list or array where ``X=[uc1, uc2, uc3, ..., lc1, lc2, lc3, ...]``. The first half of the list are the coefficients of the upper surface, while the second half are the coefficients of the lower surface.
    
Example: Fitting a CST to an airfoil using CST_fit.py
--------------------------------------------------------------

Here's an example Python code snippet that uses the CST_fit.py to fit a PARSEC surface to an RAE2822 airfoil:

.. code-block::

   # import packages
   from readairfoil import * 
   from CST_fit import *
   import numpy as np
   import matplotlib.pyplot as plt
   from readairfoil import *

   airfoil = 'rae2822' # airfoil .dat name
   N = 100 # number of points describing each of the airfoil's upper and lower surfaces
   xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
   xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ); # generating N-1 x values from 0 to 1 whose distribution follows the formula
   xu,zu,xl,zl = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distribution

   X = CST_fit(xu,zu,xl,zl,nc) # fit CST surface to airfoil


