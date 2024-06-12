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
path1='/dados/bamc/jhonatan.aguirre/DATA/ERA5/goamazon_south_america' 

file1='/python_nc'

# Out figure folder
out_fig='/dados/bamc/jhonatan.aguirre/git_repositories/ERA5_python/fig'

#out python nc files
out_files= path1+'/python_nc'


# TO open  a unique file1
iop1_f    = path1+file1+'/shallow_iop1.nc'
iop2_f    = path1+file1+'/shallow_iop2.nc'
small_f   = path1+file1+'/shallow_small.nc'
medium_f  = path1+file1+'/shallow_medium.nc'
large_f   = path1+file1+'/shallow_large.nc'
shca_f    = path1+file1+'/shallow_ca.nc'

#iop2
iop1    =  xr.open_dataset(iop1_f  )
iop2    =  xr.open_dataset(iop2_f  )
small   =  xr.open_dataset(small_f  )
medium  =  xr.open_dataset(medium_f  )
large   =  xr.open_dataset(large_f  )
shca    =  xr.open_dataset(shca_f  )

# Check if the directory exists
if not os.path.exists(out_fig):
    # If it doesn't exist, create it
    os.makedirs(out_fig)

# Check if the directory exists
if not os.path.exists(out_files):
    # If it doesn't exist, create it
    os.makedirs(out_files)


