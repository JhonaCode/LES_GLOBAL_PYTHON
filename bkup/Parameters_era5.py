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


#Path to the files 
path='/dados/bamc/jhonatan.aguirre/DATA/ERA5/goamazon_south_america_2014020100-2014033023' 


# Out figure folder
out_fig='/dados/bamc/jhonatan.aguirre/git_repositories/goamazon_large_scale'

#out python nc files
out_files= out_fig+'/python_nc'

# TO open  a unique file
temp_f= path+'/era5.temperature.goamazon_south_america_2014020100-2014033023.nc'
temp  =  xr.open_dataset(temp_f)


# Check if the directory exists
if not os.path.exists(out_fig):
    # If it doesn't exist, create it
    os.makedirs(out_fig)

# Check if the directory exists
if not os.path.exists(out_files):
    # If it doesn't exist, create it
    os.makedirs(out_files)



