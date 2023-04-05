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

BSpline.py
--------------

BSpline_fit.py
--------------

Example: Fitting a BSpline to an airfoil using BSpline_fit.py
--------------------------------------------------------------


Example: Creating a RAE2822 airfoil with BSpline.py
----------------------------------------------------