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
path='/dados/bamc/public_pablo/PAPER_EE23/models/MPAS/ERA5/ntiedtke/15km/2023021500' 

# TO open  a unique file
mp1=path + '/deg.25_diag.2023-02-15_00.00.00.nc'
#m1 =  xr.open_dataset(mp1)

# Out figure folder
out_fig='/home/jhonatan.aguirre/git_report/mpas/document/fig/mpas/'


###################################################3
#Inicial day 
di=17
#Inicial hour 
hi=00

#To acumulated 
ncfiles=[]
ncdatas=[]

for i in range(0,3,1): 
#for i in range(0,1,1): 
    dayi=di+i
    for k in range(0,24,3): 
    #for k in range(0,6,3): 
        if k<10:
            #2023-02-15_00.00.00.nc
            ncfile='2023-02-%s_0%s.00.00.nc'%(dayi,k)
            data='2023-02-%sT0%s:00'%(dayi,k)
        else:
            ncfile='2023-02-%s_%s.00.00.nc'%(dayi,k)
            data='2023-02-%sT%s:00'%(dayi,k)

        ncfiles.append(ncfile)
        ncdatas.append(data)

#print(ncfiles)
#exit()
#print(nc_files)
#format the data correnponding to the name.


###################################################3

nc_files=[path +'/deg.25_diag.'+ d  for d in ncfiles] 

#Open  all files listed in ncfiles 

m15=xr.open_mfdataset(nc_files,combine='by_coords', engine='netcdf4')

#TO see the variables
#print(m15.variables)
#[print(i) for i in m15.data_vars]
#print(list(m15.keys()))
#exit()
#print(ds.time)
#print(ncdatas)

#exit()


