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

import os, sys

import numpy as np

import datetime as dt  

import cftime

import matplotlib.pyplot as plt

####################################################
#TO load the data 
from   Parameters_era5 import *#u3,u5

# own function to transform the data in data_time 
from   source.data_own          import data_day

# Own Functions, to read the data, make anomaly 
from   source.variablesfunction import ncdump

import source.functions as fnc

# Function with the definition of differents projetions
from   source.cartopyplot   import cartopy1

from   source.nc_make  import  savetonc

import metpy.calc as met

import metpy.xarray as xt

from   metpy.cbook import example_data

import cartopy.crs as ccrs

import cartopy.feature as cfeature

import xarray as xr

from  metpy.units import units

#1979-01-16T12:00:00
d1   = np.datetime64('2023-02-01T12:00:00')
#id1  = data_day(d1,feb.data)
#print(id1)



plotname=r'2023-02-01  12:00 UTC$\nabla \times \overline{u}$ lev=%s [hpa] '%(feb.level[0].data)
name='CF_2023-02-01T1200_lev%s'%feb.level[0].data
fig5=cartopy1(data=feb.cf[id1,0,:,:],lats=feb.lat,lons=feb.lon,plotname=plotname,figname=name)#,b1=-7,b2=7)
#

print(feb)

print(feb)
plt.show()
exit()


dd = xr.Dataset(
         data_vars={
                    'anomaly_summer_v':(['time1','lev','latitude','longitude'],sv1.anomaly.data),
                    'anomaly_summer_s':(['time1','lev','latitude','longitude'],ss1.anomaly.data),
                    'anomaly_winter_v':(['time2','lev','latitude','longitude'],wv1.anomaly.data),
                    'anomaly_winter_s':(['time2','lev','latitude','longitude'],ws1.anomaly.data),
                    },
         coords={
         'latitude':sv1.latitude,
         'longitude':sv1.longitude,
         'lev':sv1.lev,
         'time1':sv1.time.data,
         'time2':wv1.time.data,
         },
         #name='dsummer'
    )

dd.to_netcdf('%s/vorticity.nc'%(out_files))

#plotname=r'Winter $\mathrm{\overline{v}}$ [m/s]   1978-2014'
#name='mean_winter_vor'
#fig5=cartopy1(data=wv1.mean_time[0,:,:],lats=lats,lons=lons,plotname=plotname,figname=name)
#
#plotname=r'Winter Vor $\mathrm{\overline{u}}$ [m/s]  1978-2014'
#name='mean_winter_v'
#fig5=cartopy1(data=ws1.mean_time[0,:,:],lats=lats,lons=lons,plotname=plotname,figname=name)
#plt.show()
#

exit()



####
####
####dx, dy = met.lat_lon_grid_deltas(lon, lat, initstring=data_crs.proj4_init)
####print(dx,dy)
####exit()
####exit()

#tu = "hours since 1970-01-01 00:00:00"
#tc = "360_day"
#attrs={'axis': 'time', 'bounds': 'time_bnds', 'standard_name': 'time', '_metpy_axis': 'time'}


#ds = xr.DataArray(
#     data=d_summer,
#     dims=var.dims,
#     coords={
#         'longitude':var.longitude,
#         'latitude':var.latitude,
#         'time':t_summer,
#         }
#         #referece_time=tc,
#         ,
#    name='dsummer'
#    )

#dwin = xr.DataArray(
#     data=d_win,
#     dims=var.dims,
#     coords={
#         'longitude':var.longitude,
#         'latitude':var.latitude,
#         'time':t_win,
#        },
#    name='dwin'
#    )





