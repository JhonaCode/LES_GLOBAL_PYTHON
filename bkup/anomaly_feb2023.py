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


#print(djf.data[0])
#1940-01-01T00:00:00.000000000
#print(djf.data[250])
#2023-02-01T00:00:00.000000000

d1   = np.datetime64('1940-01-01T00:00')
#d1   = np.datetime64('2012-01-01T00:00')
id1  = data_day(d1,djf.time.data)

d2   = np.datetime64('2023-02-01T00:00')
id2  = data_day(d2,djf.time.data)


datas=djf.time
lats=djf.latitude
lons=djf.longitude
levs=djf.level
z=djf.z[id1:id2+1,:,:,:]
u=djf.u[id1:id2+1,:,:,:]
v=djf.v[id1:id2+1,:,:,:]


dd_1  = fnc.season_xarray(datas,z,lats,lons,levs)
dd_2  = fnc.season_xarray(datas,u,lats,lons,levs)
dd_3  = fnc.season_xarray(datas,v,lats,lons,levs)


season='feb'
febz = fnc.anom_xarray(dd_1.feb,season)
febu = fnc.anom_xarray(dd_2.feb,season)
febv = fnc.anom_xarray(dd_3.feb,season)


dan = xr.Dataset(
         data_vars={
                    'anomaly_february_z' :(['time','lev','latitude','longitude'],febz.anomaly.data),
                    'mean_february_z'    :(['lev' ,'latitude','longitude'],febz.mean_time.data),
                    'standart_deviationz':(['lev' ,'latitude','longitude'],febz.standart_deviation.data),

                    'anomaly_february_u' :(['time','lev','latitude','longitude'],febu.anomaly.data),
                    'mean_february_u'    :(['lev' ,'latitude','longitude'],febu.mean_time.data),
                    'standart_deviationu':(['lev' ,'latitude','longitude'],febu.standart_deviation.data),

                    'anomaly_february_v' :(['time','lev','latitude','longitude'],febv.anomaly.data),
                    'mean_february_v'    :(['lev' ,'latitude','longitude'],febv.mean_time.data),
                    'standart_deviationv':(['lev' ,'latitude','longitude'],febv.standart_deviation.data),
                    },
         coords={
         'latitude':febz.latitude.data,
         'longitude':febz.longitude.data,
         'lev':febz.levs.data,
         'time':febu.time,
         },
         #name='dsummer'
    )


print('creating feb_1960a2023_anomaly.nc ........... ')
dan.to_netcdf('%s/feb_1960a2023_anomaly.nc'%(out_files))
print('done')


exit()





