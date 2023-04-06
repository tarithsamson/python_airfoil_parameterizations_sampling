import numpy as np
import sys
import matplotlib.pyplot as plt
import random
import os
import shutil
import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt

def postProcess(xu,zu,xl,zl,X,parametrization):

    #--------------------------------------------------------------------------
    # Input processing
    #--------------------------------------------------------------------------
    N,n = zu.shape
    #--------------------------------------------------------------------------
    # Defining parameters
    #--------------------------------------------------------------------------
    max_u = 0.3
    max_l = 0.3
    max_w = 0.4
    max_max_w_loc = 0.5
    
    #--------------------------------------------------------------------------
    # Initializing Variables
    #--------------------------------------------------------------------------
    n_rej = 0 # initial number of rejected airfoils is 0
    n_rej_max_w_loc = 0
    n_rej_max_u = 0
    n_rej_max_l = 0
    n_rej_max_w = 0
    n_rej_intersec = 0
    
    #--------------------------------------------------------------------------
    # Surface feasibility check
    #--------------------------------------------------------------------------
    label = np.zeros(n) #create an array of n zeros 
     
    w = zu - zl
    max_w_loc = np.argmax(w,axis=0)
    
    for i in range(n): # for-loop to compare corresponding upper and lower surface coordinate for current surface
        for j in range(N):
            #print('zu[%i,%i]=%.30f'%(j,i,zu[j,i]))
            #print('zl[%i,%i]=%.30f'%(j,i,zu[j,i]))
            if zu[j,i]<zl[j,i]: # intersection check 
                label[i] = 1 # change upper surface label to bad (0)
                n_rej_intersec += 1
                #n_rej += 1 # update the number of rejected airfoils
                #print('intersection violated. Breaking')
                break # stop checking surface coords
            if xl[max_w_loc[i]] > max_max_w_loc:
                #label[i] = 1 # change upper surface label to bad (0)
                n_rej_max_w_loc += 1
                #n_rej += 1 # update the number of rejected airfoils
                #print('maxu violated. Breaking')
                break # stop checking surface coords
            if(abs(zu[j,i])>max_u): # max zu check
                #label[i] = 1 # change upper surface label to bad (0)
                n_rej_max_u += 1
                #n_rej += 1 # update the number of rejected airfoils
                #print('maxu violated. Breaking')
                break # stop checking surface coords
            if(abs(zl[j,i])>max_l): # max zl check
                #label[i] = 1 # change upper surface label to bad (0)
                n_rej_max_l += 1
                #n_rej += 1 # update the number of rejected airfoils
                #print('maxl violated. Breaking')
                break # stop checking surface coords         
            if(abs(zu[j,i]-zl[j,i])>max_w): # max width check
                #label[i] = 1 # change upper surface label to bad (0)
                n_rej_max_w += 1
                #n_rej += 1 # update the number of rejected airfoils
                #print('max_w violated. Breaking')
                break # stop checking surface coords
            # # #if (zu[i,j] < zl[i,j]): # lax filters
            else:
                pass # do nothing to label if current point on current surface is good (1)
    #print(label)
    #--------------------------------------------------------------------------
    # Surface and LHS filtering method 1
    #--------------------------------------------------------------------------
    i = n-1
    while (i>=0):
        if (label[i] == 1):
            zu = np.delete(zu,[i],axis=1)
            zl = np.delete(zl,[i],axis=1)
            X = np.delete(X,[i],axis=1)
            # if a surface is labelled as bad, delete it, delete the sample from the LHS vector, and don't change the iteration counter
        else:
            pass# if a surface is labelled as good, update the iteration counter to check the next one
        i = i - 1
        
    #--------------------------------------------------------------------------
    # Curvature Calculation
    #--------------------------------------------------------------------------
    #for i in range(1,N-1):
        #print(zu.shape)
        

            
    return xu,zu,xl,zl,X,n_rej_max_w_loc,n_rej_max_u,n_rej_max_l,n_rej_max_w,n_rej_intersec