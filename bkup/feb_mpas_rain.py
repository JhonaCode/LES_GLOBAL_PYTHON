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

import matplotlib

####################################################

from   Parameters_mpas import *#u3,u5

# own function to transform the data in data_time 
from   source.data_own          import data_day

import source.functions as fnc

# Function with the definition of differents projetions
from   source.cartopyplot   import cartopy1,cartopy_sudeste,cartopy_vector,barra

import metpy.calc as met

from  metpy.units import units

from  scipy.integrate import quad

#matplotlib.use('TkAgg')


exp=m15

datas   =exp.time
levs    =exp.level#/100.0 #to hPa
lats    =exp.lat.values
lons    =exp.lon.values
rcov    =exp.rainc.values

rmic    =exp.rainnc.values
#pu      =u[::skip,::skip]
#pv      =v[::skip,::skip]

b1=10
b2=350


#for i  in  range(2,len(datas)-2,3): 
for i  in  range(2,len(datas)-1,2): 

    print(i, datas[i].values)
    print(datas[i-2:i+1].data)

    conve=np.sum(rcov[i-2:i+1,:,:],axis=0) 
    micro=np.sum(rmic[i-2:i+1,:,:],axis=0) 
    total= conve+micro

    #print(np.max(conve))
    #exit()

    plotname=r'%s Convective rain (6h)[mm]'%(datas[i].dt.strftime('%d %Y %H:00').data,)
    name='convective_rain_mpas_%s_'%(datas[i].dt.strftime('%B_%d_%Y_%H').data)
    #print(name)
    fig=cartopy_sudeste(data=conve,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=b1,b2=b2)
    plt.close()

    plotname=r'%s Grid-Scale rain (6h)[mm]'%(datas[i].dt.strftime('%d %Y %H:00').data,)
    name='gird_rain_mpas_%s_'%(datas[i].dt.strftime('%B_%d_%Y_%H').data)
    #print(name)
    fig=cartopy_sudeste(data=micro,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=b1,b2=b2)
    plt.close()

    plotname=r'%s Total rain (6h)[mm]'%(datas[i].dt.strftime('%d %Y %H:00').data,)
    name='totalrain_mpas_%s_'%(datas[i].dt.strftime('%B_%d_%Y_%H').data)
    #print(name)
    fig=cartopy_sudeste(data=total,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=b1,b2=b2)
    plt.close()

    #plt.show()
    #exit()

#plt.show()
name=r'bar_mpas_rain'
fig= barra(color='rainbow',b1=b1,b2=b2,nn=10,plotname='',figname=name,out=out_fig,label=r'[m]')
plt.show()


plt.show()


