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

import  sam_python.plotparameters as pn 

#Filter the function, more smothy
from scipy.signal import lfilter

import scipy.ndimage as ndimage


# To change the plot parameter 
#from   sam_python  import  plotparameters_new as pn

#Color map
#########
#cmap = LinearSegmentedColormap.from_list('mycmap', ['skyblue','blue','navy','steelblue','lightskyblue','white'])
cmap = LinearSegmentedColormap.from_list('mycmap', ['white','lightblue','skyblue','RoyalBlue','blue','darkblue'])
cmap3 = LinearSegmentedColormap.from_list('mycmap', ['white','silver','blue','green','yellow'], N=256, gamma=0.5)
cmap4 = LinearSegmentedColormap.from_list('mycmap', ['white','grey','lightblue','blue','green','yellow'], N=256, gamma=1.0)

def d2_plot_wind(ex,x,y,var1,var2,contour,xlim,ylim,label,origin,colors,axis_on,leg_loc):

    #Data to plot 
    #mpl.rcParams.update(params_2d)

    wf=axis_on[4]
    hf=1.0
    cmmais=axis_on[5]
    #plot size of the figures
    pn.plotsize(wf,hf,cmmais,'2d')

    ################################3
    fig = plt.figure()
    ###New axis
    ax  = plt.axes()

    if colors=='cloud':
        colors=cmap

    if colors=='whbuyl':
        colors=cmap3

    #Variable to plot
    #MF      =   np.sqrt(var1[:]**2+var2[:]**2)
    MF      =  var1 

    X,Y= np.meshgrid(x,y)

    ###################33
    levels= np.linspace(contour[0],contour[1],contour[2],endpoint=True)

    CU=ax.contourf(Y,X,MF.T,levels=levels,origin='lower',cmap=colors,extend='both');

    line_colors = ['darkgrey' for l in CU.levels]
    ###################33
    #Contour plot 
    #CS=plt.contour(Y,X,MF.T,levels=levels[1:len(levels):2],colors=line_colors,linewidths=0.1 );


    width=0.005
    scale=100
    step=100

    qv = ax.quiver(x[::step], y[::step] ,var1[::step,::step], var2[::step,::step],color='black',scale=scale, width=width)#,headlength=0.05)

    #ax.quiverkey(qv, X=1.00, Y=1.10, U=100,label=r'100[kgkg$^{-1}$ms$^{-1}$Pa]', labelpos='E',fontproperties={'size':5})
    #ax.quiverkey(qv, X=1.05, Y=1.02, U=100,label=r'100', labelpos='E',fontproperties={'size':5}, labelsep=0.01)
    

    #plot_bar
    if(axis_on[0]):

        #CB = fig.colorbar(CU, shrink=1.0, extend='neither')
        CB = fig.colorbar(CU, shrink=1.0, extend='both')

        if(contour[0]>contour[1]):

            kk= np.linspace(contour[0],0,11,endpoint=True,)
            cbarlabels=kk

        elif(contour[0]<0):

            cbarlabels = np.linspace(contour[0],contour[1] ,contour[2],endpoint=True)
            #cbarlabels=cbarlabels[1::]-contour[0]
            CB.set_ticks(cbarlabels[0::4])
            #print(cbarlabels)
            #exit()

        else:
            cbarlabels = np.linspace(contour[0],contour[1],contour[2],endpoint=True)
            print(cbarlabels)
            #cbarlabels=cbarlabels[1::]-contour[0]
            #CB.set_ticks(cbarlabels[0::4])
            CB.set_ticks(cbarlabels[::4])
            print(cbarlabels)


        #CB.set_ticks(cbarlabels[1::4])
        CB.ax.set_title(r'%s'%contour[3])

    #formater=LinearLocator(10)
    #ax.xaxis.set_major_formatter(formater)
    #ax.yaxis.set_major_formatter(formater)

    #ax.zaxis.set_major_formatter('{x:.02f}')
    ax.xaxis.set_major_locator(MultipleLocator( xlim[2]))
    ax.yaxis.set_major_locator(MultipleLocator(ylim[2]))

    #ax.set_xlim(xlim[0], xlim[1])
    #ax.set_ylim(ylim[0], ylim[1])

    #ax.set_xticks([-180, -120, -60, 0, 60, 120, 180], crs=ccrs.PlateCarree())
    #ax.set_yticks([-78.5, -60, -25.5, 25.5, 60, 80], crs=ccrs.PlateCarree())

    if(leg_loc[0]):

        ax.text(leg_loc[1], leg_loc[2], r' %s'%(label), fontsize=7, color='black')

    return fig,ax    
def d2_plot_horizontal(ex,x,y,var,contour,xlim,ylim,label,origin,colors,axis_on,leg_loc):

    #Data to plot 
    #used user parameter to plot(plotparameter.py
    #mpl.rcParams.update(params_2d)

    wf=axis_on[4]
    hf=1.0
    cmmais=axis_on[5]

    #plot size of the figures
    #cmmais are the cm to put the cbbar  without modified the size of the fig 
    pn.plotsize(wf,hf,cmmais,'2d')

    ################################3
    fig = plt.figure()
    ###New axis
    ax  = plt.axes()

    sx= x.shape[0]
    sy= y.shape[0]
    
    MF=np.zeros((sy,sx))
    
    # with the data and no time
    #Variable to plot
    MF      =   var[:,:]

    if colors=='cloud':
        colors=cmap

    if colors=='whbuyl':
        colors=cmap3

    X,Y= np.meshgrid(x,y)

    levels= np.linspace(contour[0],contour[1],contour[2],endpoint=True)

    CU=ax.contourf(Y,X,MF.T,levels=levels,origin='lower',cmap=colors,extend='both');

    line_colors = ['darkgrey' for l in CU.levels]

    #Contour plot 
    CS=plt.contour(Y,X,MF.T,levels=levels[1:len(levels):2],colors=line_colors,linewidths=0.1 );


    #plot_bar
    if(axis_on[0]):

        CB = fig.colorbar(CU, shrink=1.0, extend='neither')

        if(contour[0]>contour[1]):

            kk= np.linspace(contour[0],0,11,endpoint=True,)
            cbarlabels=kk

        elif(contour[0]<0):

            cbarlabels = np.linspace(contour[0],contour[1] ,contour[2],endpoint=True)
            #cbarlabels=cbarlabels[1::]-contour[0]
            CB.set_ticks(cbarlabels[0::4])
            #print(cbarlabels)
            #exit()

        else:
            cbarlabels = np.linspace(contour[0],contour[1]+contour[0],contour[2],endpoint=True)
            cbarlabels=cbarlabels[1::]-contour[0]
            CB.set_ticks(cbarlabels[1::4])
            #print(cbarlabels)


        #CB.set_ticks(cbarlabels[1::4])
        CB.ax.set_title(r'%s'%contour[3])

    #formater=LinearLocator(10)
    #ax.xaxis.set_major_formatter(formater)
    #ax.yaxis.set_major_formatter(formater)

    #ax.zaxis.set_major_formatter('{x:.02f}')
    ax.xaxis.set_major_locator(MultipleLocator( xlim[2]))
    ax.yaxis.set_major_locator(MultipleLocator(ylim[2]))


    ax.set_xlim(xlim[0], xlim[1])
    ax.set_ylim(ylim[0], ylim[1])

    #ax.set_xticks([-180, -120, -60, 0, 60, 120, 180], crs=ccrs.PlateCarree())
    #ax.set_yticks([-78.5, -60, -25.5, 25.5, 60, 80], crs=ccrs.PlateCarree())

    if(leg_loc[0]):

        ax.text(leg_loc[1], leg_loc[2], r' %s'%(label), fontsize=7, color='black')

    return fig,ax    

def d2_plot_im_diff(ex,time,z,var,contour,label,origin,colors,axis_on):

    #Data to plot 
    #used user parameter to plot(plotparameter.py
    #mpl.rcParams.update(params_2d)

    wf=axis_on[4]
    hf=1.0
    cmmais=axis_on[5]

    #plot size of the figures
    #cmmais are the cm to put the cbbar  without modified the size of the fig 
    pn.plotsize(wf,hf,cmmais,'2d')

    ################################3
    fig = plt.figure()
    ###New axis
    ax  = plt.axes()

    sx= time.shape[0]
    sy= z.shape[0]
    
    x=np.zeros(sx)
    y=np.zeros(sy)
    MF=np.zeros((sx,sy))
    
    # with the data and no time
    x       =   time[:]
    y       =   z[:]
    #Variable to plot
    MF      =   var[:,:]


    if colors=='cloud':
        colors=cmap

    if colors=='whbuyl':
        colors=cmap3

    X,Y= np.meshgrid(x,y)

    levels= np.linspace(contour[0],contour[1],contour[2],endpoint=True)

    Z = ndimage.gaussian_filter(MF.T, sigma=1.0, order=0)


    #CU=ax.contourf(X,Y,MF.T,levels=levels, interpolation='bilinear',origin='lower',cmap=colors,aspect='auto',extend='both');
    CU=ax.contourf(X,Y,Z,levels=levels,origin='lower',cmap=colors);


    #CU=ax.imshow(MF.T, interpolation='bilinear',origin='lower',cmap=colors,aspect='auto');

    # Set all level lines to black
    #line_colors = ['black' for l in CU.levels]
    line_colors = ['darkgrey' for l in CU.levels]

    #Contour plot 
    CS=plt.contour(X,Y,Z,levels=levels[1:len(levels):2],colors=line_colors,linewidths=0.1 );


    #plot_bar
    if(axis_on[3]):

        fig,ax=base_top_cloud(fig,ax,ex)

    #cbarlabels = np.linspace(contour[0],contour[1]+contour[0],contour[2],endpoint=True)
    #cbarlabels=cbarlabels[0::]-contour[0]
    #print(cbarlabels)
    #exit()

    #plot_bar
    if(axis_on[0]):

        #CB = fig.colorbar(CU, shrink=1.0, extend='both')
        CB = fig.colorbar(CU, shrink=1.0, extend='neither')

        if(contour[0]>contour[1]):

            kk= np.linspace(contour[0],0,11,endpoint=True,)
            cbarlabels=kk

        elif(contour[0]<0):

            cbarlabels = np.linspace(contour[0],contour[1] ,contour[2],endpoint=True)
            #cbarlabels=cbarlabels[1::]-contour[0]
            CB.set_ticks(cbarlabels[0::4])
            #print(cbarlabels)
            #exit()

        else:
            cbarlabels = np.linspace(contour[0],contour[1]+contour[0],contour[2],endpoint=True)
            cbarlabels=cbarlabels[1::]-contour[0]
            CB.set_ticks(cbarlabels[1::4])
            #print(cbarlabels)


        #CB.set_ticks(cbarlabels[1::4])
        CB.ax.set_title(r'%s'%contour[3])


    ax.xaxis_date()

    date_form = mdates.DateFormatter("%H" )
    ax.xaxis.set_major_formatter(date_form)

    #ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))
    #loc=mpl.ticker.MultipleLocator(0.5)
    #ax.yaxis.set_major_locator(loc)

    locatormax = mdates.HourLocator(interval=2)
    locatormin = mdates.HourLocator(interval=1)
    ax.xaxis.set_minor_locator(locatormin)
    ax.xaxis.set_major_locator(locatormax)

    ax.set_xlim(time[0],time[len(time)-1])
    ax.set_ylim([z[0],z[len(z)-1]])
    ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))


    ax.text(time[0+1], z[len(z)-1]-0.5, r' %s'%(label), fontsize=7, color='black')


    return fig,ax    

def base_top_cloud(fig,ax,ex):

    size= ex.date.shape[0]
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

        index1  =  np.argmin(ex.TVFLUX[i][0:maxl])
        indexc  =  np.argmax(   ex.CLD[i][0:maxl])

        #for j in range(1,10):
        #for goamazon 
        #for j in range(1,5):
        for j in range(1,20):

            index2=index1+j

            if ex.TVFLUX[i][index2]>0 and index1>3:

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
             if ex.QC[i][index3]<0.005 :

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



        pblh.append(ex.z[index1]/1000.0)
        cbase.append(ex.z[indexmin]/1000.0)
        cmflx.append(ex.MCUP[i,indexmin])
        cbase2.append(ex.z[indexc]/1000.0)
        ctop.append(ex.z[indexmax]/1000.0)

    step=1
    
    #Limits of time date
    idi2     = datetime(ex.datei.year,ex.datei.month,ex.datei.day,10)#dt.datetime(2014, days[2] ,days[0], 10)
    idf2     = datetime(ex.datef.year,ex.datef.month,ex.datef.day,18)#dt.datetime(2014, days[2] ,days[0], 10)
    #idf2     = ex.datef#dt.datetime(2014, days[3] ,days[0], 18)

    ni2,nf2= down.data_n(idi2,idf2,ex.date[:])


    # To find 13 and 14 hours
    i13     = datetime(ex.datef.year,ex.datef.month,ex.datef.day,13)#dt.datetime(2014, days[2] ,days[0], 10)
    i14     = datetime(ex.datef.year,ex.datef.month,ex.datef.day,14)#dt.datetime(2014, days[2] ,days[0], 10)

    n13,n14= down.data_n(i13,i14,ex.date[:])

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

    print(ex.date[mfi],'mfmax')
    print(ex.date[cbi],'cbmax')
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

    #text1='LFC'
    text1='NCL'
    text2='$\mathrm{Z_i}$'
    #text3='$\mathrm{h_{top}}$'
    text3='$\mathrm{h_{topo}}$'
    text4='$\mathrm{h_{base}}$'

    cbasef = lfilter(b, a, cbase)

    pblhf = lfilter(b, a, pblh)

    ctopf = lfilter(b, a, ctop)

    ax.plot( ex.date[ni2:nf2:step]     , cbasef[ni2:nf2:step] ,color='indigo' ,dashes=[2,1]  ,linewidth=1.0,alpha=1.0,marker='')

    ax.plot( ex.date[ni2:nf2:step]     , pblhf[ni2:nf2:step]  ,color='black'     ,linewidth=2.0,alpha=1.0,marker='')

    ax.plot( ex.date[ni2:nf2:step]     , ctopf[ni2:nf2:step]  ,color='grey' ,  dashes=[2,1]  ,linewidth=1.0,alpha=1.0,marker='')

    ax.plot( ex.date[ni2:nf2:step]     , cbase2[ni2:nf2:step]  ,color='red' ,  dashes=[2,1]  ,linewidth=1.0,alpha=1.0,marker='')

    idtex0    = idf2-timedelta(hours=8, minutes=0)#dt.datetime(2014, days[2] ,days[0], 17)
    idtex1    = idf2-timedelta(hours=3, minutes=0)#dt.datetime(2014, days[2] ,days[0], 18)
    idtex2    = idf2-timedelta(hours=0, minutes=0)#dt.datetime(2014, days[2] ,days[0], 17)
    idtex3    = idf2-timedelta(hours=1, minutes=0)#dt.datetime(2014, days[2] ,days[0], 17)

    ytex,ytex2= down.data_n(idtex1,idtex2,ex.date[:])

    ax.text(idtex2,cbasef[ytex]+0.1 , r' %s'%(text1), fontsize=7, color='indigo')
    ax.text(idtex1,pblhf[ytex] -0.2 , r' %s'%(text2), fontsize=7, color='black')
    ax.text(idtex0, pblhf[ytex]-0.2 , r' %s'%(text4), fontsize=7, color='red')

    if ex.name=='m_w_l' or  ex.name=='large':
        ax.text(idtex3,ctopf[ytex2]-0.4 , r' %s'%(text3), fontsize=7, color='black')
    else :
        ax.text(idtex3,ctopf[ytex2]+0.1 , r' %s'%(text3), fontsize=7, color='black')

    return fig,ax


def get_figsize(columnwidth, wf=0.5, hf=(5.**0.5-1.0)/2.0, ):

      """Parameters:
        - wf [float]:  width fraction in columnwidth units
        - hf [float]:  height fraction in columnwidth units.
                       Set by default to golden ratio.
        - columnwidth [float]: width of the column in latex. Get this from LaTeX
                               using \showthe\columnwidth
      Returns:  [fig_width,fig_height]: that should be given to matplotlib

      """

      fig_width_pt  = columnwidth*wf
      #1pt=0.3515
      inches_per_pt = 1.0/72.27               # Convert pt to inch
      fig_width     = fig_width_pt*inches_per_pt  # width in inches
      fig_height    = fig_width*hf           # height in inches

      #print('Fig size in',fig_width,fig_height)
      #print('Fig size mm',fig_width*2.54*2.0,fig_height*2.54*2.0,wf,hf)

      return [fig_width, fig_height]
