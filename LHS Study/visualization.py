import numpy as np
import matplotlib.pyplot as plt
import random
import os
import shutil
import pandas as pd
import statistics as stat
import matplotlib.pyplot as plt

def visualization(x_u,zu,x_l,zl,parametrization):
    
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
        plt.plot(x_u,zu[:,i],'b',linewidth=0.7) # plotting current sample's upper surface
        plt.plot(x_l,zl[:,i],'b',linewidth=0.7) # plottingcurrent sample's lower surface
    plt.plot(x_u,zu_max,color='red',marker='^',markersize=1.5,linewidth=0.7,label='Upper Surface Bound') # plotting current sample's maximum upper surface
    plt.plot(x_l,zl_min,color='red',marker='v',markersize=1.5,linewidth=0.7,label='Lower Surface Bound') # plotting current sample's minimum lower surface
    plt.plot(x_u,zu_mean,color='orange',marker='^',markersize=1.5,linewidth=0.7,label='Upper Surface Mean') # plotting current sample's mean upper surface
    plt.plot(x_l,zl_mean,color='orange',marker='v',markersize=1.5,linewidth=0.7,label='Lower Surface Surface') # plotting current sample's mean lower surface
    # plot settings
    plt.grid()
    plt.gca().set_aspect('equal', adjustable='box')
    plt.xlabel('x/c')
    plt.ylabel('y/c')
    plt.legend(loc='center left', bbox_to_anchor=(1, 0.5),shadow=False)
    plt.title('%s Design Space with n_feas = %i'%(parametrization,n))
    plt.savefig(parametrization + ' Data/' + '%s Design Space with n_feas = %i'%(parametrization,n)+'.png',dpi=(2**8))
    
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
    plt.suptitle('Sample of %d out of %d Feasible %s Airfoils' %(nsubplots,n,parametrization)) # Writing SUPtitle (main title)
    # for loop to iterate through rows, columns, and numsubplots to populate subplot grid
    for row in range(rows):
        for col in range(cols):
            ax[row,col].plot(x_u,zu[:,chosen[i]],'b',linewidth=0.7) # plotting current sample's upper surface
            ax[row,col].plot(x_l,zl[:,chosen[i]],'b',linewidth=0.7) # plottingcurrent sample's lower surface
            ax[row,col].set_aspect('equal', 'box') # setting sunplot aspect ratio to equal
            ax[row,col].axis('off') # turning axis/grid off for aethetic purposes
            i = i + 1 # increasing iteration counter by 1 to populate the next grid location with the next chosen sample
    plt.subplots_adjust(wspace = 0, hspace = 0) # set vertical and horizontal spacing between subplot to 0
    plt.show()
    fig.savefig(parametrization + ' Data/' + 'Sample of %d out of %d Feasible %s Airfoils' %(nsubplots,n,parametrization)+'.png',dpi=(2**8))
    
    # #--------------------------------------------------------------------------
    # # processing surfaces to convert it a ICEM accepted format
    # #--------------------------------------------------------------------------
    # # flip zu and combine with zl with first column deleted to convert to selig format
    # # combining zu and zl, and settting x = [x,x] to match and converting to Selig format
    # surfaces = np.concatenate((np.flip(zu,axis=1),np.delete(zl,0,axis=1)), axis=1) # combine the upper and lower surface (minus the first point) into a (n,2*N-1) numpy array
    # x = np.reshape(x,(len(x),1)) # reshape x from (N,) to (N,1)
    # x = np.concatenate((np.flip(x),np.delete(x,0,axis=0)), axis=0) # flip x and combine with x with first column deleted to convert to selig format
    
    # # -------------------------------------------------------------------------
    # # plotting and saving airfoil surfaces
    # # -------------------------------------------------------------------------
    # # create folder to save airfoil plots in
    # # use shutil to delete airfoil folder if exists to avoid overlap of data
    # shutil.rmtree(parametrization + ' Data/' + 'Airfoil Plots', ignore_errors=True)
    # # make a new directory for the airfoils and allow for a new directory even if there is already one with the same name
    # os.makedirs(parametrization + ' Data/' + 'Airfoil Plots', exist_ok=True)
    
    # # use shutil to delete airfoil folder if exists to avoid overlap of data
    # shutil.rmtree(parametrization + ' Data/' + 'Airfoils', ignore_errors=True)
    # # make a new directory for the airfoils and allow for a new directory even if there is already one with the same name
    # os.makedirs(parametrization + ' Data/' + 'Airfoils', exist_ok=True)
    
    # # for loop to store each row of airfoil surfaces from surface as a unique variable
    # for i in range(len(surfaces)):
    #     y = surfaces[i,:] # define y as one surface
    #     y = np.reshape(y,(len(y),1)) # reshape y from (len(y),) to (len(y),1)
    #     npairfoil = np.insert(y,0,np.transpose(x),axis=1) # define npairfoil as an array containing both x and y values
    #     airfoil = pd.DataFrame(npairfoil) # convert npairfoil arrray into a panda dataframe for easier saving
    #     new_row = pd.DataFrame({'X':'\t'+'airfoil %s'%i}, index =[0])# add the airfoil name as the top row, reset the dataframe index, and drop the old one
    #     airfoil = pd.concat([new_row, airfoil]).reset_index(drop=True)
    #     airfoil.to_csv(parametrization + ' Data/Airfoils/'+'airfoil%s'%i+'.dat',sep='\t',index=False,header=False) # save dataframe to a .dat file of the same name in the new directory, with a tab delimiter, and without the index, or column names
        
    #     # plotting
    #     fig = plt.figure(figsize=(6,9),dpi=(2**8))
    #     plt.plot(airfoil[0],airfoil[1],'b',linewidth=0.7)
    #     plt.gca().set_aspect('equal', adjustable='box')
    #     plt.title('Airfoil No.%d' %i)
    #     plt.xlabel('x/c')
    #     plt.ylabel('y/c')
    #     plt.savefig(parametrization + ' Data/Airfoil Plots/'+'airfoil%s'%i+'.png',dpi=(2**8))
    return
