import datetime as dt

import xarray as xr

import pandas as pd

import numpy as np

#path1='/pesq/dados/bamc/jhonatan.aguirre/DATA/ERA5/MPAS_data/goamazon_era5_1.grib'

#era1 = xr.open_dataset(path1,engine='cfgrib')


#path2='/pesq/dados/bamc/jhonatan.aguirre/DATA/ERA5/MPAS_data/goamazon_era5_2.grib'

#era2 = xr.open_dataset(path2,engine='cfgrib')


#print(era1.time[0:10])
#print(era2.time[0:10])

#dataset = xr.open_mfdataset([path1,path2],concat_dim='time',engine='cfgrib')
#dataset = xr.open_mfdataset([path1,path2],engine='cfgrib', compat='override')

#print(dataset)
#exit()


def open_era5(path,name,UTC=0,date=[],lats=[],lons=[],levs=[]):

    date_format = '%Y%m%d%H%M'

    era5 = xr.open_dataset(path,engine='cfgrib',filter_by_keys={'typeOfLevel': 'surface'})
    #era5 = xr.open_dataset(path,engine='cfgrib')

    #dataset = xr.open_dataset(nc_files[0],engine='cfgrib',filter_by_keys={'typeOfLevel': 'surface'})

    if date:

        di=dt.datetime.strptime(date[0], date_format)

        df=dt.datetime.strptime(date[1], date_format)

        era5 = era5.sel(time=slice(di,df))

    if len(lats):
        era5=era5.sel(latitude=lats,method='nearest')

    if len(lons):
        era5=era5.sel(longitude=lons,method='nearest')
    #tomean = goa.sel(time=slice(di,df))
    
    era5['name'] = name
    
    ltime=pd.to_datetime(era5.time)+dt.timedelta(hours=UTC)

    #########################################
    era5['pytime']=ltime


    #print(era5.variables)
    #print(era5.Dimensions)
    #print(era5)
    #exit()

    return era5
