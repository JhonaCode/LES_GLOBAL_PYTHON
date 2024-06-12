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

import  Parameters_iop  as de

import source.functions as fnc

# Function with the definition of differents projetions
import   source.cartopyplot   as ma 

# Function to load the ncfiles
import xarray as xr


#Mean iop1 for diffentes hours

mh1=fnc.mean_hours_xr(de.iop1,'01')
mh2=fnc.mean_hours_xr(de.iop2,'02')
print(mh1.time)
print(mh2.time)

#shca = xr.combine_by_coords(mh1,mh2)
shca = xr.merge([mh1,mh2])

shca =fnc.mean_hours_xr(shca,'01')

#t->temperature
#ma.cartopy_plot(mh1,'cc','2024-01-01T16:00',lev=850)
#ma.cartopy_plot(mh2,'cc','2024-01-01T16:00',lev=850)

ma.cartopy_qflux(mh1['p71.162'],mh1['p72.162'],date_str='2024-01-01T16:00',scale=3000,width=0.005)
ma.cartopy_qflux(mh2['p71.162'],mh2['p72.162'],date_str='2024-01-01T16:00',scale=3000,width=0.005)
ma.cartopy_qflux(shca['p71.162'],shca['p72.162'],date_str='2024-01-01T16:00',scale=3000,width=0.005)

plt.show()

exit()


#t->temperature
ma.cartopy_plot(mh1[0],'t',lev=850)
exit()

#ma.cartopy_vector(de.u1,de.v1,date_str='2014-02-27T04:00',lev=850,scale=200,width=0.005)


#ma.cartopy_plot(de.cf1  ,'cc','2014-02-27T00:00',lev=850,lat=[-5,5,5],lon=[-85,-45,5],bcolor=[0,0.3,10])

plt.show()


#ma.cartopy_vector(de.u1,de.u2,scale=1, width=0.1,data=[0],color='RdBu_r',bcolor=[0,10,10],plotname='',figname='fig1',out='',cbar=True,MPAS=False):
#
#ma.cartopy_plot(de.q    ,'q','2014-02-01T08:00',lev=850)
#
#ma.cartopy_plot(de.temp1,'t','2014-02-01T12:00',lev=850)

#shallow :)

#ma.cartopy_plot(de.cf1,'cc','2014-02-27T04:00',lev=850)
#ma.cartopy_plot(de.cf1,'cc','2014-02-27T08:00',lev=850)
#ma.cartopy_plot(de.cf1,'cc','2014-02-27T12:00',lev=850)
#ma.cartopy_plot(de.cf1,'cc','2014-02-27T16:00',lev=850)
#ma.cartopy_plot(de.cf1,'cc','2014-02-27T20:00',lev=850)
#plt.show()
#exit()
