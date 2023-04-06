.. _readairfoil:

Reading Airfoil Data from the UIUC Database
============================================
This function reads airfoil data from the UIUC database. The database can be found at http://m-selig.ae.illinois.edu/ads/coord_database.html.

readairfoil.py
--------------
This function is  used to read airfoil data from the UIUC database. The function can read .dat files in both Selig and Lednicer format, however Selig format is recommended.

The input parameters to the readairfoil function are:

- **'airfoil'**: a string describing the name of the airfoil that is to be read from the UIUC database. The name of the airfoil should be in the format 'airfoilname.dat' where 'airfoilname' is the name of the airfoil. For example, the NACA 0012 airfoil would be specified as 'naca0012.dat'.
- **'f'**: a string that specifies the format of the airfoil data. The options are 'selig' or 'lednicer'. The default is 'selig'.
- **'DIR'**: a string that specifies the directory where the UIUC database is located. For example, the author's current directory ss '/home/user/Documents/work/uiuc_airfoil_database/'.
- **N**: an int that specifies the number of points to generate on the upper and lower surfaces
- **xdist**: a 1-D numpy array of x-coordinates at which the upper and lower surfaces are evaluated. If this parameter is not provided, the points will be generated uniformly between 0 and 1.

The outputs of the readairfoil function are:

- **xu**: a 1-D numpy array of the x-coordinates of the upper surface
- **zu**: a 1-D numpy array of the z-coordinates of the upper surface
- **xl**: a 1-D numpy array of the x-coordinates of the lower surface
- **zl**: a 1-D numpy array of the z-coordinates of the lower surface

Example: Reading an RAE2822 airfoil with readairfoil.py
-------------------------------------------------------  

Here's an example Python code snippet that uses readairfoil to read an RAE2822 airfoil from the UIUC database.

.. code-block::

   # import packages
   from readairfoil import * 
   import numpy as np
   import matplotlib.pyplot as plt

   airfoil = 'rae2822' # airfoil .dat name
   N = 100 # number of points describing each of the airfoil's upper and lower surfaces
   xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
   xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ); # generating N-1 x values from 0 to 1 whose distribution follows the formula
   xu,zu,xl,zl = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distribution

   plt.plot(xu,zu,marker='o',label='Upper Surface') # upper surface points          
   plt.plot(xl,zl,marker='o',label='Lower Surface') # lower surface points          
   plt.legend()
   plt.show()