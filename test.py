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

#############################################################################################################################

from CST import *
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



