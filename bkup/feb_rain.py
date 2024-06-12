#!/usr/bin/python
# -*- coding: UTF-8 -*-


#################################
#PYTHON CODE TO PLOT DIFFERENS 
#MAPS PROJECTION USING THE 
#LIBRARY BASEMAP. 
#################################
#PYTHON CODE TO PLOT DIFFERENS 
# Data:13/04/22
#################################
# By: Jhonatan A. A Manco
#################################

import numpy as np

import datetime as dt  

import matplotlib.pyplot as plt

####################################################
#TO load the data 
from   Parameters_era5 import *#u3,u5

from   Parameters_own import *#u3,u5

# own function to transform the data in data_time 
from   source.data_own          import data_day

import source.functions as fnc

# Function with the definition of differents projetions
from   source.cartopyplot   import cartopy1,cartopy_sudeste,barra

from   source.nc_make  import  savetonc


di=17
hi=00
idi=[]

#for i in range(0,23,4): 
##for i in range(0,3,4): 
#
#    hour=hi+i
#
#    if hour>23:
#        h=hour-24
#        di1=di+1
#    else:
#        h=hour
#        di1=di
#
#    if h<10:
#        label='2023-02-%sT0%s:00'%(di1,h)
#    else:
#        label='2023-02-%sT%s:00'%(di1,h)
#
#    d1  = np.datetime64(label)
#    idi.append(data_day(d1,feb_rain.time.data))

for i in range(0,3,1): 
#for i in range(0,3,4): 

    #hour=hi+i
    dayi=di+i

    for k in range(0,24,6): 

        if k<10:
            label='2023-02-%sT0%s:00'%(dayi,k)
        else:
            label='2023-02-%sT%s:00'%(dayi,k)

        d1  = np.datetime64(label)
        idi.append(data_day(d1,feb.time.data))

datas=feb_rain.time
lats =feb_rain.latitude
lons =feb_rain.longitude
tp   =feb_rain.tp

"""
for i  in idi: 

    print(i)
    var= np.sum(feb_rain.tp[i-5:i+1,:,:],axis=0) 
    #print(datas[i-5:i+1].data)

    plotname=r'%s Total rain (Accumulated in 6h)[m]'%(datas[i].dt.strftime('%B %d %Y %H:00').data,)
    name='totalrain_%s_'%(datas[i].dt.strftime('%B_%d_%Y_%H').data)
    #print(name)
    fig=cartopy_sudeste(data=var,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=0.00005,b2=0.025)
    plt.close()
"""
    
#plt.show()
b1=0.00005
b2=0.025
name=r'bar_rain'
fig= barra(color='rainbow',b1=b1,b2=b2,nn=10,plotname='',figname=name,out=out_fig,label=r'[m]')
plt.show()


#z_mean=z.mean(dim='time')
#u_mean=u.mean(dim='time')
#v_mean=v.mean(dim='time')

exit()


