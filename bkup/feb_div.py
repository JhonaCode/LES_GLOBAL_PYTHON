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
from   source.cartopyplot   import cartopy1,cartopy_sudeste,cartopy_vector

from   source.nc_make  import  savetonc

import xarray as xr

import cartopy.crs as ccrs

import metpy.calc as met

#import metpy.xarray as xt

from   metpy.cbook import example_data


# load example data
ds = example_data()

# Calculate the total deformation of the flow
div = met.divergence(ds.uwind, ds.vwind)

# start figure and set axis
fig, ax = plt.subplots(figsize=(5, 5))

# plot divergence and scale by 1e5
cf = ax.contourf(ds.lon, ds.lat, div * 1e5, range(-15, 16, 1), cmap=plt.cm.bwr_r)
plt.colorbar(cf, pad=0, aspect=50)
ax.barbs(ds.lon.values, ds.lat.values, ds.uwind, ds.vwind, color='black', length=5, alpha=0.5)
ax.set(xlim=(260, 270), ylim=(30, 40))
ax.set_title('Horizontal Divergence Calculation')



# TO calculate the divergen form data of era5 and compared


i=300
k=0
skip=1

levs =feb.level.values
lats =feb.latitude[::skip]
lons =feb.longitude[::skip]

u=feb.u[i,k,::skip,::skip]
v=feb.v[i,k,::skip,::skip]

dx, dy = met.lat_lon_grid_deltas(lons, lats)

# Calculate the total deformation of the flow
div = met.divergence(u,v,dx=dx,dy=dy)
#qu=feb.q[i,k,::skip,::skip]*feb.u[i,k,::skip,::skip]
#qv=feb.q[i,k,::skip,::skip]*feb.v[i,k,::skip,::skip]
#div = met.divergence(qu,qv,dx=dx,dy=dy)
#div = met.divergence(u,v)

# start figure and set axis
fig, ax = plt.subplots(figsize=(5, 5))

# plot divergence and scale by 1e5
cf = ax.contourf(lons, lats, div * 1e5, range(-15, 16, 1), cmap=plt.cm.bwr_r)
#cf = ax.contourf(lons, lats, div * 1e5, cmap=plt.cm.bwr_r)
plt.colorbar(cf, pad=0, aspect=50)
#ax.barbs(ds.lon.values, ds.lat.values, ds.uwind, ds.vwind, color='black', length=5, alpha=0.5)
ax.set(xlim=(260, 270), ylim=(30, 40))
ax.set_title('Horizontal Divergence Calculation')



fig, ax = plt.subplots(figsize=(5, 5))
#div = met.divergence(feb.u[i,k,::skip,::skip], feb.u[i,k,::skip,::skip])
cf = ax.contourf(lons, lats, feb.d[i,k,::skip,::skip]* 1e5, range(-15, 16, 1), cmap=plt.cm.bwr_r)
plt.colorbar(cf, pad=0, aspect=50)
#ax.barbs(ds.lon.values, ds.lat.values, ds.uwind, ds.vwind, color='black', length=5, alpha=0.5)
ax.set(xlim=(260, 270), ylim=(30, 40))
ax.set_title('Horizontal Divergence  Calculation meu')


plt.show()


