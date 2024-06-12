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

import numpy as np

import datetime as dt  

import matplotlib.pyplot as plt

####################################################

from   Parameters_mpas import *#u3,u5

# own function to transform the data in data_time 
from   source.data_own          import data_day

import source.functions as fnc

# Function with the definition of differents projetions
from   source.cartopyplot   import cartopy1,cartopy_sudeste,cartopy_vector,barra

from   source.nc_make  import  savetonc

import xarray as xr

import cartopy.crs as ccrs

import metpy.calc as met

from  metpy.units import units

from  scipy.integrate import quad


#To calculate the divergent, skip=1
skip=10

exp=m15
datas   =exp.time
levs    =exp.level#/100.0 #to hPa
lats    =exp.lat
lons    =exp.lon
u       =exp.uzonal_isobaric
v       =exp.umeridional_isobaric
q       =exp.qv_isobaric
dx, dy  =met.lat_lon_grid_deltas(lons, lats)


#print(exp.variables)

#exit()

#print(levs)
#[ 100.  125.  150.  175.  200.  225.  250.  300.  350.  400.  450.  500.
#  550.  600.  650.  700.  750.  775.  800.  825.  850.  875.  900.  925.
#  950.  975. 1000.]
#exit()


#thickness of the layer
hs  = 25

for i  in  range(len(datas)): 

    div=[]
    quall=[]
    qvall=[]
        
    for nn in range(0,len(levs)):

        #Formando qu e qv
        qu=q[i,:,:,nn]*u[i,:,:,nn]
        qv=q[i,:,:,nn]*v[i,:,:,nn]

        #calculando o divergente de quv
        quall.append(qu)
        qvall.append(qv)
        div.append(met.divergence(qu, qv,dx=dx,dy=dy)*1e3)

    #zerando o acumulador
    inte  =q[0,:,:,0]*0
    intequ=q[0,:,:,0]*0
    inteqv=q[0,:,:,0]*0

    for nn in range(1,len(levs)):

        intequ+=0.5*hs*(quall[nn-1]+quall[nn])
        inteqv+=0.5*hs*(qvall[nn-1]+qvall[nn])
        inte+=0.5*hs*(div[nn-1]+div[nn])


    #plotname=r'%s $\int\nabla \cdot (q\mathbf{u}) dp$ [gkg$^{-1}$s$^{-1}hpa$] '%(datas[i].dt.strftime('%B %d %Y %H:00').data)
    plotname=r'%s $\int\nabla\cdot(q\mathbf{u})dp$ '%(datas[i].dt.strftime('%d %Y %H:00').data)
    name='divquv_mpas_%s'%(datas[i].dt.strftime('%B_%d_%Y_%H').data)


    skip=10
    pu=intequ[::skip,::skip]
    pv=inteqv[::skip,::skip]

    fig,fq=cartopy_vector(datau=pu,datav=pv,scale=800,width=0.0035,data=inte[::skip,::skip],cbar=False,plotname=plotname,figname=name,out=out_fig,b1=-0.07,b2=0.07,MPAS=True)

    plt.close()

plotname=''
clabel='[gkg$^{-1}$ms$^{-1}$Pa]'
name='barra_divquv_vector'
fig=barra(clabel=clabel,plotname=plotname,figname=name,out=out_fig,b1=-0.07,b2=0.07)

plt.show()


