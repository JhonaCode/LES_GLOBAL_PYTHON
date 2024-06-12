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
#TO load the data 
from   Parameters_era5 import *#u3,u5

from   Parameters_own import *#u3,u5

# own function to transform the data in data_time 
from   source.data_own          import data_day

import source.functions as fnc

# Function with the definition of differents projetions
from   source.cartopyplot   import cartopy1,cartopy_sudeste,barra

from   source.nc_make  import  savetonc


di=15
hi=00
idi=[]

#for i in range(0,3,4): 
#
#    #hour=hi+i
#
#    if hour>23:
#        h=hour-24
#        di1+=1
#        print(i/24)
#    else:
#        h=hour
#        di1=di
#
#    if h<10:
#        label='2023-02-%sT0%s:00'%(di1,h)
#    else:
#        label='2023-02-%sT%s:00'%(di1,h)

for i in range(0,5,1): 
#for i in range(0,3,4): 

    #hour=hi+i
    dayi=di+i

    for k in range(0,24,6): 

        if k<10:
            label='2023-02-%sT0%s:00'%(dayi,k)
        else:
            label='2023-02-%sT%s:00'%(dayi,k)

        d1  = np.datetime64(label)
        idi.append(data_day(d1,feb.time.data))


datas=feb.time
lats =feb.latitude
lons =feb.longitude
levs =feb.level
z    =feb.z
u    =feb.u
v    =feb.v

for i  in idi: 

    var=feb.cc[i,0,:,:] 
    #print(feb.time[i])
    plotname=r' %s FCC lev=%s [hpa] '%(datas[i].dt.strftime('%B %d %Y %H:00').data,levs[0].data)
    name='fcc_%s_lev_%s'%(datas[i].dt.strftime('%B_%d_%Y_%H').data,levs[0].data)
    #print(name)
    fig=cartopy_sudeste(data=var,lats=lats,lons=lons,plotname=plotname,figname=name,out=out_fig,b1=0.1,b2=1)

    #plt.show()

    plt.close()

b1=0.1
b2=1.0
name=r'bar_fcc'
fig= barra(color='rainbow',b1=b1,b2=b2,nn=10,plotname='',figname=name,out=out_fig,label=r'')
plt.show()

    

exit()


