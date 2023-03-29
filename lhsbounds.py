import numpy as np
from scipy import interpolate
from readairfoil import *

def lhsbounds(parametrization,airfoil,scale):
    
    #------------------------------------------------------------------------------
    # Load airfoil
    #------------------------------------------------------------------------------
    N = 100 # number of points describing each of the airfoil's upper and lower surfaces
    xi = np.arange(N) # generate ascending integers from 0 to 0 to N-1
    xdist = 1.0 - np.cos( xi* (np.pi)/2.0/(N - 1.0) ); # generating N-1 x values from 0 to 1 whose distribution follows the formula
    xu,zu,xl,zl = readairfoil(airfoil,xdist=xdist) # load airfoil with the following distribution
    
    #------------------------------------------------------------------------------
    # Get bounds for PARSEC surface
    #------------------------------------------------------------------------------
    if parametrization=="PARSEC":
        if airfoil=='naca0012':
            # naca0012
            #               xu       zu       z_xxU    R_U      xl       zl       z_xxL    R_L #     t_TE     b_TE
            X0 = np.array([0.2984,  0.0594, -0.4441,  0.0145,  0.2984, -0.0594,  0.4441,  0.0145,  0.000000001,  16.4423])
            
            l_bounds = np.zeros((len(X0)))
            u_bounds = np.zeros((len(X0)))
            
            for i in range(len(X0)):
                if X0[i]>=0:
                    l_bounds[i] = X0[i]*(1-scale)
                    u_bounds[i] = X0[i]*(1+scale)
                else:
                    l_bounds[i] = X0[i]*(1+scale)
                    u_bounds[i] = X0[i]*(1-scale)
        elif airfoil=='rae2822':
            #               xu      zu       z_xxU    R_U      xl       zl       z_xxL    R_L #     t_TE     b_TE
            X0 = np.array([0.4306,  0.0629, -0.4272,  0.0081,  0.3438, -0.0589,  0.7008,  0.0085,  -6.7582,  9.1863])
            
            l_bounds = np.zeros((len(X0)))
            u_bounds = np.zeros((len(X0)))
            
            for i in range(len(X0)):
                if X0[i]>=0:
                    l_bounds[i] = X0[i]*(1-scale)
                    u_bounds[i] = X0[i]*(1+scale)
                else:
                    l_bounds[i] = X0[i]*(1+scale)
                    u_bounds[i] = X0[i]*(1-scale)
                    
    #------------------------------------------------------------------------------
    # Get bounds for CST surface
    #------------------------------------------------------------------------------
    elif parametrization=="CST":
        if airfoil=='naca0012':
        #                   aUp1        aUp2       aUp3       aUp4        aUp5      aLw1       aLw2      aLw3      aLw4       aLw5                                                             
            X0 = np.array([-0.172046,  -0.14823,  -0.16697,  -0.114792,  -0.172237, 0.172046,  0.14823,  0.16697,  0.114792,  0.172237])
            
            l_bounds = np.zeros((len(X0)))
            u_bounds = np.zeros((len(X0)))
            
            for i in range(len(X0)):
                if X0[i]>=0:
                    l_bounds[i] = X0[i]*(1-scale)
                    u_bounds[i] = X0[i]*(1+scale)
                else:
                    l_bounds[i] = X0[i]*(1+scale)
                    u_bounds[i] = X0[i]*(1-scale)
        
        elif airfoil=='rae2822':
    
            #               aUp1        aUp2        aUp3        aUp4        aUp5       aLw1       aLw2       aLw3      aLw4       aLw5                                                             
            X0 = np.array([-0.130048,  -0.133146,  -0.228736,  -0.0734107,  0.0378001, 0.127495,  0.140408,  0.1886,   0.194971,  0.200752])
            
            l_bounds = np.zeros((len(X0)))
            u_bounds = np.zeros((len(X0)))
            #------------------------------------------------------------------------------
        # Get bounds for BSpline surface
        #------------------------------------------------------------------------------
        elif parametrization=='BSpline':
            
            xu = np.reshape(xu,((len(xu),1)))
            zu = np.reshape(zu,((len(zu),1)))
            xl = np.reshape(xl,((len(xl),1)))
            zl = np.reshape(zl,((len(zl),1)))
            
            # Load airfoil data from file (x, y coordinates)
            #airfoil_data = np.loadtxt('airfoil.dat')
            us = np.concatenate((xu,zu),axis=1)
            ls = np.concatenate((xl,zl),axis=1)
            
            # Define knot vector (uniformly spaced)
            knots = np.linspace(0, 1, len(us))
            
            # Define degree of B-spline curve
            degree = 3
            
            # Create B-spline object
            ubs = interpolate.make_interp_spline(knots, us, k=degree)
            lbs = interpolate.make_interp_spline(knots, ls, k=degree)
            
            # Evaluate B-spline at new points
            new_points = np.linspace(0, 1, 100)
            ubspnts = ubs(new_points)
            lbspnts = lbs(new_points)
            
            ubscp = ubs.c
            lbscp = lbs.c
            
            u_bounds_1 = [0] * N
            l_bounds_1 = [0] * N
            l_bounds_2 = [0] * N
            u_bounds_2 = [0] * N
            
            for i in range(len(ubscp)):
                if ubscp[i][1] > 0:
                    l_bounds_1[i] = ubscp[i][1]*(1-scale)
                    u_bounds_1[i] = ubscp[i][1]*(1+scale)
                    
                else:
                    l_bounds_1[i] = ubscp[i][1]*(1+scale)
                    u_bounds_1[i] = ubscp[i][1]*(1-scale)
                    
                if lbscp[i][1] > 0:
                    l_bounds_2[i] = lbscp[i][1]*(1-scale)
                    u_bounds_2[i] = lbscp[i][1]*(1+scale)
                    
                else:
                    l_bounds_2[i] = lbscp[i][1]*(1+scale)
                    u_bounds_2[i] = lbscp[i][1]*(1-scale)
                    
            l_bounds_1[0] = 0.0
            u_bounds_1[0] = 0.00000001
            for i in range(len(X0)):
                if X0[i]>=0:
                    l_bounds[i] = X0[i]*(1-scale)
                    u_bounds[i] = X0[i]*(1+scale)
                else:
                    l_bounds[i] = X0[i]*(1+scale)
                    u_bounds[i] = X0[i]*(1-scale)
                    
    #------------------------------------------------------------------------------
    # Get bounds for BSpline surface
    #------------------------------------------------------------------------------
    elif parametrization=='BSpline':
        
        xu = np.reshape(xu,((len(xu),1)))
        zu = np.reshape(zu,((len(zu),1)))
        xl = np.reshape(xl,((len(xl),1)))
        zl = np.reshape(zl,((len(zl),1)))
        
        # Load airfoil data from file (x, y coordinates)
        #airfoil_data = np.loadtxt('airfoil.dat')
        us = np.concatenate((xu,zu),axis=1)
        ls = np.concatenate((xl,zl),axis=1)
        
        # Define knot vector (uniformly spaced)
        knots = np.linspace(0, 1, len(us))
        
        # Define degree of B-spline curve
        degree = 3
        
        # Create B-spline object
        ubs = interpolate.make_interp_spline(knots, us, k=degree)
        lbs = interpolate.make_interp_spline(knots, ls, k=degree)
        
        # Evaluate B-spline at new points
        new_points = np.linspace(0, 1, 100)
        ubspnts = ubs(new_points)
        lbspnts = lbs(new_points)
        
        ubscp = ubs.c
        lbscp = lbs.c
        
        u_bounds_1 = [0] * N
        l_bounds_1 = [0] * N
        l_bounds_2 = [0] * N
        u_bounds_2 = [0] * N
        
        for i in range(len(ubscp)):
            if ubscp[i][1] > 0:
                l_bounds_1[i] = ubscp[i][1]*(1-scale)
                u_bounds_1[i] = ubscp[i][1]*(1+scale)
                
            else:
                l_bounds_1[i] = ubscp[i][1]*(1+scale)
                u_bounds_1[i] = ubscp[i][1]*(1-scale)
                
            if lbscp[i][1] > 0:
                l_bounds_2[i] = lbscp[i][1]*(1-scale)
                u_bounds_2[i] = lbscp[i][1]*(1+scale)
                
            else:
                l_bounds_2[i] = lbscp[i][1]*(1+scale)
                u_bounds_2[i] = lbscp[i][1]*(1-scale)
                
        l_bounds_1[0] = 0.0
        u_bounds_1[0] = 0.00000001
    
    return l_bounds,u_bounds

