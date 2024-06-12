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
path='/dados/bamc/jhonatan.aguirre/DATA/ERA5/goamazon_south_america' 

# Out figure folder
out_fig='/dados/bamc/jhonatan.aguirre/git_repositories/goamazon_large_scale'

#out python nc files
out_files= path+'/python_nc'

# TO open  a unique file
temp_f = path+'/era5.temperature.goamazon_south_america_2014020100-2014033023.nc'
geo_f  = path+'/era5.geopotential.goamazon_south_america_2014020100-2014033023.nc'
q_f    = path+'/era5.specific_humidity.goamazon_south_america_2014020100-2014033023.nc'
rh_f   = path+'/era5.relative_humidity.goamazon_south_america_2014020100-2014033023.nc'
u_f    = path+'/era5.u_component_of_wind.goamazon_south_america_2014020100-2014033023.nc'
v_f    = path+'/era5.v_component_of_wind.goamazon_south_america_2014020100-2014033023.nc'
w_f    = path+'/era5.vertical_velocity.goamazon_south_america_2014020100-2014033023.nc'
cf_f   = path+'/era5.fraction_of_cloud_cover.goamazon_south_america_2014020100-2014033023.nc'
md_f   = path+'/era5.vertically_integrated_moisture_divergence.goamazon_south_america_2014020100-2014033023.nc'
tprec_f= path+'/era5.total_precipitation.goamazon_south_america_2014020100-2014033023.nc'
cprec_f= path+'/era5.convective_precipitation.goamazon_south_america_2014020100-2014033023.nc'
lcld_f = path+'/era5.low_cloud_cover.goamazon_south_america_2014020100-2014033023.nc'
mcld_f = path+'/era5.medium_cloud_cover.goamazon_south_america_2014020100-2014033023.nc'
hcld_f = path+'/era5.high_cloud_cover.goamazon_south_america_2014020100-2014033023.nc'
shf_f  = path+'/era5.surface_sensible_heat_flux.goamazon_south_america_2014020100-2014033023.nc'
lhf_f  = path+'/era5.surface_latent_heat_flux.goamazon_south_america_2014020100-2014033023.nc'
qu_f   = path+'/era5.vertical_integral_of_eastward_water_vapour_flux.goamazon_south_america_2014020100-2014033023.nc'
qv_f   = path+'/era5.vertical_integral_of_northward_water_vapour_flux.goamazon_south_america_2014020100-2014033023.nc'

#iop1
temp  =  xr.open_dataset(temp_f  )
cf    =  xr.open_dataset(cf_f    )
z     =  xr.open_dataset(geo_f   )
q     =  xr.open_dataset(q_f     )
rh    =  xr.open_dataset(rh_f    )
u     =  xr.open_dataset(u_f     )
v     =  xr.open_dataset(v_f     )
w     =  xr.open_dataset(w_f     )
md    =  xr.open_dataset(md_f    )
tprec =  xr.open_dataset(tprec_f )
cprec =  xr.open_dataset(cprec_f )
lcld  =  xr.open_dataset(lcld_f  )
mcld  =  xr.open_dataset(mcld_f  )
hcld  =  xr.open_dataset(hcld_f  )
shf   =  xr.open_dataset(shf_f   )
lhf   =  xr.open_dataset(lhf_f   )
qu    =  xr.open_dataset(qu_f    )
qv    =  xr.open_dataset(qv_f    )


# Check if the directory exists
if not os.path.exists(out_fig):
    # If it doesn't exist, create it
    os.makedirs(out_fig)

# Check if the directory exists
if not os.path.exists(out_files):
    # If it doesn't exist, create it
    os.makedirs(out_files)



