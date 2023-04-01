.. _BSpline_parametrization_method:

BSpline Parametrization Method
====================================

The BSpline parametrization method is an airfoil parametrization method that uses onstructed by combining a set of control points with a set of basis functions. The control points determine the shape of the curve, while the basis functions determine how the curve is constructed. The basis functions are defined recursively using a set of knots, which are the points where the B-spline transitions from one basis function to the next.


.. math::

    S(x)=\sum_{j=0}^{n-1} c_j B_{j, k ; t}(x)

where :math:B_{j, k ; t} are B-spline basis functions of degree :math:k and knots :math:t.

Subsection 1
------------

Here you can describe a subsection of the Parametrization Method.

Subsection 2
------------

Here you can describe another subsection of the Parametrization Method.