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

import matplotlib.pyplot as plt
####################################################

import  Parameters_era5_iop1  as i1
import  Parameters_era5_iop2  as i2

import source.var_joint  as vj

import source.functions  as fnc

# Function with the definition of differents projetions
import   source.cartopyplot   as ma 

# Function to load the ncfiles
import xarray as xr

#""" IOP1
days  =   [
            '02-27', '03-06', '03-09',
            '03-10', '03-15', '03-16',
            '03-17', '03-18'
           ]

tl1= vj.joint(i1,days,name='shallow_iop1',outf=i1.out_files,save=True)


#### IOP2

days  =   [ 
          '09-02','09-03','09-04','09-09','11-09', 
          '09-14','09-15','09-16','09-19','09-20', 
          '09-21','09-22','09-23','09-26','09-27', 
          '09-29','10-01','10-03','10-05','10-07', 
           ]

tl2= vj.joint(i2,days,name='shallow_iop2',outf=i1.out_files,save=True)

###SHCA
shca = xr.merge([
                tl1,tl2
                        ] )


name='shallow_ca'
print('creating %s.nc ........... '%(name))
shca.to_netcdf('%s/%s.nc'%(i1.out_files,name))

#"""

"""LARGE

days  =   [
           '02-27','03-06',
          ]



tl1  = vj.joint(i1,days,outf=i1.out_files,save=False)



days  =   [
           '03-10','09-09','09-19','09-20','10-05',
           '09-03','09-15','09-22','09-26','09-29','10-01'
           ]

tl2=vj.joint(i2,days,outf=i1.out_files,save=False)


large = xr.merge([
                tl1,tl2
                        ] )


name='shallow_large'
print('creating %s.nc ........... '%(name))
large.to_netcdf('%s/%s.nc'%(i1.out_files,name))


"""

"""MEDIUM
days  =   [
                "03-09","03-17","03-15",
              ]


tl1  = vj.joint(i1,days,outf=i1.out_files,save=False)



exp_days  =   [
               "09-02","09-14","09-21",
               "09-27","10-07","10-08"
               ]

tl2=vj.joint(i2,days,outf=i1.out_files,save=False)


medium = xr.merge([
                tl1,tl2
                        ] )


name='shallow_medium'
print('creating %s.nc ........... '%(name))
medium.to_netcdf('%s/%s.nc'%(i1.out_files,name))

"""

"""SMALL
days  =   [
                "03-16","03-18",
              ]


tl1  = vj.joint(i1,days,i1.out_files,save=False)



days  =   [
               "09-04","09-11","09-16",
               "09-23","10-03","10-09"
               ]

tl2=vj.joint(i2,days,i1.out_files,save=False)


small = xr.merge([
                tl1,tl2
                        ] )


name='shallow_small'
print('creating %s.nc ........... '%(name))
small.to_netcdf('%s/%s.nc'%(i1.out_files,name))

"""



plt.show()
