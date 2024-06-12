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
from   source.cartopyplot   import cartopy1,barra

from   source.nc_make  import  savetonc


d1   = np.datetime64('2023-02-01T00:00')
id1  = data_day(d1,feb.time.data)

d2   = np.datetime64('2023-02-01T23:00')
id2  = data_day(d2,feb.time.data)


##datas=feb.time
##lats =feb.latitude
##lons =feb.longitude
##levs =feb.level
##z    =feb.z[id1:id2+1,:,:,:]
##u    =feb.u[id1:id2+1,:,:,:]
##v    =feb.v[id1:id2+1,:,:,:]
##
##
##z_mean=z.mean(dim='time')
##u_mean=u.mean(dim='time')
##v_mean=v.mean(dim='time')


#1979-01-16T12:00:00
d3d   = [np.datetime64('2018-02-01T00:00:00'),
        np.datetime64('2019-02-01T00:00:00'),
        np.datetime64('2020-02-01T00:00:00'),
        np.datetime64('2021-02-01T00:00:00'),
        np.datetime64('2022-02-01T00:00:00'),
        np.datetime64('2023-02-01T00:00:00'),
        ]

"""
for d3 in d3d:

    id3  = data_day(d3,feb_mean.time.data)
    lats =feb_mean.latitude
    lons =feb_mean.longitude
    levs =feb_mean.lev
    
    var= feb_mean.anomaly_february_v[id3,0,:,:]
    
    
    d3l=d3.item().strftime('%B %Y')
    d3n=d3.item().strftime('%B_%Y')
    
    
    b1=-3
    b2=3
    
    plotname=r'%s normal anomaly v[m/s] lev=%s [hpa] '%(d3l,levs[0].data)
    name='v_%s_anomaly_lev%s'%(d3n,levs[0].data)
    fig5=cartopy1(data=var,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=b1,b2=b2,cbar=False)
    
    
    var= feb_mean.anomaly_february_v[id3,1,:,:]
    plotname=r'%s normal anomaly v[m/s] lev=%s [hpa] '%(d3l,levs[1].data)
    name='v_%s_anomaly_lev%s'%(d3n,levs[1].data)
    fig5=cartopy1(data=var,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=b1,b2=b2,cbar=False)
    
    var= feb_mean.anomaly_february_v[id3,2,:,:]
    plotname=r'%s normal anomaly v[m/s] lev=%s [hpa] '%(d3l,levs[2].data)
    name='v_%s_anomaly_lev%s'%(d3n,levs[2].data)
    fig5=cartopy1(data=var,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=b1,b2=b2,cbar=False)
    
    
    
    var= feb_mean.anomaly_february_u[id3,0,:,:]

    b1=-3
    b2=3
    plotname=r'%s normal anomaly u[m/s] lev=%s [hpa] '%(d3l,levs[0].data)
    name='u_%s_anomaly_lev%s'%(d3n,levs[0].data)
    fig5=cartopy1(data=var,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=b1,b2=b2,cbar=False)
    
    
    
    var= feb_mean.anomaly_february_u[id3,1,:,:]
    plotname=r'%s normal anomaly u[m/s] lev=%s [hpa] '%(d3l,levs[1].data)
    name='u_%s_anomaly_lev%s'%(d3n,levs[1].data)
    fig5=cartopy1(data=var,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=b1,b2=b2,cbar=False)
    
    var= feb_mean.anomaly_february_u[id3,2,:,:]
    plotname=r'%s normal anomaly u[m/s] lev=%s [hpa] '%(d3l,levs[2].data)
    name='u_%s_anomaly_lev%s'%(d3n,levs[2].data)
    fig5=cartopy1(data=var,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=b1,b2=b2,cbar=False)
    #
    
    var= feb_mean.anomaly_february_z[id3,0,:,:]
    
    plotname=r'%s normal anomaly geopotential  [m$^2$/s$^2$] lev=%s [hpa] '%(d3l,levs[0].data)
    name='z_%s_anomaly_lev%s'%(d3n,levs[0].data)
    fig5=cartopy1(data=var,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=b1,b2=b2,cbar=False)
    
    
    var= feb_mean.anomaly_february_z[id3,1,:,:]
    plotname=r'%s normal anomaly geopotential [m$^2$/s$^2$] lev=%s [hpa] '%(d3l,levs[1].data)
    name='z_%s_anomaly_lev%s'%(d3n,levs[1].data)
    fig5=cartopy1(data=var,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=b1,b2=b2,cbar=False)
    
    var= feb_mean.anomaly_february_z[id3,2,:,:]
    plotname=r'%s normal anomaly geopotential [m$^2$/s$^2$] lev=%s [hpa] '%(d3l,levs[2].data)
    name='z_%s_anomaly_lev%s'%(d3n,levs[2].data)
    fig5=cartopy1(data=var,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=b1,b2=b2,cbar=False)

    plt.close(all)
    
"""

b1=-3
b2=3

name=r'bar_v_anomaly'
fig= barra(color='RdBu_r',b1=b1,b2=b2,nn=10,plotname='',figname=name,out=out_fig,label=r'[ms$^{-1}]$')

name=r'bar_z_anomaly'
fig= barra(color='RdBu_r',b1=b1,b2=b2,nn=10,plotname='',figname=name,out=out_fig,label=r'[m$^{2}$s$^{-2}]$')


plt.show()

