import  numpy as np

import  matplotlib.pyplot as plt

#Color map
from    matplotlib.colors import LinearSegmentedColormap

from matplotlib.ticker import (MultipleLocator, LinearLocator,NullFormatter,
                                   ScalarFormatter)
import matplotlib.ticker as tkr


#To work with date in plots 
import  matplotlib.dates as mdates

import  matplotlib as mpl

from datetime import datetime, timedelta

import datetime as dt

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

    size_wg = leg_loc[6][0]
    size_hf = leg_loc[6][1]
    cmas    = leg_loc[6][2]

    tama= pp.plotsize(size_wg,size_hf, cmas,pars.plotdef)


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
    CU=plt.contourf(X,Y,MF.T,levels=levels,origin='lower',cmap=colors,extend='neither');
    #CU=ax.contourf(X,Y,Z,levels=levels,origin='lower',cmap=colors);

    #plt.grid(color = 'gray', linestyle = '--', linewidth = 0.25)
    #plt.grid(color = 'gray', linestyle = '--', linewidth = 0.25)
    plt.grid(color = 'gray',linewidth=0.5,alpha=0.5,dashes=[1,1,0,0] )

    # Set all level lines to black
    #line_colors = ['black' for l in CU.levels]
    line_colors = ['darkgrey' for l in CU.levels]

    #Contour plot 
    CS=ax.contour(X,Y,MF.T,levels=levels[1:len(levels):2],colors=line_colors,linewidths=0.1 );

    #plot_bar
    if(leg_loc[2][1]):

        #CB = plt.colorbar()
        CB = fig.colorbar(CU, shrink=1.0, extend='neither',orientation=leg_loc[2][0], format=tkr.FormatStrFormatter('%.2f'))


        CB.ax.tick_params(labelsize=tama) 


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

        #CB.set_ticks(cbarlabels[0::3])
        CB.ax.set_title(r' %s'%leg_loc[2][2],size=tama-1)


    #plot_bar
    #if(axis_on[3]):
    #fig,ax=base_top_cloud(fig,ax,var)

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
    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))

    ax=label_plots(x,ax,leg_loc,explabel[1],explabel[2],tama)

    plt.savefig('%s/vertical_2d_%s.pdf'%(pars.out_fig,explabel[0]),bbox_inches='tight',dpi=200, format='pdf')

    return fig,ax    

def base_top_cloud(fig,ax,ex):

    size= ex.time.shape[0]
    tam = ex.MCUP.shape[0]

    #max heigh points
    #ex: resolution (50m)*30
    #for gomazon paper 
    #maxl=30

    #for arm paper 
    maxl=80

    ctop  =[]
    ctop2 =[]
    cbase =[]
    cbase2=[]
    pblh  =[]
    cmflx =[]

    for i in range(0,tam):

        index1  =  np.argmin(ex.TVFLUX[i][0:maxl].values)
        indexc  =  np.argmax(   ex.CLD[i][0:maxl].values)

        #for j in range(1,10):
        #for goamazon 
        #for j in range(1,5):
        for j in range(1,20):

            index2=index1+j

            if ex.TVFLUX[i][index2].values>0 and index1>3:

                indexmin=index2

                break

            else:
                    indexmin=index1

        #for gomazon paper
        #for i1 in range(0,70):
        for i1 in range(0,100):

             index3=indexmin+i1

             #paper goamazon
             #if ex.QC[i][index3]<0.001 :
             if ex.QC[i][index3].values<0.005 :

                 indexmax=index3

                 break
        #for i2 in range(0,70):

        #         index4=indexmin+i1

        #         if ex.CLD[i][index4]<0.001 :

        #             indexmax2=index4

        #             break

        #for i1 in range(0,70):

        #    index3=indexmin+i1

        #    if ex.CLD[i][index3]<0.0005:

        #        indexmax=index3

        #        break

        ##for i1 in range(0,70):

        ##    index3=indexmin+i1

        ##    if ex.MCUP[i][index3]<0.001:

        ##        indexmax=index3

        ##        break



        pblh.append(ex.z[index1].values/1000.0)
        cbase.append(ex.z[indexmin].values/1000.0)
        cmflx.append(ex.MCUP[i,indexmin].values)
        cbase2.append(ex.z[indexc].values/1000.0)
        ctop.append(ex.z[indexmax].values/1000.0)

    step=1

    #Limits of time date
    #idi2     = datetime(ex.datei.year,ex.datei.month,ex.datei.day,10)#dt.datetime(2014, days[2] ,days[0], 10)
    #idf2     = datetime(ex.datef.year,ex.datef.month,ex.datef.day,18)#dt.datetime(2014, days[2] ,days[0], 10)
    ##idf2     = ex.datef#dt.datetime(2014, days[3] ,days[0], 18)
    date_format = '%Y-%m-%dT%H'
    idi2=dt.datetime.strptime('2025-01-01T10', date_format)
    idf2=dt.datetime.strptime('2025-01-01T17', date_format)
    time1 = np.datetime64(idi2) 
    time2 = np.datetime64(idf2) 

    ni2,nf2= down.data_n(time1,time2,ex.time[:].values)

    # To find 13 and 14 hours
    #i13     = datetime(ex.datef.year,ex.datef.month,ex.datef.day,13)#dt.datetime(2014, days[2] ,days[0], 10)
    #i14     = datetime(ex.datef.year,ex.datef.month,ex.datef.day,14)#dt.datetime(2014, days[2] ,days[0], 10)
    i13=dt.datetime.strptime('2025-01-01T13', date_format)
    i14=dt.datetime.strptime('2025-01-01T14', date_format)
    i3 = np.datetime64(i13) 
    i4 = np.datetime64(i14) 

    n13,n14= down.data_n(i3,i4,ex.time[:].values)


    #TO find the cloud fraction max
    cbi    =np.argmax(cbase)
    cbmax   =cbase[cbi]
    cbmax14 =cbase[n14]

    #TO find the mass flux max
    mfi   =np.argmax(cmflx)
    mfmax =cmflx[mfi]
    cbmf  =cbase[mfi]

    #Tree ways to calculate the max 
    #topmax=np.max(ctop)

    top_cb  =ctop[cbi]
    top_14  =ctop[n14]
    top_mf  =ctop[mfi]

    print(ex.time[mfi],'mfmax')
    print(ex.time[cbi],'cbmax')
    #print(ex.date[n14],'14')


    #############
    print('######')
    print('CB base='   ,cbmax)
    print('CB base 14=',cbmax14)
    print('MF base='   ,cbmf)

    #############
    print('######')
    print('CB top='   ,top_cb)
    print('CB top 14=',top_14)
    print('MF top='   ,top_mf)

    #############
    print('######')
    print('CB    Deep=',top_cb-cbmax)
    print('CB 14 Deep=',top_14-cbmax14)
    print('MF Deep=',top_mf-cbmf)
    

    n = 3#nf2-ni2  # the larger n is, the smoother curve will be
    b = [1.0 / n] * n
    a = 1


    cbasef = lfilter(b, a, cbase)

    pblhf = lfilter(b, a, pblh)

    ctopf = lfilter(b, a, ctop)

    ax.plot( ex.time[ni2:nf2:step]     , cbasef[ni2:nf2:step] ,color='fuchsia' ,dashes=[1,0]  ,linewidth=1.0,alpha=1.0,marker='')

    ax.plot( ex.time[ni2:nf2:step]     , pblhf[ni2:nf2:step]  ,color='navy'     ,linewidth=1.0,alpha=1.0,marker='')

    ax.plot( ex.time[ni2:nf2:step]     , ctopf[ni2:nf2:step]  ,color='black' ,  dashes=[1,0]  ,linewidth=1.0,alpha=1.0,marker='')

    ax.plot( ex.time[ni2:nf2:step]     , cbase2[ni2:nf2:step]  ,color='lime' ,  dashes=[1,0]  ,linewidth=1.0,alpha=1.0,marker='')


    ytex,ytex2= down.data_n(time1,time2,ex.time[:].values)

    text1   ='$\mathrm{h_{b}}$'
    idtex1  = idf2-timedelta(hours=2, minutes=30)
    ax.text(idtex1, pblhf[ytex2]+0.2 , r' %s'%(text1), fontsize=7, color='fuchsia')

    text2='$\mathrm{Z_i}$'
    idtex1    = idf2-timedelta(hours=0, minutes=0)
    ax.text(idtex1,pblhf[ytex2] -0.1 , r' %s'%(text2), fontsize=6, color='navy')

    text1='LFC'
    #text1='NCL'
    idtex2    = idf2-timedelta(hours=0, minutes=0)
    ax.text(idtex2,cbasef[ytex2]+0.0 , r' %s'%(text1), fontsize=6, color='lime')

    text3='$\mathrm{h_{t}}$'
    #text3='$\mathrm{h_{topo}}$'
    idtex3    = idf2-timedelta(hours=0, minutes=00)
    ax.text(idtex3,ctopf[ytex2]+0.2 , r' %s'%(text3), fontsize=7, color='black')

    #if ex.name=='m_w_l' or  ex.name=='large':
    #    ax.text(idtex3,ctopf[ytex2]-0.4 , r' %s'%(text3), fontsize=7, color='black')
    #else :

    return fig,ax

def label_plots(time,ax,legend,explabel1,explabel2,tama): 

    #leg_loc      =  ( [ 0.5,4.2],[ 0.5,4.2],[vertical,True],[xlabel,'True'],[ylabel,'True'],[size_wg,size_hf])

    xlabel=legend[3][0]

    ylabel=legend[4][0]

    ax.text(time[legend[0][0]], legend[0][1], r' %s'%(explabel1), fontsize=tama, color='black')

    if  legend[1]:

        ax.text(time[legend[1][0]], legend[1][1], r' %s'%(explabel2), fontsize=tama, color='black')

    if( legend[3][1]==True):
        plt.xlabel(r'%s'%(xlabel), fontsize=tama) 

    if( legend[4][1]==True):
        plt.ylabel(r'%s'%(ylabel), fontsize=tama) 



    return ax
