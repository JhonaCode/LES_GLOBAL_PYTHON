###########################################
# PYTHON FILE TO 
# DEFINED MULTIPLES PLOT PROJECTION
#USING THE BASEMAP LIBRARY
###########################################

import numpy  as np 

import matplotlib as mpl

import matplotlib.pyplot as plt

import sources.plotparameters as pn

import cartopy.crs as ccrs

import cartopy.feature as cfeature

from cartopy.mpl.ticker import LongitudeFormatter, LatitudeFormatter

import datetime as dt

import pandas   as pd

import  os,sys

import importlib

import subprocess, sys

#from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER

#to cp the parametres defaul 
subprocess.run('cp Parameters_default.py /pesq/dados/bamc/jhonatan.aguirre/git_repositories/MAPS_python/sources/', shell = True, executable="/bin/bash")

#used the user parameter to plot(plotparameter.py) if para:
#pars=__import__('source.Parameters_default',globals())
pars=importlib.import_module('.Parameters_default','sources',)

def ajust_var_ux(data,varname,date_str=[],lev=[],vmulti=[]):

    global pars

    var=getattr(data,varname)

    if lev: 
        var= var.sel(t_iso_levels=var.t_iso_levels.isin([lev]))
        #var= np.squeeze(var,1)
    else: 
        var=var 

    if date_str: 

        date_format = '%Y-%m-%dT%H:%M'##+':00.00000000'
        date_obj=dt.datetime.strptime(date_str, date_format)
        var= var.sel(Time=[date_obj],method='nearest')

    else:

        var= var.isel(Time=[0])

    if vmulti:
        var=var*vmulti

    var =  var[0,:,0].to_polycollection(projection=pars.projection, override=True)

    return var

def axis_def_ux(ax,var,bcolor,lat,lon):

    if bcolor:
        b1=bcolor[0]
        b2=bcolor[1]
        bn=bcolor[2]
    else: 
        b1=np.min(var[:])
        b2=np.max(var[:])
        bn=5

    levels= np.linspace(b1,b2,bn,endpoint=True)

    projection=ccrs.PlateCarree()

    if(lat):
        minlat= lat[0]
        maxlat= lat[1]
        nlat  = lat[2] 
        levels_lat= np.linspace(minlat,maxlat,nlat,endpoint=True)

        if(lon):

            minlon= lon[0]
            maxlon= lon[1]
            nlon  = lon[2] 

            levels_lon= np.linspace(minlon,maxlon,nlon,endpoint=True)

            ax.set_extent([minlon, maxlon, minlat,maxlat],crs=projection)

            ax.set_xticks(levels_lon, crs=projection)
            ax.set_yticks(levels_lat, crs=projection)


    lon_formatter = LongitudeFormatter(number_format='.1f',
                                       degree_symbol='',
                                       dateline_direction_label=True)
    lat_formatter = LatitudeFormatter(number_format='.1f',
                                      degree_symbol='')

    ax.xaxis.set_major_formatter(lon_formatter)
    ax.yaxis.set_major_formatter(lat_formatter)

    ax.tick_params(axis='x', labelsize=6)
    ax.tick_params(axis='y', labelsize=6)

    return ax,levels

def def_axis_1(ax):

    #ax.set_global()
    #ax.stock_img()
    ax.coastlines()
    ax.gridlines(draw_labels=False)
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.COASTLINE)

    #MOMO STATES
    #ax.add_feature(cfeature.STATES.with_scale('50m'))

    return ax


def cartopy_plot_ux(data,varname,date_str=[],lev=[],lats=[],lons=[],vmulti=[],bcolor=[],plotname=[],color='RdBu_r',out='',cbar=True,para=[],figname=[],units=[],extend=[]):

    global pars

    if not extend:
        extend=pars.extend

    if para:
        pars=importlib.import_module('.%s'%(para),'source')

    var=ajust_var_ux(data,varname,date_str,lev,vmulti)


    pn.plotsize(pars.plotdef,pars.wf,pars.hf,pars.cmmais)

    #fig = plt.figure()
    #ax  = fig.add_subplot(1, 1, 1, projection=pars.projection)

    fig, ax = plt.subplots(
        1,
        1,
        #figsize=(5, 5),
        #facecolor="w",
        constrained_layout=True,
        subplot_kw=dict(projection=pars.projection),
    )


    ax=def_axis_1(ax)

    #Axis definitions
    ax,levels=axis_def_ux(ax,var,bcolor,lats,lons)

    filled=ax.add_collection(var)

    var.set_antialiased(False)
    var.set_cmap(color)

    print(levels)

    if cbar: 

        CB=fig.colorbar(var, orientation='vertical',shrink=0.5)

        #CB.set_ticks(levels)

        if units:

            CB.ax.set_title(r'%s'%units,fontsize=6)

        else:
            CB.ax.set_title(r'%s'%var.units,fontsize=6)

        # Add a colorbar for the filled contour.
        #fig.colorbar(filled, orientation='horizontal',shrink=0.5)

    if plotname:
        plon=plotname

        ax.set_title("%s"%(plon),fontsize=6)
    else:
        if lev:
            plon='%s_%s\n%s_%shpa'%(data.name.values,varname,date_str,lev)
        else:
            plon='%s_%s\n%s'%(data.name.values,varname,date_str)

        ax.set_title("%s"%(plon),fontsize=6)
    #else 

    if figname:
        fign=figname
    else:
        if lev:
            fign='contour_%s_%s_%s_%s'%(data.name.values,varname,date_str,lev)
        else:
            fign='contour_%s_%s_%s'%(data.name.values,varname,date_str)

    fig.savefig('%s/%s.pdf'%(pars.out_fig,fign),bbox_inches='tight', format='pdf', dpi=200)
               
    return fig     
