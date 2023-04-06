.. _BSpline_parametrization_method:

BSpline Airfoil Parametrization Method
=======================================

Introduction
-------------    

The BSpline parametrization method is an airfoil parametrization method that is constructed by combining a set of control points with a set of basis functions. The control points determine the shape of the curve, while the basis functions determine how the curve is constructed. The basis functions are defined recursively using a set of knots, which are the points where the B-spline transitions from one basis function to the next.


.. math::

    S(x)=\sum_{j=0}^{n-1} c_j B_{j, k ; t}(x)

where :math:`B_{j, k ; t}` are B-spline basis functions of degree :math:`k` and knots :math:`t`.

B-spline basis elements are defined via

.. math::

    \begin{array}{r}
    B_{i, 0}(x)=1, \text{ if } t_i \leq x<t_{i+1} \text{, otherwise } 0, \\
    B_{i, k}(x)=\frac{x-t_i}{t_{i+k}-t_i} B_{i, k-1}(x)+\frac{t_{i+k+1}-x}{t_{i+k+1}-t_{i+1}} B_{i+1, k-1}(x)
    \end{array}

This code uses Scipy's implementation of the B-spline basis functions to both fit a B-spline to an airfoil and to create a new airfoil from a set of control points. More information can be found in the Scipy documentation: https://docs.scipy.org/doc/scipy/reference/generated/scipy.interpolate.BSpline.html 

BSpline.py
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

Example: Creating an airfoil with BSpline.py
----------------------------------------------------
BSpline_fit.py is a script that fits a B-spline to an airfoil. The script takes in a set of control points and a set of knots and fits a B-spline to the airfoil. 

Here's an example Python code snippet that uses the BSpline pararmetrization method to generate points for the RAE 2822 airfoil with an arbirtary x point distribution function with 30 points on each surface:

.. code-block::

   # import packages
   from readairfoil import * 
   from BSpline import *
   import numpy as np
   import matplotlib.pyplot as plt

   #              
   X = np.array([]) # control point coordinates

   N = 30 # number of points on each surface

   xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
   xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ) # generating N-1 x values from 0 to 1 whose distribution follows the formula

   xu,zu,xl,zl = BSpline(X,N,d,k,xdist) # generate surface points using the BSpline parametrization method

   plt.plot(xu,zu,marker='o',label='Upper Surface') # upper surface points          
   plt.plot(xl,zl,marker='o',label='Lower Surface') # lower surface points          
   plt.legend()
   plt.show()


BSpline_fit.py
----------------

This function is used to fit a BSpline to a set of airfoil coordinates. 

The input parameters to the BSpline_fit function are:

- **xu**: a 1-D numpy array of the x-coordinates of the upper surface of the target airfoil
- **zu**: a 1-D numpy array of the z-coordinates of the upper surface of the target airfoil
- **xl**: a 1-D numpy array of the x-coordinates of the lower surface of the target airfoil
- **zl**: a 1-D numpy array of the z-coordinates of the lower surface of the target airfoil
- **d**: an int that specifies the degree of the BSpline the surface
- **k**: a 1-D array of non-decreasing knots that control the B-Spline basis functions
- **ncp**: an int that specifies that number of control points of the BSpline surface 

The outputs of the BSpline_fit function are:

- **X**: a 1-D list or array where ``X=[x_cp1, x_cp2, x_cp3, ..., z_cp1, z_cp2, z_cp3, ...]``. The first half of the list are the x-coordinates of the control points, while the second half are the z-coordinates of the control points.  

Example: Fitting a BSpline to an airfoil using BSpline_fit.py
--------------------------------------------------------------

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