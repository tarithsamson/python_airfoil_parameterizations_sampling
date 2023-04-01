from PARSEC import *
import numpy as np
import matplotlib.pyplot as plt

# Generate surface points for the RAE 2822 airfoil surface via the PARSEC parametrization method with 150 points on each surface

#              xu      zu       z_xxU    R_U      xl       zl       z_xxL    R_L       t_TE     b_TE
X = np.array([0.4306,  0.0629, -0.4272,  0.0081,  0.3438, -0.0589,  0.7008,  0.0085,  -6.7582,  9.1863])

xu,zu,xl,zl = PARSEC(X,150)
plt.plot(xu,zu,label='Upper Surface') # upper surface points          
plt.plot(xl,zl,label='Lower Surface') # lower surface points          
plt.legend()
plt.show()

#############################################################################################################################

from CST import *
import numpy as np
import matplotlib.pyplot as plt

# Generate surface points for the RAE 2822 airfoil surface via the CST parametrization method with 150 points on each surface
#               aUp1        aUp2        aUp3        aUp4        aUp5       aLw1       aLw2       aLw3      aLw4       aLw5                                                             
X = np.array([-0.130048,  -0.133146,  -0.228736,  -0.0734107,  0.0378001, 0.127495,  0.140408,  0.1886,   0.194971,  0.200752])

xu,zu,xl,zl = CST(X,150)
plt.plot(xu,zu,label='Upper Surface') # upper surface points          
plt.plot(xl,zl,label='Lower Surface') # lower surface points          
plt.legend()
plt.show()

#############################################################################################################################

from CST import *
import numpy as np
import matplotlib.pyplot as plt

# Generate surface points for the RAE 2822 airfoil surface via the CST parametrization method with 150 points on each surface
#               aUp1        aUp2        aUp3        aUp4        aUp5       aLw1       aLw2       aLw3      aLw4       aLw5                                                             
X = np.array([-0.130048,  -0.133146,  -0.228736,  -0.0734107,  0.0378001, 0.127495,  0.140408,  0.1886,   0.194971,  0.200752])

xu,zu,xl,zl = CST(X,150)
plt.plot(xu,zu,label='Upper Surface') # upper surface points          
plt.plot(xl,zl,label='Lower Surface') # lower surface points          
plt.legend()
plt.show()



