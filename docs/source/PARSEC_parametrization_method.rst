.. _PARSEC_parametrization_method:

Parsec Airfoil Parametrization Method
==========================================

Introduction
------------   

The PARSEC airfoil parameterization was developed by Sobieczky in 1998. 

\In the PARSEC method, the upper surface of the airfoil is described by a
sixth order polynomial:

.. math:: z_{u}(x)=\sum_{i=1}^{6} a_{i} x^{i-(1 / 2)},

where :math:`a_{i}, i=1, \ldots, 6`, are the polynomial coefficients,
and :math:`x` is the nondimensional chordwise location,
:math:`0 \leq x \leq 1`. The coefficients, shown in Fig. 7.4, are
determined by six geometrical constraints.

#. Maximum upper surface :math:`z`-coordinate :math:`z_{U}` at
   :math:`x_{U}`, i.e.:

.. math:: z_{u}\left(x_{U}\right)=z_{U}

2. First order derivative is zero at :math:`x_{U}`, i.e.:

.. math:: \left.\frac{d z_{u}}{d x}\right|_{x=x_{U}}=0

3. Prescribed second order derivative :math:`z_{x x U}` at
   :math:`x_{U}`, i.e.:

.. math:: \left.\frac{d^{2} z_{u}}{d x^{2}}\right|_{x=x_{U}}=z_{x x U}

4. Trailing edge (TE) off-set, :math:`t_{\text {off }}`, and thickness,
   :math:`t_{T E}`, i.e.:

.. math:: z_{u}(x=1)=t_{o f f}+\frac{1}{2} t_{T E}

5. TE direction angle, :math:`\theta_{T E}`, and wedge angle,
   :math:`\beta_{T E}`, i.e.:

.. math:: \left.\frac{d z_{u}}{d x}\right|_{x=1}=\tan \left(\theta_{T E}-\frac{1}{2} \beta_{T E}\right)

6. Prescribed LE radius of upper surface, :math:`R_{U}`. A circle at
   :math:`\left(x_{c}, z_{c}\right)` with a radius :math:`R_{U}`, and is
   defined as:

.. math:: \left(x-x_{c}\right)^{2}+\left(z-z_{c}\right)^{2}=R_{U}

The LE of the airfoil is at the origin, so
:math:`\left(x_{c}, z_{c}\right)=(0,0)`. We can write:

.. math:: z=\left(2 R_{U}-x\right)^{1 / 2} \cdot x^{1 / 2}

The upper surface polynomial can be written as:

.. math:: z_{u}=a_{1} \cdot x^{1 / 2}+\sum_{i=2}^{6} a_{i} x^{i-(1 / 2)} .

Comparing the two above equations for small :math:`x`, we obtain:

.. math:: a_{1} \cdot x^{1 / 2} \approx\left(2 R_{U}\right)^{1 / 2}

which is the condition that has been met at the LE. The above geometrical
constraints form a linear system of
equations:

.. math:: \boldsymbol {P a=q}

where:

.. math::

   \boldsymbol{P}=\left[\begin{array}{cccccc}
   x_{U}^{1 / 2} & x_{U}^{3 / 2} & x_{U}^{5 / 2} & x_{U}^{7 / 2} & x_{U}^{9 / 2} & x_{U}^{11 / 2} \\
   1 / 2 x_{U}^{-1 / 2} & 3 / 2 x_{U}^{1 / 2} & 5 / 2 x_{U}^{3 / 2} & 7 / 2 x_{U}^{5 / 2} & 9 / 2 x_{U}^{7 / 2} & 11 / 2 x_{U}^{9 / 2} \\
   -1 / 4 x_{U}^{-3 / 2} & 3 / 4 x_{U}^{-1 / 2} & 15 / 4 x_{U}^{1 / 2} & 35 / 4 x_{U}^{3 / 2} & 63 / 4 x_{U}^{5 / 2} & 99 / 4 x_{U}^{7 / 2} \\
   1 & 1 & 1 & 1 & 1 & 1 \\
   1 / 2 & 3 / 2 & 5 / 2 & 7 / 2 & 9 / 2 & 11 / 2 \\
   1 & 0 & 0 & 0 & 0 & 0
   \end{array}\right]

.. math::

   \begin{gathered}
   \boldsymbol{q}=\left[\begin{array}{c}
   z_{U} \\
   0 \\
   z_{x x U} \\
   t_{\text {off }}+1 / 2 t_{T E} \\
   \tan \left(\theta_{T E}-1 / 2 \beta_{T E}\right) \\
   \left(2 R_{U}\right)^{1 / 2}
   \end{array}\right] \\
   \boldsymbol{a}=\left[\begin{array}{lll}
   a_{1} & \cdots & a_{6}
   \end{array}\right]^{T} .
   \end{gathered}

The linear system has a unique solution given by:

.. math:: \boldsymbol {a={P}^{-1} q}

The lower surface is configured in a similar fashion. We have:

.. math:: z_{l}(x)=\sum_{i=1}^{6} b_{i} x^{i-(1 / 2)},

with the following constraints:

.. math::

   \begin{gathered}
   z_{l}\left(x_{L}\right)=z_{L} \\
   \left.\frac{d^{2} z_{l}}{d x^{2}}\right|_{x=x_{L}}=z_{x x L}, \\
   z_{l}(x=1)=t_{\text {off }}-\frac{1}{2} t_{T E},
   \end{gathered}

.. math::

   \begin{gathered}
   \left.\frac{d z_{l}}{d x}\right|_{x=1}=\tan \left(\theta_{T E}+\frac{1}{2} \beta_{T E}\right), \\
   b_{1} \cdot x^{1 / 2} \approx-\left(2 R_{L}\right)^{1 / 2}
   \end{gathered}

The linear system of equations is:

.. math:: \boldsymbol{Eb=v}

where :math:`\mathrm{E}=\mathrm{P}` and

.. math::

   \begin{gathered}
   \boldsymbol{v}=\left[\begin{array}{c}
   z_{L} \\
   0 \\
   z_{x x L} \\
   t_{o f f}-1 / 2 t_{T E} \\
   \tan \left(\theta_{T E}+1 / 2 \beta_{T E}\right) \\
   -\left(2 R_{L}\right)^{1 / 2}
   \end{array}\right] \\
   \boldsymbol{b}=\left[\begin{array}{lll}
   b_{1} & \cdots & b_{6}
   \end{array}\right]^{T} .
   \end{gathered}

The solution to the matrix equation is:

.. math:: \boldsymbol {b={E}^{-1} v}

Altogether, there are 12 parameters in the PARSEC formulation. Some of
the parameters can be fixed during an optimization. For example, setting
:math:`t_{T E}=0` will yield a sharp closed TE. Also, it is possible to
work only on the upper or the lower surface.


PARSEC.py
-----------------------------

The code provided is for the PARSEC airfoil surface generation method. This method is used to generate the coordinates of the upper and lower surfaces of an airfoil based on a set of design variables. The PARSEC method uses polynomial equations to define the shape of the airfoil.

The input parameters to the PARSEC function are:

X: a numpy array of shape (10, n) or (10,), where n is the number of airfoils to generate. The shape (10, n) is a structured array where each column represents the design variables for an individual airfoil. The shape (10,) is an unstructured array where the elements represent the design variables for a single airfoil.
N: an integer representing the number of points to generate on the airfoil surface.
xdist: an optional parameter that can be used to specify the x-coordinates at which the airfoil surface points should be generated. If this parameter is not provided, the points will be generated uniformly between 0 and 1.
The output of the PARSEC function are:

zu: a numpy array of shape (N, n) containing the coordinates of the upper surface of the airfoil. Each column represents an individual airfoil.
zl: a numpy array of shape (N, n) containing the coordinates of the lower surface of the airfoil. Each column represents an individual airfoil.
The PARSEC function uses the input parameters to calculate the shape of the airfoil using polynomial equations. The function then generates N points on the airfoil surface using these equations. The resulting zu and zl arrays contain the coordinates of these surface points for each airfoil in the input array.

PARSEC_fit.py
--------------

Example: Fitting a PARSEC surface to an airfoil using PARSEC_fit.py
--------------------------------------------------------------------


Example: Creating a RAE2822 airfoil with PARSEC.py
--------------------------------------------------

Here's an example Python code snippet that uses the PARSC pararmetrization method to generate points for the RAE 2822 airfoil with an arbirtary x point distribution function with 100 points:

.. code-block::

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