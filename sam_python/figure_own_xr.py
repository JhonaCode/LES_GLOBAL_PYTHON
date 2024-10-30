import  numpy as np

import  matplotlib.pyplot as plt

#Color map
from    matplotlib.colors import LinearSegmentedColormap

from matplotlib.ticker import (MultipleLocator, LinearLocator,NullFormatter,
                                   ScalarFormatter)


#To work with date in plots 
import  matplotlib.dates as mdates

import  matplotlib as mpl

from datetime import datetime, timedelta

import  sam_python.data_own as down

#Filter the function, more smothy
from scipy.signal import lfilter

import scipy.ndimage as ndimage

import subprocess, sys

import importlib

import xarray as xr

import  sam_python.plotparameters      as pp

#to cp the parametres defaul 
subprocess.run('cp Parameters_default.py /pesq/dados/bamc/jhonatan.aguirre/git_repositories/MAPS_python/sam_python/', shell = True, executable="/bin/bash")

#used the user parameter to plot(plotparameter.py) if para:
#pars=__import__('source.Parameters_default',globals())
pars=importlib.import_module('.Parameters_default','sam_python',)


#Color map
#########
#cmap = LinearSegmentedColormap.from_list('mycmap', ['skyblue','blue','navy','steelblue','lightskyblue','white'])
cmap = LinearSegmentedColormap.from_list('mycmap', ['white','lightblue','skyblue','RoyalBlue','blue','darkblue'])
cmap3 = LinearSegmentedColormap.from_list('mycmap', ['white','silver','blue','green','yellow'], N=256, gamma=0.5)
cmap4 = LinearSegmentedColormap.from_list('mycmap', ['white','grey','lightblue','blue','green','yellow'], N=256, gamma=1.0)


def d2_plot_im_diff(var,z,alt,contour,colors,explabel,leg_loc,hours=[]):

    #Data to plot 
    #used user parameter to plot(plotparameter.py
    #mpl.rcParams.update(params_2d)

    size_wg = leg_loc[5][0]
    size_hf = leg_loc[5][1]

    pp.plotsize(size_wg,size_hf, 0.0,'2d')

    ################################3
    fig = plt.figure()
    ###New axis
    ax  = plt.axes()

    try:
        x       =  var.Time[:]
    except:
        x       =  var.time[:].values

    sx= x.shape[0]
    sy= z.shape[0]

    #x=np.zeros(sx)
    y=np.zeros(sy)
    MF=np.zeros((sx,sy))
    
    # with the data and no time

    y       =   z[:]/1000.0

    #Variable to plot
    MF      =   var.values 

    if colors=='cloud':
        colors=cmap

    if colors=='whbuyl':
        colors=cmap3


    X,Y= np.meshgrid(x,y)

    levels= np.linspace(contour[0],contour[1],contour[2],endpoint=True)

    Z = ndimage.gaussian_filter(MF.T, sigma=1.0, order=0)

    #CU=ax.contourf(X,Y,MF.T,levels=levels, interpolation='bilinear',origin='lower',cmap=colors,aspect='auto',extend='both');
    CU=ax.contourf(X,Y,Z,levels=levels,origin='lower',cmap=colors);

    # Set all level lines to black
    #line_colors = ['black' for l in CU.levels]
    line_colors = ['darkgrey' for l in CU.levels]

    #Contour plot 
    CS=plt.contour(X,Y,Z,levels=levels[1:len(levels):2],colors=line_colors,linewidths=0.1 );

    #plot_bar
    if(leg_loc[2][1]):

        CB = fig.colorbar(CU, shrink=1.0, extend='neither',orientation=leg_loc[2][0])

        if(contour[0]>contour[1]):

            kk= np.linspace(contour[0],0,11,endpoint=True,)
            cbarlabels=kk

        elif(contour[0]<0):

            cbarlabels = np.linspace(contour[0],contour[1] ,contour[2],endpoint=True)
            #cbarlabels=cbarlabels[1::]-contour[0]
            CB.set_ticks(cbarlabels[0::2])

        else:
            cbarlabels = np.linspace(contour[0],contour[1],contour[2],endpoint=True)

            CB.set_ticks(cbarlabels[0::2])


        #CB.set_ticks(cbarlabels[1::4])
        CB.ax.set_title(r'%s'%leg_loc[2][2])


    ax.xaxis_date()

    date_form = mdates.DateFormatter("%H" )
    ax.xaxis.set_major_formatter(date_form)

    locatormax = mdates.HourLocator(interval=2)
    locatormin = mdates.HourLocator(interval=1)
    ax.xaxis.set_minor_locator(locatormin)
    ax.xaxis.set_major_locator(locatormax)


    if hours:
        ax.set_xlim([hours[0],hours[1]])

    ax.set_ylim([alt[0],alt[1]])
    ax.yaxis.set_major_locator(plt.MultipleLocator(2.0))

    ax=label_plots(x,ax,leg_loc,explabel[1],explabel[2])

    plt.savefig('%s/vertical_2d_%s.pdf'%(pars.out_fig,explabel[0]),bbox_inches='tight',dpi=200, format='pdf')

    return fig,ax    

def label_plots(time,ax,legend,explabel1,explabel2): 

    #leg_loc      =  ( [ 0.5,4.2],[ 0.5,4.2],[vertical,True],[xlabel,'True'],[ylabel,'True'],[size_wg,size_hf])

    xlabel=legend[3][0]

    ylabel=legend[4][0]

    ax.text(time[legend[0][0]], legend[0][1], r' %s'%(explabel1), fontsize=8, color='black')

    ax.text(time[legend[0][0]], legend[0][1], r' %s'%(explabel2), fontsize=8, color='black')

    if( legend[3][1]==True):
        plt.xlabel(r'%s'%(xlabel)) 

    if( legend[4][1]==True):
        plt.ylabel(r'%s'%(ylabel)) 

    return ax
