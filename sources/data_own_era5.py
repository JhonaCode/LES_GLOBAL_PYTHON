import datetime as dt

import xarray as xr

import pandas as pd

import numpy as np

from cfgrib import open_datasets

date_format = "%Y%m%d%H%M"

def open_era5_by_vars(path, name, shortNames, date=None, lats=None, lons=None, UTC=0):
    datasets = []

    datasets = []

    for shortName in shortNames:
        try:
            ds = xr.open_dataset(
                path,
                engine="cfgrib",
                backend_kwargs={"filter_by_keys": {"typeOfLevel": "surface", "shortName": shortName}}
            )
    
            # skip empty datasets
            if not ds.dims:
                print(f"Warning: variable '{shortName}' not found in file, skipping.")
                continue
    
            # create time if missing
            if "time" not in ds.coords:
                if "forecastReferenceTime" in ds.coords and "step" in ds.coords:
                    valid_time = pd.to_datetime(ds.forecastReferenceTime.values) + pd.to_timedelta(ds.step.values, unit='s')
                    ds = ds.assign_coords(time=("step", valid_time))
                else:
                    print(f"Warning: variable '{shortName}' has no 'time' info, skipping.")
                    continue
    
            # optional filtering
            if date:
                di = dt.datetime.strptime(date[0], date_format)
                df = dt.datetime.strptime(date[1], date_format)
                ds = ds.sel(time=slice(di, df))
    
            if lats is not None and len(lats):
                ds = ds.sel(latitude=lats, method="nearest")
            if lons is not None and len(lons):
                ds = ds.sel(longitude=lons, method="nearest")
    
            datasets.append(ds)
    
        except Exception as e:
            print(f"Warning: failed to load variable '{shortName}': {e}")
            continue
    
    # merge all successfully loaded datasets
    if datasets:
        era5 = xr.merge(datasets, compat="override")
        era5["name"] = name
        ltime = pd.to_datetime(era5.time.values) + dt.timedelta(hours=UTC)
        era5 = era5.assign_coords(local_time=("time", ltime))
    else:
        raise ValueError("No variables were successfully loaded from the GRIB file.")
    
    return era5



def open_era5(path, name, date=None, lats=None, lons=None, UTC=0):

    
    # ERA5 stores some variables with different temporal definitions.
    # open all sub-datasets (ERA5 surface often has multiple groups)
    datasets = open_datasets(
        path,
        backend_kwargs={"filter_by_keys": {"typeOfLevel": "surface"}}
    )

    # union of all available times
    all_times = np.unique(np.concatenate([ds.time.values for ds in datasets]))

    # align all datasets to the same time axis (fill missing with NaN)
    datasets_aligned = [ds.reindex(time=all_times) for ds in datasets]

    # merge into a single dataset
    era5 = xr.merge(datasets_aligned, compat="override")

    # optional time filtering
    if date:
        di = dt.datetime.strptime(date[0], date_format)
        df = dt.datetime.strptime(date[1], date_format)
        era5 = era5.sel(time=slice(di, df))

    # optional spatial subsetting
    if lats is not None and len(lats):
        era5 = era5.sel(latitude=lats, method="nearest")
    if lons is not None and len(lons):
        era5 = era5.sel(longitude=lons, method="nearest")

    # add a name variable
    era5["name"] = name

    # build shifted local time coordinate
    ltime = pd.to_datetime(era5.time.values) + dt.timedelta(hours=UTC)
    era5 = era5.assign_coords(local_time=("time", ltime))

    return era5


def open_era5_old(path,name,UTC=0,date=[],lats=[],lons=[],levs=[]):

    date_format = '%Y%m%d%H%M'

    ##
    #era5 = xr.open_dataset(path,engine='cfgrib',filter_by_keys={'typeOfLevel': 'surface'})

    era5 = xr.open_datasets(path,engine='cfgrib',filter_by_keys={'typeOfLevel': 'surface'})


    #era5 = xr.open_dataset(path,engine='cfgrib')

    #dataset = xr.open_dataset(nc_files[0],engine='cfgrib',filter_by_keys={'typeOfLevel': 'surface'})


    #print(ltime)
    
    # valid_time coordinate
    valid_time= era5.time + era5.step

    # add it to dataset
    era5 = era5.assign_coords(valid_time=("time", valid_time.values))

    if date:

        di=dt.datetime.strptime(date[0], date_format)

        df=dt.datetime.strptime(date[1], date_format)

        era5 = era5.sel(time=slice(di,df))

    if len(lats):
        era5=era5.sel(latitude=lats,method='nearest')

    if len(lons):
        era5=era5.sel(longitude=lons,method='nearest')
    #tomean = goa.sel(time=slice(di,df))
    
    
    #To Transform to UTC
    ltime=pd.to_datetime(era5.time)+dt.timedelta(hours=UTC)

    era5['pytime']=ltime

    era5['name'] = name
    exit()
    #########################################


    #print(era5.variables)
    #print(era5.Dimensions)
    #print(era5)
    #exit()

    return era5
