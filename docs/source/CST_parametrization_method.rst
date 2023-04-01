.. _CST_parametrization_method:

CST Parametrization Method
============================

The CST (Class Shape Transformation) airfoil parametrization method is a mathematical model that describes the shape of an airfoil using a set of control points. The shape of the airfoil is defined by a polynomial curve that passes through these control points.

The CST method assumes that the airfoil shape can be described by two separate functions: one for the upper surface and one for the lower surface. These functions are defined using the Bernstein polynomial basis and are expressed as linear combinations of Bernstein polynomials.

The Bernstein polynomials are defined as follows:

.. math::

    S(x)=\sum_{j=0}^{n-1} c_j B_{j, k ; t}(x)

where :math:B_{j, k ; t} are B-spline basis functions of degree :math:k and knots :math:t.

where :math:i is the degree of the polynomial, :math:n is the total degree of the polynomial, and :math:x is the independent variable.

In the CST method, the shape of the airfoil is defined by a set of coefficients :math:a_i and :math:b_i that determine the weights of the Bernstein polynomials for the upper and lower surfaces, respectively. The coefficients are chosen so that the resulting airfoil shape satisfies certain constraints, such as the location of the maximum thickness and the amount of camber.

The CST method also allows for the inclusion of a thickness distribution function, which is used to control the thickness of the airfoil. This function is expressed as a polynomial curve that passes through a set of thickness control points. The thickness distribution function is added to the upper and lower surface functions to generate the final airfoil shape.

The CST method is implemented in the following Python function:

.. code-block:: 

    def CST(X,N,xdist=None):
    """
    Compute the upper and lower surfaces of a CST airfoil given a set of control
    points and a number of discretization points.

    Parameters:
        X (ndarray): A (2*n, dp) array of control points, where n is the number of
            Bernstein polynomials and dp is the number of dimensions (typically 2).
        N (int): The number of discretization points.
        xdist (ndarray): A 1D array of x-coordinates for the discretization points.

    Returns:
        x (ndarray): A 1D array of x-coordinates for the upper and lower surface points.
        zu (ndarray): A (N, dp) array of y-coordinates for the upper surface points.
        zl (ndarray): A (N, dp) array of y-coordinates for the lower surface points.
    """
    
The input parameters are:

X: A (2*n, dp) array of control points, where n is the number of Bernstein polynomials and dp is the number of dimensions (typically 2).
N: The number of discretization points.
xdist: A 1D array of x-coordinates for the discretization points.
The output values are:

x: A 1D array of x-coordinates for the upper and lower surface points.
zu: A (N, dp) array of y-coordinates for the upper surface points.
zl: A (N, dp) array of y-coordinates for the lower surface points.
The CST function first generates a set of x-coordinates based on the input xdist or using the np.linspace function. It then computes the upper and lower surface functions by evaluating the Bernstein polynomials at each of these x-coordinates using the