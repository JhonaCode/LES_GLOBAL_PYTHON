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

from   Parameters_quv import *#u3,u5

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
        idi.append(data_day(d1,fquv.time.data))



#To calculate the divergent, skip=1
skip=10
datas=fquv.time
levs =fquv.isobaricInhPa.values
lats =fquv.latitude
lons =fquv.longitude
dx, dy = met.lat_lon_grid_deltas(lons, lats)

#print(levs)
#700.  650. 600. 550. 500. 450. 400. 350. 300. 250. 200

#1000. 950. 900. 850. 800. 750. 700. 650. 600. 550. 500.  450.
#  400.  350.



#thin of the layer
hs  = 50

for i  in idi: 

    div=[]
    quall=[]
    qvall=[]
        
    for nn in range(0,len(levs)):

        #Formando qu e qv
        qu=fquv.q[i,nn,:,:]*fquv.u[i,nn,:,:]
        qv=fquv.q[i,nn,:,:]*fquv.v[i,nn,:,:]

        #calculando o divergente de quv
        quall.append(qu)
        qvall.append(qv)
        div.append(met.divergence(qu, qv,dx=dx,dy=dy)*1e3)

    #zerando o acumulador
    inte  =np.zeros([fquv.q.shape[2],fquv.q.shape[3]])
    intequ=np.zeros([fquv.q.shape[2],fquv.q.shape[3]])
    inteqv=np.zeros([fquv.q.shape[2],fquv.q.shape[3]])

    for nn in range(1,len(levs)):

        intequ+=0.5*hs*(quall[nn-1]+quall[nn])
        inteqv+=0.5*hs*(qvall[nn-1]+qvall[nn])
        inte+=0.5*hs*(div[nn-1]+div[nn])

        #print(nn,nn-1,levs[nn],levs[nn-1])

    #exit()


#    q2u=fquv.q[i,1,:,:]*fquv.u[i,1,:,:]*1e3
#    q2v=fquv.q[i,1,:,:]*fquv.v[i,1,:,:]*1e3
#    div2= met.divergence(q2u, q2v,dx=dx,dy=dy)
#
#    q3u=fquv.q[i,2,:,:]*fquv.u[i,2,:,:]*1e3
#    q3v=fquv.q[i,2,:,:]*fquv.v[i,2,:,:]*1e3
#    div3= met.divergence(q3u, q3v,dx=dx,dy=dy)

#    div=0.5*(500-200)*(div1[:,:]+div2[:,:])+0.5*(850-500)*(div2[:,:]+div3[:,:])

    plotname=r'%s $\int\nabla \cdot (q\mathbf{u}) dp$ [gkg$^{-1}$s$^{-1}hpa$] '%(datas[i].dt.strftime('%B %d %Y %H:00').data)
    name='divquv_wind_%s'%(datas[i].dt.strftime('%B_%d_%Y_%H').data)


    skip=10

    #pu=intequ[::skip,::skip]
    #pv=inteqv[::skip,::skip]

    #skip=3
    #fig=cartopy_vector(datau=pu,datav=pv,scale=800,width=0.0035,data=inte[::skip,::skip],cbar=False,plotname=plotname,figname=name,out=out_fig,b1=-0.07,b2=0.07)

    #850 hpa, vector of wind
    k=3
    pu=fquv.u[i,k,::skip,::skip]
    pv=fquv.v[i,k,::skip,::skip]

    fig=cartopy_vector(datau=pu,datav=pv,scale=250,width=0.0035,data=inte[::skip,::skip],cbar=False,plotname=plotname,figname=name,out=out_fig,b1=-0.07,b2=0.07)

    #plt.show()
    #exit()
    plt.close()

plotname=''
name='barra_divquv_vector'
fig=barra(plotname=plotname,figname=name,out=out_fig,b1=-0.07,b2=0.07)
plt.show()
plt.close()


