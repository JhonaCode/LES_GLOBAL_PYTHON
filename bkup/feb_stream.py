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
from   source.cartopyplot   import cartopy1,cartopy_sudeste,cartopy_vector,barra

from   source.nc_make  import  savetonc

import xarray as xr

import cartopy.crs as ccrs

di=17
hi=00
idi=[]

for i in range(0,3,1): 
#for i in range(0,1,1): 

    #hour=hi+i
    dayi=di+i

    for k in range(0,24,6): 
    #for k in range(0,6,6): 

        if k<10:
            label='2023-02-%sT0%s:00'%(dayi,k)
        else:
            label='2023-02-%sT%s:00'%(dayi,k)

        d1  = np.datetime64(label)
        idi.append(data_day(d1,feb.time.data))


datas=feb.time
levs =feb.level.values
lats =feb.latitude
lons =feb.longitude
skip=10


for i  in idi: 

    for k  in range(0,3): 

        pu=feb.u[i,k,::skip,::skip]
        pv=feb.v[i,k,::skip,::skip]

        plotname=r'%s $|\mathbf{u}|$ [m/s] %s hpa'%(datas[i].dt.strftime('%B %d %Y %H:00').data,levs[k])
        name='uv_vector_%s_%s'%(datas[i].dt.strftime('%B_%d_%Y_%H').data,levs[k])


        if(k==0):
            b1=0.0
            b2=80
        elif(k==1):
            b1=0.0
            b2=60
        else:
            b1=0.0
            b2=30

        fig=cartopy_vector(datau=pu,datav=pv,color='RdYlBu_r',plotname=plotname,figname=name,cbar=False,out=out_fig,b1=b1,b2=b2)

        #plt.show()
        #exit()
        plt.close()
"""
for k  in range(0,3): 
    if(k==0):
        b1=0.0
        b2=80
    elif(k==1):
        b1=0.0
        b2=60
    else:
        b1=0.0
        b2=30

    lev=levs[k]
    name=f'bar_rain_{lev}'

    fig= barra(color='RdYlBu_r',b1=b1,b2=b2,nn=10,plotname='',figname=name,out=out_fig,label=r'[ms$^{-1}$]')
plt.show()
    
"""


#fig = plt.figure(figsize=(6,3))
#ax = plt.axes(projection=ccrs.PlateCarree())  # note that I changed the map projection

#qv = ax.quiver(pu.longitude, pu.latitude, pu, pv, transform=ccrs.PlateCarree())

#ax.coastlines(color='grey');

#fig2 = plt.figure(figsize=(6,3))
#ax1 = plt.axes(projection=ccrs.EqualEarth())
#st = ax1.streamplot(pu.longitude, pu.latitude, pu.values, pv.values, transform=ccrs.PlateCarree())
#
#ax1.coastlines(color='grey');


#for i  in idi: 
#    var= 


    #plotname=r'%s Total rain (Sum 6h)[m]'%(datas[i].dt.strftime('%B %d %Y %H:00').data,)
    #name='totalrain_%s_'%(datas[i].dt.strftime('%B_%d_%Y_%H').data)
    ##print(name)
    #fig=cartopy_sudeste(data=var,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=0.00005,b2=0.015)
    #plt.close()
    
#plt.show()


#z_mean=z.mean(dim='time')
#u_mean=u.mean(dim='time')
#v_mean=v.mean(dim='time')

exit()


