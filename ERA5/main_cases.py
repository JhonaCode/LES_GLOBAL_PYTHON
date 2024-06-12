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

import  Parameters_era5_shca  as sh

import source.functions as fnc

# Function with the definition of differents projetions
import   source.cartopyplot   as ma 

# Function to load the ncfiles
import xarray as xr


#Mean iop1 for diffentes hours, ()
iop1        =   fnc.mean_hours_xr(sh.iop1  ,'iop1'  ,'2024-01-01')
iop2        =   fnc.mean_hours_xr(sh.iop2  ,'iop2'  ,'2024-01-02')
shca        =   fnc.mean_hours_xr(sh.shca  ,'shca'  ,'2024-01-01')
small       =   fnc.mean_hours_xr(sh.small ,'small' ,'2024-01-01')
large       =   fnc.mean_hours_xr(sh.large ,'large' ,'2024-01-01')
medium      =   fnc.mean_hours_xr(sh.medium,'medium','2024-01-01')

#ma.cartopy_plot(iop1,  'cc','2024-01-01T16:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(iop2,  'cc','2024-01-02T16:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(shca,  'cc','2024-01-01T16:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(small, 'cc','2024-01-01T16:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(medium,'cc','2024-01-01T16:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(large, 'cc','2024-01-01T16:00',lev=250,bcolor=[0,1,6])
#
#ma.cartopy_plot(iop1,  'cc','2024-01-01T20:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(iop2,  'cc','2024-01-02T20:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(shca,  'cc','2024-01-01T20:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(small, 'cc','2024-01-01T20:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(medium,'cc','2024-01-01T20:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(large, 'cc','2024-01-01T20:00',lev=250,bcolor=[0,1,6])
#
#ma.cartopy_plot(iop1,  'cc','2024-01-01T16:00',lev=500,bcolor=[0,1,6])
#ma.cartopy_plot(iop2,  'cc','2024-01-02T16:00',lev=500,bcolor=[0,1,6])
#ma.cartopy_plot(shca,  'cc','2024-01-01T16:00',lev=500,bcolor=[0,1,6])
#ma.cartopy_plot(small, 'cc','2024-01-01T16:00',lev=500,bcolor=[0,1,6])
#ma.cartopy_plot(medium,'cc','2024-01-01T16:00',lev=500,bcolor=[0,1,6])
#ma.cartopy_plot(large, 'cc','2024-01-01T16:00',lev=500,bcolor=[0,1,6])
#
#ma.cartopy_plot(iop1,  'cc','2024-01-01T20:00',lev=500,bcolor=[0,1,6])
#ma.cartopy_plot(iop2,  'cc','2024-01-02T20:00',lev=500,bcolor=[0,1,6])
#ma.cartopy_plot(shca,  'cc','2024-01-01T20:00',lev=500,bcolor=[0,1,6])
#ma.cartopy_plot(small, 'cc','2024-01-01T20:00',lev=500,bcolor=[0,1,6])
#ma.cartopy_plot(medium,'cc','2024-01-01T20:00',lev=500,bcolor=[0,1,6])
#ma.cartopy_plot(large, 'cc','2024-01-01T20:00',lev=500,bcolor=[0,1,6])
#
#ma.cartopy_plot(iop1,  'cc','2024-01-01T16:00',lev=850,bcolor=[0,1,6])
#ma.cartopy_plot(iop2,  'cc','2024-01-02T16:00',lev=850,bcolor=[0,1,6])
#ma.cartopy_plot(shca,  'cc','2024-01-01T16:00',lev=850,bcolor=[0,1,6])
#ma.cartopy_plot(small, 'cc','2024-01-01T16:00',lev=850,bcolor=[0,1,6])
#ma.cartopy_plot(medium,'cc','2024-01-01T16:00',lev=850,bcolor=[0,1,6])
#ma.cartopy_plot(large, 'cc','2024-01-01T16:00',lev=850,bcolor=[0,1,6])
#
#ma.cartopy_plot(iop1,  'cc','2024-01-01T20:00',lev=850,bcolor=[0,1,6])
#ma.cartopy_plot(iop2,  'cc','2024-01-02T20:00',lev=850,bcolor=[0,1,6])
#ma.cartopy_plot(shca,  'cc','2024-01-01T20:00',lev=850,bcolor=[0,1,6])
#ma.cartopy_plot(small, 'cc','2024-01-01T20:00',lev=850,bcolor=[0,1,6])
#ma.cartopy_plot(medium,'cc','2024-01-01T20:00',lev=850,bcolor=[0,1,6])
#ma.cartopy_plot(large, 'cc','2024-01-01T20:00',lev=850,bcolor=[0,1,6])
#
#ma.cartopy_plot(iop1,  'w','2024-01-01T16:00',lev=250,bcolor=[-1,1,6])
#ma.cartopy_plot(iop2,  'w','2024-01-02T16:00',lev=250,bcolor=[-1,1,6])
#ma.cartopy_plot(shca,  'w','2024-01-01T16:00',lev=250,bcolor=[-1,1,6])
#ma.cartopy_plot(small, 'w','2024-01-01T16:00',lev=250,bcolor=[-1,1,6])
#ma.cartopy_plot(medium,'w','2024-01-01T16:00',lev=250,bcolor=[-1,1,6])
#ma.cartopy_plot(large, 'w','2024-01-01T16:00',lev=250,bcolor=[-1,1,6])
#
#ma.cartopy_plot(iop1,  'w','2024-01-01T20:00',lev=250,bcolor=[-1,1,6])
#ma.cartopy_plot(iop2,  'w','2024-01-02T20:00',lev=250,bcolor=[-1,1,6])
#ma.cartopy_plot(shca,  'w','2024-01-01T20:00',lev=250,bcolor=[-1,1,6])
#ma.cartopy_plot(small, 'w','2024-01-01T20:00',lev=250,bcolor=[-1,1,6])
#ma.cartopy_plot(medium,'w','2024-01-01T20:00',lev=250,bcolor=[-1,1,6])
#ma.cartopy_plot(large, 'w','2024-01-01T20:00',lev=250,bcolor=[-1,1,6])
#
#ma.cartopy_plot(iop1,  'w','2024-01-01T16:00',lev=500,bcolor=[-1,1,6])
#ma.cartopy_plot(iop2,  'w','2024-01-02T16:00',lev=500,bcolor=[-1,1,6])
#ma.cartopy_plot(shca,  'w','2024-01-01T16:00',lev=500,bcolor=[-1,1,6])
#ma.cartopy_plot(small, 'w','2024-01-01T16:00',lev=500,bcolor=[-1,1,6])
#ma.cartopy_plot(medium,'w','2024-01-01T16:00',lev=500,bcolor=[-1,1,6])
#ma.cartopy_plot(large, 'w','2024-01-01T16:00',lev=500,bcolor=[-1,1,6])
#
#ma.cartopy_plot(iop1,  'w','2024-01-01T20:00',lev=500,bcolor=[-1,1,6])
#ma.cartopy_plot(iop2,  'w','2024-01-02T20:00',lev=500,bcolor=[-1,1,6])
#ma.cartopy_plot(shca,  'w','2024-01-01T20:00',lev=500,bcolor=[-1,1,6])
#ma.cartopy_plot(small, 'w','2024-01-01T20:00',lev=500,bcolor=[-1,1,6])
#ma.cartopy_plot(medium,'w','2024-01-01T20:00',lev=500,bcolor=[-1,1,6])
#ma.cartopy_plot(large, 'w','2024-01-01T20:00',lev=500,bcolor=[-1,1,6])
#
#ma.cartopy_plot(iop1,  'w','2024-01-01T16:00',lev=850,bcolor=[-1,1,6])
#ma.cartopy_plot(iop2,  'w','2024-01-02T16:00',lev=850,bcolor=[-1,1,6])
#ma.cartopy_plot(shca,  'w','2024-01-01T16:00',lev=850,bcolor=[-1,1,6])
#ma.cartopy_plot(small, 'w','2024-01-01T16:00',lev=850,bcolor=[-1,1,6])
#ma.cartopy_plot(medium,'w','2024-01-01T16:00',lev=850,bcolor=[-1,1,6])
#ma.cartopy_plot(large, 'w','2024-01-01T16:00',lev=850,bcolor=[-1,1,6])
#
#ma.cartopy_plot(iop1,  'w','2024-01-01T20:00',lev=850,bcolor=[-1,1,6])
#ma.cartopy_plot(iop2,  'w','2024-01-02T20:00',lev=850,bcolor=[-1,1,6])
#ma.cartopy_plot(shca,  'w','2024-01-01T20:00',lev=850,bcolor=[-1,1,6])
#ma.cartopy_plot(small, 'w','2024-01-01T20:00',lev=850,bcolor=[-1,1,6])
#ma.cartopy_plot(medium,'w','2024-01-01T20:00',lev=850,bcolor=[-1,1,6])
#ma.cartopy_plot(large, 'w','2024-01-01T20:00',lev=850,bcolor=[-1,1,6])


#ma.cartopy_plot(iop1,  'z','2024-01-01T16:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(iop2,  'z','2024-01-02T16:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(shca,  'z','2024-01-01T16:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(small, 'z','2024-01-01T16:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(medium,'z','2024-01-01T16:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(large, 'z','2024-01-01T16:00',lev=250,bcolor=[0,1,6])
#ma.cartopy_plot(large, 'z','2024-01-01T20:00',lev=250,bcolor=[0,1,6])

ma.cartopy_plot(iop1,  'tp','2024-01-01T16:00',vmulti=1000,bcolor=[1,5,5],extend='max',units=r"[mmday$^{-1}$]")
ma.cartopy_plot(iop2,  'tp','2024-01-02T16:00',vmulti=1000,bcolor=[1,5,5],extend='max',units=r"[mmday$^{-1}$]")
ma.cartopy_plot(shca,  'tp','2024-01-01T16:00',vmulti=1000,bcolor=[1,5,5],extend='max',units=r"[mmday$^{-1}$]")
ma.cartopy_plot(small, 'tp','2024-01-01T16:00',vmulti=1000,bcolor=[1,5,5],extend='max',units=r"[mmday$^{-1}$]")
ma.cartopy_plot(medium,'tp','2024-01-01T16:00',vmulti=1000,bcolor=[1,5,5],extend='max',units=r"[mmday$^{-1}$]")
ma.cartopy_plot(large, 'tp','2024-01-01T16:00',vmulti=1000,bcolor=[1,5,5],extend='max',units=r"[mmday$^{-1}$]")

ma.cartopy_plot(iop1,  'cp','2024-01-01T16:00',vmulti=1000,bcolor=[1,5,5],extend='max',units=r"[mmday$^{-1}$]")
ma.cartopy_plot(iop2,  'cp','2024-01-02T16:00',vmulti=1000,bcolor=[1,5,5],extend='max',units=r"[mmday$^{-1}$]")
ma.cartopy_plot(shca,  'cp','2024-01-01T16:00',vmulti=1000,bcolor=[1,5,5],extend='max',units=r"[mmday$^{-1}$]")
ma.cartopy_plot(small, 'cp','2024-01-01T16:00',vmulti=1000,bcolor=[1,5,5],extend='max',units=r"[mmday$^{-1}$]")
ma.cartopy_plot(medium,'cp','2024-01-01T16:00',vmulti=1000,bcolor=[1,5,5],extend='max',units=r"[mmday$^{-1}$]")
ma.cartopy_plot(large, 'cp','2024-01-01T16:00',vmulti=1000,bcolor=[1,5,5],extend='max',units=r"[mmday$^{-1}$]")

plt.show()


#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=iop1,date_str='2024-01-01T16:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=iop2,date_str='2024-01-02T16:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=shca,date_str='2024-01-01T16:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=small,date_str='2024-01-01T16:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=medium,date_str='2024-01-01T16:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=large,date_str='2024-01-01T16:00',scale=3000,width=0.005)

#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=iop1  ,date_str='2024-01-01T20:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=iop2  ,date_str='2024-01-02T20:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=shca  ,date_str='2024-01-01T20:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=small ,date_str='2024-01-01T20:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=medium,date_str='2024-01-01T20:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=large ,date_str='2024-01-01T20:00',scale=3000,width=0.005)

#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=iop1  ,date_str='2024-01-01T12:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=iop2  ,date_str='2024-01-02T12:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=shca  ,date_str='2024-01-01T12:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=small ,date_str='2024-01-01T12:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=medium,date_str='2024-01-01T12:00',scale=3000,width=0.005)
#ma.cartopy_vector('p71.162','p72.162',bcolor=[-500,500,6],data=large ,date_str='2024-01-01T12:00',scale=3000,width=0.005)

