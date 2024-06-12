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

from   Parameters_quv import *#u3,u5

# own function to transform the data in data_time 
from   source.data_own          import data_day

import source.functions as fnc

# Function with the definition of differents projetions
from   source.cartopyplot   import cartopy1,cartopy_sudeste,cartopy_vector,barra

from   source.nc_make  import  savetonc

import xarray as xr

import cartopy.crs as ccrs

import metpy.calc as met

from  metpy.units import units

from  scipy.integrate import quad


di=17
hi=00

idi=[]

for i in range(0,1,1): 

    dayi=di+i

    for k in range(0,24,1): 

        if k<10:
            label='2023-02-%sT0%s:00'%(dayi,k)
        else:
            label='2023-02-%sT%s:00'%(dayi,k)

        d1  = np.datetime64(label)
        idi.append(data_day(d1,fquv.time.data))


#To calculate the divergent, skip=1
skip =10
datas=fquv.time
levs =fquv.isobaricInhPa.values
lats =fquv.latitude
lons =fquv.longitude
dx,dy=met.lat_lon_grid_deltas(lons, lats)


#print(levs)
#700.  650. 600. 550. 500. 450. 400. 350. 300. 250. 200
#1000. 950. 900. 850. 800. 750. 700. 650. 600. 550. 500.  450.
#  400.  350.
#thin of the layer

iqu=fquv.u[idi,:,:]
iqv=fquv.v[idi,:,:]
im =fquv.q[idi,:,:]

miqu=[]
miqv=[]
mim=[]

for i  in range (0,len(idi)-5,6): 

    print(fquv.time[i:i+5])
    miqu.append(iqu[i:i+5,:,:].mean(dim='time'))
    miqv.append(iqv[i:i+5,:,:].mean(dim='time'))
    mim.append(  im[i:i+5,:,:].mean(dim='time'))

miqu=xr.concat(miqu,dim='time')
miqv=xr.concat(miqv,dim='time')
mim =xr.concat(mim ,dim='time')

plotname=''
name=''
fig=cartopy_vector(datau=miqu[0,0,::skip,::skip],datav=miqv[0,0,::skip,::skip],scale=250,width=0.0035,cbar=False,plotname=plotname,figname=name)

plt.show()

plotname=''
name='barra_divquv_vector'
fig=barra(plotname=plotname,figname=name,out=out_fig,b1=-0.07,b2=0.07)
plt.show()
plt.close()

