import numpy as np
import matplotlib.pyplot as plt
import random
import os
import shutil
import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt

def visualization(xu,zu,xl,zl,parametrization):
    
    #--------------------------------------------------------------------------
    # input processing
    #--------------------------------------------------------------------------
    N,n = zu.shape
    #--------------------------------------------------------------------------
    # Plotting upper, lower, and mean surface bounds
    #--------------------------------------------------------------------------
    zu_max = np.zeros(N) # initialize an array of zeros for the maximum coord of the upper surface
    zl_min = np.zeros(N) # initialize an array of zeros for the minimum coord of the lower surface
    zu_mean = np.zeros(N) # initialize an array of zeros for the mean coord of the upper surface
    zl_mean = np.zeros(N) # initialize an array of zeros for the mean coord of the lower surface
    
    # for loop to cycle through each upper and lower surface point and store information to intialized arrrays
    for i in range(N):
        zu_max[i] = max(zu[i,:]) # stores max upper surface coord at a given x point for all airfoils
        zl_min[i] = min(zl[i,:]) # stores min lower surface coord at a given x point for all airfoils
        zu_mean[i] = stat.mean(zu[i,:]) # stores mean upper surface coord at a given x point for all airfoils
        zl_mean[i] = stat.mean(zl[i,:]) # stores mean lower surface coord at a given x point for all airfoils
        
    fig = plt.figure(figsize=(6,9),dpi=(2**8))
    for i in range(n):
        plt.plot(xu[:,i],zu[:,i],color='blue',linewidth=0.2) # plotting current sample's upper surface
        plt.plot(xl[:,i],zl[:,i],color='blue',linewidth=0.2) # plottingcurrent sample's lower surface
    # plt.plot(xu[:,0],zu_max,color='red',marker='^',markersize=0.5,linewidth=0.5,label='Upper Surface Bound') # plotting current sample's maximum upper surface
    # plt.plot(xl[:,0],zl_min,color='red',marker='v',markersize=0.5,linewidth=0.5,label='Lower Surface Bound') # plotting current sample's minimum lower surface
    plt.plot(xu[:,0],zu_max,color='red',linewidth=0.5,label='Design Space Outer Bound') # plotting current sample's maximum upper surface
    plt.plot(xl[:,0],zl_min,color='red',linewidth=0.5) # plotting current sample's minimum lower surface
    # plt.plot(xu[:,0],zu_mean,color='orange',marker='^',markersize=0.5,linewidth=0.5,label='Upper Surface Mean') # plotting current sample's mean upper surface
    # plt.plot(xl[:,0],zl_mean,color='orange',marker='v',markersize=0.5,linewidth=0.5,label='Lower Surface Surface') # plotting current sample's mean lower surface
    plt.plot(xu[:,0],zu_mean,color='orange',linewidth=0.5,label='Design Space Mean') # plotting current sample's mean upper surface
    plt.plot(xl[:,0],zl_mean,color='orange',linewidth=0.5) # plotting current sample's mean lower surface
    # plot settings
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x/c')
    plt.ylabel('y/c')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),shadow=False)
    plt.title('%s Design Space Overlay'%(parametrization))
    
    #--------------------------------------------------------------------------
    # plotting a representative sample grid of airfoils
    #--------------------------------------------------------------------------
    # plotting a representative grid of airfoils
    rows = 6 # number of rows in the subplot grid
    cols = 6 # number of columns in the subplot grid
    nsubplots = rows*cols # total number of representative samples to plot
    
    # randomly choosing nsubplot airfoils to plot
    chosen = random.sample(range(n),nsubplots)
    
    # plotting
    i = 0 # setting iteration counter to 0
    fig, ax = plt.subplots(rows, cols, dpi=(2**8)) # specifying rows, columns, and image quality of the subplots
    fig.tight_layout() # specifying tight layout of subplots
    plt.suptitle('%s Design Space Airfoil Samples' %(parametrization)) # Writing SUPtitle (main title)
    # for loop to iterate through rows, columns, and numsubplots to populate subplot grid
    for row in range(rows):
        for col in range(cols):
            ax[row,col].plot(xu,zu[:,chosen[i]],color='blue',linewidth=0.7) # plotting current sample's upper surface
            ax[row,col].plot(xl,zl[:,chosen[i]],color='blue',linewidth=0.7) # plottingcurrent sample's lower surface
            ax[row,col].set_aspect('equal', 'box') # setting sunplot aspect ratio to equal
            ax[row,col].axis('off') # turning axis/grid off for aethetic purposes
            i = i + 1 # increasing iteration counter by 1 to populate the next grid location with the next chosen sample
    plt.subplots_adjust(wspace = 0, hspace = 0) # set vertical and horizontal spacing between subplot to 0
    plt.show()
    
    return