import sys
import numpy as np
from scipy.stats import qmc
from lhsbounds import *
from postprocess import *
from visualization import *
import os
import statistics as stat

def dat_gen(n,runs,N,parametrizations,init_airfoil='naca0012',scale=0.5):
    
    #--------------------------------------------------------------------------
    # Import parametrization methods
    #--------------------------------------------------------------------------
    for parametrization in parametrizations:
        exec('sys.path.append(\'D:\codelab_campus\Simple Wing Generator\Simple Wing Generator/parametrizations/'+parametrization+'\')')
        exec('from '+parametrization+' import *')
        
        # create folder to save airfoil plots in
        # make a new directory for the airfoils and allow for a new directory even if there is already one with the same name
        os.makedirs(parametrization + ' Data',exist_ok=True)
        
        #--------------------------------------------------------------------------
        # Initialize empty arrays to store rejection data for each design space
        #--------------------------------------------------------------------------
        # exec('n_rej_max_wloc_'+parametrization+' = np.zeros(runs)')
        # exec('n_rej_max_u_'+parametrization+' = np.zeros(runs)')
        # exec('n_rej_max_l_'+parametrization+' = np.zeros(runs)')
        # exec('n_rej_max_w_'+parametrization+' = np.zeros(runs)')
        # exec('n_rej_intersec_'+parametrization+'= np.zeros(runs)')
    
    n_rej_max_wloc_PARSEC= np.zeros(runs)
    n_rej_max_u_PARSEC = np.zeros(runs)
    n_rej_max_l_PARSEC = np.zeros(runs)
    n_rej_max_w_PARSEC = np.zeros(runs)
    n_rej_intersec_PARSEC = np.zeros(runs)
    
    n_rej_max_wloc_CST= np.zeros(runs)
    n_rej_max_u_CST = np.zeros(runs)
    n_rej_max_l_CST = np.zeros(runs)
    n_rej_max_w_CST = np.zeros(runs)
    n_rej_intersec_CST = np.zeros(runs)
    
    # for loop to loop through all design space sizes for all run lengths
    for i in range(0,len(n)):
        for j in range(0,runs):
            for parametrization in parametrizations:
                
                print('%s Parametrization Method, n = %i, Run %i' %(parametrization,n[i],j+1))
                
                #--------------------------------------------------------------------------
                # Generate lhs for each parametrization method
                #--------------------------------------------------------------------------
                l_bounds,u_bounds = lhs_bounds(parametrization,init_airfoil,scale)
           
                #----------------------------------------------------------------------
                # LHS based on bounds
                #----------------------------------------------------------------------
                d = len(l_bounds) # number of dimensions; DVs
                sampler = qmc.LatinHypercube(d) # asssigning d dimensions to an LHS sampler
                sample = sampler.random(n[i]) # number of random samples = 1000*n, due to most airfoil being infeasible
                X = qmc.scale(sample,l_bounds,u_bounds) # creates matrix of samples, n rows by d columns
                X = np.transpose(X)
                #------------------------------------------------------------------------------
                # Airfoil surface generation and processing
                #------------------------------------------------------------------------------
                xu,zu,xl,zl = eval(parametrization+'(X,N)') # call respective parametrization method and store its output
                xu,zu,xl,zl,X,n_rej_max_wloc,n_rej_max_u,n_rej_max_l,n_rej_max_w,n_rej_intersec = postProcess(xu,zu,xl,zl,X,parametrization)
                visualization(xu,zu,xl,zl,parametrization)
            
                if parametrization == 'PARSEC':
                    n_rej_max_wloc_PARSEC[j]= n_rej_max_wloc/n[i]
                    n_rej_max_u_PARSEC[j] = n_rej_max_u/n[i]
                    n_rej_max_l_PARSEC[j] = n_rej_max_l/n[i]
                    n_rej_max_w_PARSEC[j] = n_rej_max_w/n[i]
                    n_rej_intersec_PARSEC[j] = n_rej_intersec/n[i]
                    
                if parametrization == 'CST':
                    n_rej_max_wloc_CST[j]= n_rej_max_wloc/n[i]
                    n_rej_max_u_CST[j] = n_rej_max_u/n[i]
                    n_rej_max_l_CST[j] = n_rej_max_l/n[i]
                    n_rej_max_w_CST[j] = n_rej_max_w/n[i]
                    n_rej_intersec_CST[j] = n_rej_intersec/n[i]
                
        n_rej_max_wloc_min_PARSEC = 0
        n_rej_max_wloc_mean_PARSEC = 0
        n_rej_max_wloc_max_PARSEC = 0
        
        n_rej_max_u_min_PARSEC = 0
        n_rej_max_u_mean_PARSEC = 0
        n_rej_max_u_max_PARSEC = 0
        
        n_rej_max_l_min_PARSEC = 0
        n_rej_max_l_mean_PARSEC = 0
        n_rej_max_l_max_PARSEC = 0
        
        n_rej_max_w_min_PARSEC = 0
        n_rej_max_w_mean_PARSEC = 0
        n_rej_max_w_max_PARSEC = 0
        
        n_rej_intersec_min_PARSEC = 0
        n_rej_intersec_mean_PARSEC = 0
        n_rej_intersec_max_PARSEC = 0
        
        n_rej_max_wloc_min_CST = 0
        n_rej_max_wloc_mean_CST = 0
        n_rej_max_wloc_max_CST = 0
        
        n_rej_max_u_min_CST = 0
        n_rej_max_u_mean_CST = 0
        n_rej_max_u_max_CST = 0
        
        n_rej_max_l_min_CST = 0
        n_rej_max_l_mean_CST = 0
        n_rej_max_l_max_CST = 0
        
        n_rej_max_w_min_CST = 0
        n_rej_max_w_mean_CST = 0
        n_rej_max_w_max_CST = 0
        
        n_rej_intersec_min_CST = 0
        n_rej_intersec_mean_CST = 0
        n_rej_intersec_max_CST = 0
        
        # # using the exec function to dynamically create variables based on the parametrization method being used
        # exec('n_rej_intersec_min_'+parametrization+' = np.min(n_rej_intersec_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('n_rej_intersec_mean_'+parametrization+' = np.mean(n_rej_intersec_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('n_rej_intersec_max_'+parametrization+' = np.max(n_rej_intersec_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('error_intersec_'+parametrization+'=n_rej_intersec_max_'+parametrization+'-n_rej_intersec_min_'+parametrization)
        
        # # using the exec function to dynamically create variables based on the parametrization method being used
        # exec('n_rej_max_w_min_'+parametrization+' = np.min(n_rej_max_w_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('n_rej_max_w_mean_'+parametrization+' = np.mean(n_rej_max_w_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('n_rej_max_w_max_'+parametrization+' = np.max(n_rej_max_w_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('error_max_w_'+parametrization+'=n_rej_max_w_max_'+parametrization+'-n_rej_max_w_min_'+parametrization)
        
        # # using the exec function to dynamically create variables based on the parametrization method being used
        # exec('n_rej_max_u_min_'+parametrization+' = np.min(n_rej_max_u_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('n_rej_max_u_mean_'+parametrization+' = np.mean(n_rej_max_u_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('n_rej_max_u_max_'+parametrization+' = np.max(n_rej_max_u_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('error_max_u_'+parametrization+'=n_rej_max_u_max_'+parametrization+'-n_rej_max_u_min_'+parametrization)
        
        # # using the exec function to dynamically create variables based on the parametrization method being used
        # exec('n_rej_max_l_min_'+parametrization+' = np.min(n_rej_max_l_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('n_rej_max_l_mean_'+parametrization+' = np.mean(n_rej_max_l_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('n_rej_max_l_max_'+parametrization+' = np.max(n_rej_max_l_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('error_max_l_'+parametrization+'=n_rej_max_l_max_'+parametrization+'-n_rej_max_l_min_'+parametrization)
    
        # # using the exec function to dynamically create variables based on the parametrization method being used
        # exec('n_rej_max_wloc_min_'+parametrization+' = np.min(n_rej_max_wloc_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('n_rej_max_wloc_mean_'+parametrization+' = np.mean(n_rej_max_wloc_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('n_rej_max_wloc_max_'+parametrization+' = np.max(n_rej_max_wloc_'+parametrization+',axis=0)') # calculate the ratio of designs that are accepted to the inital number of designs
        # exec('error_max_wloc_'+parametrization+'=n_rej_max_wloc_max_'+parametrization+'-n_rej_max_wloc_min_'+parametrization)
        
        # using the exec function to dynamically create variables based on the parametrization method being used
        n_rej_intersec_min_PARSEC = np.min(n_rej_intersec_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_intersec_mean_PARSEC = np.mean(n_rej_intersec_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_intersec_max_PARSEC = np.max(n_rej_intersec_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        error_intersec_PARSEC=n_rej_intersec_max_PARSEC-n_rej_intersec_min_PARSEC
        
        # using the exec function to dynamically create variables based on the parametrization method being used
        n_rej_max_w_min_PARSEC = np.min(n_rej_max_w_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_w_mean_PARSEC = np.mean(n_rej_max_w_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_w_max_PARSEC = np.max(n_rej_max_w_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        error_max_w_PARSEC=n_rej_max_w_max_PARSEC-n_rej_max_w_min_PARSEC
        
        # using the exec function to dynamically create variables based on the parametrization method being used
        n_rej_max_u_min_PARSEC = np.min(n_rej_max_u_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_u_mean_PARSEC = np.mean(n_rej_max_u_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_u_max_PARSEC = np.max(n_rej_max_u_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        error_max_u_PARSEC=n_rej_max_u_max_PARSEC-n_rej_max_u_min_PARSEC
        
        # using the exec function to dynamically create variables based on the parametrization method being used
        n_rej_max_l_min_PARSEC = np.min(n_rej_max_l_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_l_mean_PARSEC = np.mean(n_rej_max_l_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_l_max_PARSEC = np.max(n_rej_max_l_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        error_max_l_PARSEC=n_rej_max_l_max_PARSEC-n_rej_max_l_min_PARSEC
    
        # using the exec function to dynamically create variables based on the parametrization method being used
        n_rej_max_wloc_min_PARSEC = np.min(n_rej_max_wloc_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_wloc_mean_PARSEC = np.mean(n_rej_max_wloc_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_wloc_max_PARSEC = np.max(n_rej_max_wloc_PARSEC,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        error_max_wloc_PARSEC=n_rej_max_wloc_max_PARSEC-n_rej_max_wloc_min_PARSEC
        
        ###########
        # using the exec function to dynamically create variables based on the parametrization method being used
        n_rej_intersec_min_CST = np.min(n_rej_intersec_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_intersec_mean_CST = np.mean(n_rej_intersec_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_intersec_max_CST = np.max(n_rej_intersec_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        error_intersec_CST=n_rej_intersec_max_CST-n_rej_intersec_min_CST
        
        # using the exec function to dynamically create variables based on the parametrization method being used
        n_rej_max_w_min_CST = np.min(n_rej_max_w_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_w_mean_CST = np.mean(n_rej_max_w_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_w_max_CST = np.max(n_rej_max_w_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        error_max_w_CST=n_rej_max_w_max_CST-n_rej_max_w_min_CST
        
        # using the exec function to dynamically create variables based on the parametrization method being used
        n_rej_max_u_min_CST = np.min(n_rej_max_u_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_u_mean_CST = np.mean(n_rej_max_u_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_u_max_CST = np.max(n_rej_max_u_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        error_max_u_CST=n_rej_max_u_max_CST-n_rej_max_u_min_CST
        
        # using the exec function to dynamically create variables based on the parametrization method being used
        n_rej_max_l_min_CST = np.min(n_rej_max_l_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_l_mean_CST = np.mean(n_rej_max_l_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_l_max_CST = np.max(n_rej_max_l_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        error_max_l_CST=n_rej_max_l_max_CST-n_rej_max_l_min_CST
    
        # using the exec function to dynamically create variables based on the parametrization method being used
        n_rej_max_wloc_min_CST = np.min(n_rej_max_wloc_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_wloc_mean_CST = np.mean(n_rej_max_wloc_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        n_rej_max_wloc_max_CST = np.max(n_rej_max_wloc_CST,axis=0) # calculate the ratio of designs that are accepted to the inital number of designs
        error_max_wloc_CST=n_rej_max_wloc_max_CST-n_rej_max_wloc_min_CST
        
        #------------------------------------------------------------------------------
        # Plot design space stats
        #------------------------------------------------------------------------------
        labels = ['Surface \n Intersection','abs(yu/c) \n > 0.3', 'abs(yl/c) \n > 0.3', 'max(t) \n > 0.4', 'x/c at max(t) \n > 0.5']
        
        n_rej_mean_PARSEC = [n_rej_intersec_mean_PARSEC, n_rej_max_w_mean_PARSEC, n_rej_max_u_mean_PARSEC, n_rej_max_l_mean_PARSEC,n_rej_max_wloc_mean_PARSEC]
        n_rej_mean_CST = [n_rej_intersec_mean_CST, n_rej_max_w_mean_CST, n_rej_max_u_mean_CST, n_rej_max_l_mean_CST,n_rej_max_wloc_mean_CST]
        
        x = np.arange(len(labels))  # the label locations
        width = 0.35  # the width of the bars
        
        fig, ax = plt.subplots(figsize=(6,9),dpi=(2**8))
        rects1 = ax.bar(x - width/2, n_rej_mean_PARSEC, width, label='PARSEC')
        rects2 = ax.bar(x + width/2, n_rej_mean_CST, label='CST')
        
         #Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Ratio of Rejected Samples')
        ax.set_xlabel('Reason for Rejection')
        ax.set_title('LHS Design Space Comparison')
        ax.set_xticks(x, labels)
        ax.legend()
        ax.set_ylim(0, 1.1)
        #fig.tight_layout()
        plt.savefig('LHS Design Space Rejected Samples and Cause for N = %i' %(n[i]),dpi=(2**8))        
    
    return
