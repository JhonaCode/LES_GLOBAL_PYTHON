#!/usr/bin/python
# -*- coding: UTF-8 -*-

#################################
#PYTHON CODE TO PLOT DIFFERENS 
#MPAS DATA USING CARTOPY AND XARRAY. 
#################################
#PYTHON CODE TO PLOT DIFFERENS 
# Data:01/11/23
#################################
# By: Jhonatan A. A Manco
#################################

# Function to load the ncfiles
import xarray as xr

import  os,sys


#Path to the files 
path1='/dados/bamc/jhonatan.aguirre/DATA/ERA5/goamazon_south_america/python_nc' 

# Out figure folder
out_fig='/dados/bamc/jhonatan.aguirre/git_repositories/goamazon_large_scale'

#out python nc files
out_files= path1+'/python_nc'

# TO open  a unique file
iop1_f1 = path1+'/shallow_iop1.nc'
iop1    = xr.open_dataset(iop1_f1,engine='netcdf4')
iop2_f1 = path1+'/shallow_iop2.nc'
iop2    = xr.open_dataset(iop2_f1,engine='netcdf4')


# Check if the directory exists
if not os.path.exists(out_fig):
    # If it doesn't exist, create it
    os.makedirs(out_fig)

# Check if the directory exists
if not os.path.exists(out_files):
    # If it doesn't exist, create it
    os.makedirs(out_files)
