# import packages
from PARSEC import *
import numpy as np
import matplotlib.pyplot as plt

#              xu      zu       z_xxU    R_U      xl       zl       z_xxL    R_L       t_TE     b_TE
X = np.array([0.4306,  0.0629, -0.4272,  0.0081,  0.3438, -0.0589,  0.7008,  0.0085,  -6.7582,  9.1863])

N = 30 # number of points on each surface

xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ) # generating N-1 x values from 0 to 1 whose distribution follows the formula

xu,zu,xl,zl = PARSEC(X,N,xdist) # generate surface points using the PARSEC parametrization method

plt.plot(xu,zu,marker='o',label='Upper Surface') # upper surface points          
plt.plot(xl,zl,marker='o',label='Lower Surface') # lower surface points          
plt.legend()
plt.show()

# #############################################################################################################################

# from CST import *
# import numpy as np
# import matplotlib.pyplot as plt

# # Generate surface points for the RAE 2822 airfoil surface via the CST parametrization method with 150 points on each surface
# #               aUp1        aUp2        aUp3        aUp4        aUp5       aLw1       aLw2       aLw3      aLw4       aLw5                                                             
# X = np.array([-0.130048,  -0.133146,  -0.228736,  -0.0734107,  0.0378001, 0.127495,  0.140408,  0.1886,   0.194971,  0.200752])

# xu,zu,xl,zl = CST(X,150)
# plt.plot(xu,zu,label='Upper Surface') # upper surface points          
# plt.plot(xl,zl,label='Lower Surface') # lower surface points          
# plt.legend()
# plt.show()

# #############################################################################################################################

# from CST import *
# import numpy as np
# import matplotlib.pyplot as plt

# # Generate surface points for the RAE 2822 airfoil surface via the CST parametrization method with 150 points on each surface
# #              x1       x2       x3       x4       x5      x6       x7        y1    y2       y3       y4       y5       y6       y7               
# X = np.array([-0.130048,  -0.133146,  -0.228736,  -0.0734107,  0.0378001, 0.127495,  0.140408,  0.1886,   0.194971,  0.200752])

# xu,zu,xl,zl = CST(X,150)
# plt.plot(xu,zu,label='Upper Surface') # upper surface points          
# plt.plot(xl,zl,label='Lower Surface') # lower surface points          
# plt.legend()
# plt.show()


