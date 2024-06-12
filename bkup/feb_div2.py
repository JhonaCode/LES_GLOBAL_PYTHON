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

from   Parameters_own import *#u3,u5

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


di=17
hi=00
idi=[]

for i in range(0,3,1): 
#for i in range(0,1,1): 

    #hour=hi+i
    dayi=di+i

    for k in range(0,24,6): 
    #for k in range(0,6,6): 

        if k<10:
            label='2023-02-%sT0%s:00'%(dayi,k)
        else:
            label='2023-02-%sT%s:00'%(dayi,k)

        d1  = np.datetime64(label)
        idi.append(data_day(d1,feb.time.data))



#To calculate the divergent, skip=1
skip=10
datas=feb.time
levs =feb.level.values
lats =feb.latitude
lons =feb.longitude
dx, dy = met.lat_lon_grid_deltas(lons, lats)

for i  in idi: 

    for k  in range(2,3): 

        #i=420

        #metodo1 transformando para metpy 
        #u2 = feb.metpy.parse_cf('u')
        #v2 = feb.metpy.parse_cf('v')
        #div = met.divergence(u2[i,k,:,:],v2[i,k,:,:],dx=dx,dy=dy)

        #msem tranformaççao 
        #u1 =units.Quantity(feb.u[i,k,:,:],'m/s') 
        #v1 =units.Quantity(feb.v[i,k,:,:],'m/s') 
        #div = met.divergence(u1,v1,dx=dx,dy=dy)

        #msem tranformaççao 
        div = met.divergence(feb.u[i,k,:,:], feb.v[i,k,:,:],dx=dx,dy=dy)
        #fig=cartopy_vector(datau=pu,datav=pv,data=div[::skip,::skip],plotname=plotname,figname=name,out='',b1=-1.0e-3,b2=1.0e-3)

        #qu divengence
        #qu=feb.q[i,k,:,:]*feb.u[i,k,:,:]*1e3
        #qv=feb.q[i,k,:,:]*feb.v[i,k,:,:]*1e3
        #div = met.divergence(qu, qv,dx=dx,dy=dy)


        #if(k==0):
        #    b1=0.0
        #    b2=80

        #elif(k==1):
        #    b1=0.0
        #    b2=60
        #else:
        #    b1=0.0
        #    b2=30

        skip=10

        pu=feb.u[i,k,::skip,::skip]
        pv=feb.v[i,k,::skip,::skip]


        skip=3

        plotname=r'%s $\nabla \cdot \mathbf{u}$ [s$^{-1}$] %s hpa'%(datas[i].dt.strftime('%B %d %Y %H:00').data,levs[k])
        name='div_vector_%s_%s'%(datas[i].dt.strftime('%B_%d_%Y_%H').data,levs[k])

        #to div qu
        #fig=cartopy_vector(datau=pu,datav=pv,data=div[::skip,::skip],plotname=plotname,figname=name,out='',b1=-1.1e-3,b2=1.1e-3)
        #fig=cartopy_vector(datau=pu,datav=pv,data=feb.d[i,k,::skip,::skip],plotname=plotname,figname=name,out='',b1=-0.8e-4,b2=1.0e-4)

        fig=cartopy_vector(datau=pu,datav=pv,data=div[::skip,::skip],cbar=False,plotname=plotname,figname=name,out=out_fig,b1=-1.1e-4,b2=1.1e-4)
        #fig=cartopy_vector(datau=pu,datav=pv,data=feb.d[i,k,::skip,::skip],plotname=plotname,figname=name,out=out_fig,b1=-1.1e-4,b2=1.1e-4)
        #plt.show()
        plt.close()

plotname=''
name='barra_div'
fig=barra(plotname=plotname,figname=name,out=out_fig,b1=-1.1e-4,b2=1.1e-4)
plt.show()
plt.close()

"""
print(fquv.levs)

exit()

for i  in idi: 
        
    #i=420
    #k=0

    for k  in range(2,3): 

        q1u=feb.q[i,0,:,:]*feb.u[i,0,:,:]*1e3
        q1v=feb.q[i,0,:,:]*feb.v[i,0,:,:]*1e3
        div1= met.divergence(q1u, q1v,dx=dx,dy=dy)

        q2u=feb.q[i,1,:,:]*feb.u[i,1,:,:]*1e3
        q2v=feb.q[i,1,:,:]*feb.v[i,1,:,:]*1e3
        div2= met.divergence(q2u, q2v,dx=dx,dy=dy)

        q3u=feb.q[i,2,:,:]*feb.u[i,2,:,:]*1e3
        q3v=feb.q[i,2,:,:]*feb.v[i,2,:,:]*1e3
        div3= met.divergence(q3u, q3v,dx=dx,dy=dy)

        div=0.5*(500-200)*(div1[:,:]+div2[:,:])+0.5*(850-500)*(div2[:,:]+div3[:,:])

        plotnam=r'%s $\nabla \cdot (q\mathbf{u})$ [gkg$^{-1}$s$^{-1}$] %s hpa'%(datas[i].dt.strftime('%B %d %Y %H:00').data,levs[k])
        name='uv_vector_%s_%s'%(datas[i].dt.strftime('%B_%d_%Y_%H').data,levs[k])

        if(k==0):
            b1=0.0
            b2=80
        elif(k==1):
            b1=0.0
            b2=60
        else:
            b1=0.0
            b2=30

        pu=feb.u[i,k,::skip,::skip]
        pv=feb.v[i,k,::skip,::skip]

        skip=3
        fig=cartopy_vector(datau=pu,datav=pv,data=div[::skip,::skip],plotname=plotname,figname=name,out='',b1=-0.3,b2=0.35)

    #fig=cartopy_vector(datau=pu,datav=pv,data=feb.d[i,k,::skip,::skip],plotname=plotname,figname=name,out='',b1=-0.8e-4,b2=1.0e-4)
    #plt.close()
    plt.show()

plotname=''
name='barra_div'
fig=barra(plotname=plotname,figname=name,out=out_fig,b1=-0.3,b2=0.35)
plt.show()
plt.close()
plt.close()

#"""

