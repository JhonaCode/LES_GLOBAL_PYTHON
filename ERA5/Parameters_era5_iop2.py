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

#out python nc files
out_files= path1+'/python_nc'

#IOP2

file1  = '.goamazon_south_america_2014081500-2014103123.nc'

# TO open  a unique file1
temp_f = path1+'/era5.temperature' +file1
geo_f  = path1+'/era5.geopotential'+file1
q_f    = path1+'/era5.specific_humidity'+file1
rh_f   = path1+'/era5.relative_humidity'+file1
u_f    = path1+'/era5.u_component_of_wind'+file1
v_f    = path1+'/era5.v_component_of_wind'+file1
w_f    = path1+'/era5.vertical_velocity'+file1
cf_f   = path1+'/era5.fraction_of_cloud_cover'+file1
md_f   = path1+'/era5.vertically_integrated_moisture_divergence'+file1
tprec_f= path1+'/era5.total_precipitation'+file1
cprec_f= path1+'/era5.convective_precipitation'+file1
lcld_f = path1+'/era5.low_cloud_cover'+file1
mcld_f = path1+'/era5.medium_cloud_cover'+file1
hcld_f = path1+'/era5.high_cloud_cover'+file1
shf_f  = path1+'/era5.surface_sensible_heat_flux'+file1
lhf_f  = path1+'/era5.surface_latent_heat_flux'+file1
qu_f   = path1+'/era5.vertical_integral_of_eastward_water_vapour_flux'+file1
qv_f   = path1+'/era5.vertical_integral_of_northward_water_vapour_flux'+file1

#iop2
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
qu    =  xr.open_dataset(qu_f   )
qv    =  xr.open_dataset(qv_f   )





