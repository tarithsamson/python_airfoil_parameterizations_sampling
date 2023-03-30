.. _PARSEC_parametrization_method:

PARSEC Parametrization Method
================================

The code provided is for the PARSEC airfoil surface generation method. This method is used to generate the coordinates of the upper and lower surfaces of an airfoil based on a set of design variables. The PARSEC method uses polynomial equations to define the shape of the airfoil.

The input parameters to the PARSEC function are:

X: a numpy array of shape (10, n) or (10,), where n is the number of airfoils to generate. The shape (10, n) is a structured array where each column represents the design variables for an individual airfoil. The shape (10,) is an unstructured array where the elements represent the design variables for a single airfoil.
N: an integer representing the number of points to generate on the airfoil surface.
xdist: an optional parameter that can be used to specify the x-coordinates at which the airfoil surface points should be generated. If this parameter is not provided, the points will be generated uniformly between 0 and 1.
The output of the PARSEC function are:

zu: a numpy array of shape (N, n) containing the coordinates of the upper surface of the airfoil. Each column represents an individual airfoil.
zl: a numpy array of shape (N, n) containing the coordinates of the lower surface of the airfoil. Each column represents an individual airfoil.
The PARSEC function uses the input parameters to calculate the shape of the airfoil using polynomial equations. The function then generates N points on the airfoil surface using these equations. The resulting zu and zl arrays contain the coordinates of these surface points for each airfoil in the input array.

The Parsec Airfoil Parametrization Method
==========================================

The Parsec method is a parameterization method that uses a combination of polynomial functions and Fourier series to describe the shape of an airfoil. The method is based on the idea that the airfoil shape can be approximated by a series of curves, each of which is described by a set of parameters.

The basic equation for the Parsec method is:

.. math::

    z(x) = \sum_{i=1}^n a_i x^{2i-1} + \sum_{i=0}^{m-1} b_i \sin(\pi i x) + c

where :math:`z(x)` is the shape of the airfoil at position :math:`x`, :math:`n` is the number of polynomial terms, :math:`m` is the number of Fourier terms, and :math:`a_i`, :math:`b_i`, and :math:`c` are the parameters that define the shape of the airfoil.

To use the Parsec method to generate an airfoil shape, the following steps can be taken:

1. Choose the number of polynomial and Fourier terms to use.
2. Generate a set of initial guesses for the parameters :math:`a_i`, :math:`b_i`, and :math:`c`.
3. Use a nonlinear optimization algorithm to find the set of parameters that minimizes the difference between the generated airfoil shape and a target airfoil shape.

One advantage of the Parsec method is that it can generate a wide range of airfoil shapes using only a small number of parameters. Additionally, the method can be combined with other optimization techniques to produce airfoils with specific performance characteristics.

The implementation of the Parsec method can be found in various software packages, such as XFOIL, OpenVSP, and AirfoilTools. In Python, the method can be implemented using the `scipy.optimize.minimize` function and the `numpy` and `math` libraries.

Here's an example Python code snippet that uses the PARSC pararmetrization method to generate points for the RAE 2822 airfoil with an arbirtary x point distribution function with 100 points:

.. code-block:: python

    from PARSEC import *
    import numpy as np
    import matplotlib.pyplot as plt

    # Generate surface points for the RAE 2822 airfoil surface via the PARSEC parametrization method

    #              xu      zu       z_xxU    R_U      xl       zl       z_xxL    R_L #     t_TE     b_TE
    X = np.array([0.4306,  0.0629, -0.4272,  0.0081,  0.3438, -0.0589,  0.7008,  0.0085,  -6.7582,  9.1863])

    xu,zu,xl,zl = PARSEC(X,150)
    plt.plot(xu,zu,label='Upper Surface') # upper surface points          
    plt.plot(xl,zl,label='Lower Surface') # lower surface points          
    plt.legend()
    plt.show()