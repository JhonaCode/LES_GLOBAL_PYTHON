#IN
#data: my data
#time: Time vectors with data.
#Out
#index

import datetime as dt

import xarray as xr

import pandas as pd

import uxarray as ux

import numpy as np

from collections import deque

import variables_to_drop as vd

#parallel
import concurrent.futures
import logging
import threading
import time
import queue
import random

def concatenate_month_queue(date,grid,path,header,name,UTC=0,npp=6,variables=[]):
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = ldataset(date,path,grid,header,npp,name,UTC,variables)

    #pipeline = queue.Queue(maxsize=10)
    pipeline = queue.Queue()

    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=npp) as executor:
        for k in range(0,npp):

            executor.submit(producer,pipeline,event,database,k,npp)

    consumer(pipeline,database)

    return database.dataset

def producer(queue, event,database,k,npp):

    #while not event.is_set() or k < npp-1: 

    logging.info("Producer read file: %s---no:%s", database.range[k],k)
    mm=database.read(k)

    #mm = random.randint(1, 101)
    #mm1 = random.randint(1, 101)
    #print(mm)

    queue.put(mm)

    logging.info("Producer received event. Exiting")

def consumer(queue,database):

    #while even.is_set or not queue.empty():
    while not queue.empty():

        mm = queue.get()
        #print('consumer',mmm)

        #logging.info(
        #    "Consumer adding dataset part for a no %s", k
        #)

        database.dataset.append(mm)

    logging.info("Consumer received event. Exiting")


class ldataset:

    def __init__(self,date,path,grid,header,npp,name,UTC,variables):

        self.dataset  = []
        self.path0    = path[0] 
        self.path1    = path[1] 
        self.grid     = grid 
        self.header1  = header[0]
        self.header2  = header[1]
        self.name     = name 
        self.UTC      = UTC 
        self.mm       = [] 

        datei=date[0]
        datef=date[1]
        hours_step=24
        self.dates=gerate_data(datei,datef,hours_step,'%Y%m%d%H')
        self.nd=len(self.dates)
        self.ndays=int(self.nd/(npp))
        self.hours_step=1
        self.range=dates_range(npp,self.nd,self.ndays)
        self.variables=variables

        print(self.range,'rangex')
        #print(self.name)

    def read(self, name):

        logging.info("Thread %s: starting read", name)
        #print(self.range[name])

        nc_files=[]

        for i in self.range[name]: 


            diag=gerate_data_mpas(self.dates[i],self.dates[i+1],self.hours_step,'%Y-%m-%d_%H.%M'+'.00')


            for diagi in diag[0]:
                nc=self.path0+'/%s_%s_%s/'%(self.header1,self.dates[i],self.dates[i+1])+self.path1+'/%s'%(self.header2)+diagi+'.nc'
                nc_files.append(nc)
                #print( nc)

        #exit()

        #print(self.grid)
        #print('hola')
        #print(len(nc_files))
        #print(nc_files[0])
        #mm = ux.open_dataset(self.grid,nc_files[0])


        mm = ux.open_mfdataset(self.grid,nc_files,combine='nested', concat_dim='Time',parallel=False,engine='netcdf4')

        #variables=vd.variables[:]

        #variables=[
        #'edmf_a_isobaric',
        #'edmf_w_isobaric',
        #'edmf_qt_isobaric',
        #'edmf_qc_isobaric',
        #'edmf_thl_isobaric',
        #'edmf_ent_isobaric',
        #'sub_thl_isobaric',
        #'sub_qv_isobaric',
        #'det_thl_isobaric',
        #'det_qv_isobaric',
        #'olrtoa',
        #'refl10cm_max',
        #'refl10cm_1km',
        #'refl10cm_1km_max',
        #'u10',
        #'v10',
        #'q2',
        #'th2m',
        #'mslp',
        #'dewpoint_200hPa',
        #'temperature_200hPa',
        #'height_200hPa',
        #'uzonal_200hPa',
        #'umeridional_200hPa',
        #'w_500hPa',
        #'vorticity_925hPa',
        #'cldfrac_tot_UPP',
        #'cldfrac_isobaric',
        #'rthratenlw_isobaric',
        #'rthratensw_isobaric',
        #'uvel_isobaric',
        #'vvel_isobaric',
        #'zgeo_isobaric',
        #'cape',
        #'cin',
        #'lcl',
        #'lfc',
        #'sst',
        #'xice',
        #'spmt',
        #'sfc_runoff',
        #'udr_runoff',
        #'sms_total',
        #'smois_lys01',
        #'smois_lys02',
        #'smois_lys03',
        #'smois_lys04',
        #'tslb_lys01',
        #'tslb_lys02',
        #'tslb_lys03',
        #'tslb_lys04',
        #'h_pbl',
        #'qke_isobaric',
        #'kzh_isobaric',
        #'kzm_isobaric',
        #'kzq_isobaric',
        #'t02mt',
        #'q02mt',
        #'u10mt',
        #'v10mt',
        #'acrefl10cm_max',
        #'acrefl10cm_1km',
        #'re_cloud_isobaric',
        #'re_ice_isobaric',
        #'qc_isobaric',
        #'qi_isobaric',
        #'qr_isobaric',
        #'qs_isobaric',
        #'qg_isobaric',
        #'ni_isobaric',
        #'nr_isobaric',
        #'nc_isobaric',
        #'rre_cloud_isobaric',
        #'rre_ice_isobaric',
        #'rre_snow_isobaric',
        #'ciwpth_isobaric',
        #'clwpth_isobaric',
        #'cswpth_isobaric',
        #'cldfrac_bl_isobaric',
        #'qc_bl_isobaric',
        #'qi_bl_isobaric',
        #'cov_isobaric',
        #'el_pbl_isobaric',
        #'qke_adv_isobaric',
        #'qsq_isobaric',
        #'tsq_isobaric',
        #'tke_pbl_isobaric',
        #'dqke_isobaric',
        #'qbuoy_isobaric',
        #'qdiss_isobaric',
        #'qshear_isobaric',
        #'qwt_isobaric',
        #'edmf_a_isobaric',
        #'edmf_w_isobaric',
        #'edmf_qt_isobaric',
        #'edmf_qc_isobaric',
        #'edmf_thl_isobaric',
        #'edmf_ent_isobaric',
        #'sub_thl_isobaric',
        #'sub_qv_isobaric',
        #'det_thl_isobaric',
        #'det_qv_isobaric',
        #        ]

        variables=[
        'olrtoa',
        #'refl10cm_max',
        #'refl10cm_1km',
        #'refl10cm_1km_max',
        'u10',
        'v10',
        'q2',
        't2m',
        #'th2m',
        'mslp',
        'dewpoint_200hPa',
        'temperature_200hPa',
        'height_200hPa',
        'uzonal_200hPa',
        'umeridional_200hPa',
        'w_500hPa',
        'vorticity_925hPa',
        'cldfrac_tot_UPP',
        'cldfrac_isobaric',
        'rthratenlw_isobaric',
        'rthratensw_isobaric',
        'uvel_isobaric',
        'vvel_isobaric',
        'zgeo_isobaric',
        #'w_isobaric',
        #'atmt_isobaric',
        'shmt_isobaric',
        'uvmt_isobaric',
        'vvmt_isobaric',
        'ghmt_isobaric',
        'ommt_isobaric',
        'z_isobaric',
        'z_iso_levels',
        'u_iso_levels',
        'cape',
        'cin',
        'lcl',
        'lfc',
        'sst',
        'xice',
        'spmt',
        'sfc_runoff',
        'udr_runoff',
        'sms_total',
        'smois_lys01',
        'smois_lys02',
        'smois_lys03',
        'smois_lys04',
        'tslb_lys01',
        'tslb_lys02',
        'tslb_lys03',
        'tslb_lys04',
        'h_pbl',
        'qke_isobaric',
        'kzh_isobaric',
        'kzm_isobaric',
        'kzq_isobaric',
        'q02mt',
        'u10mt',
        'v10mt',
        #'acrefl10cm_max',
        #'acrefl10cm_1km',
        #'acrefl10cm_1km_max'
                ]

        ##print(variables)

        if self.variables: 
           print('variables drops')
           mm=mm.drop_vars(variables) 

        #print(mm)
        #print('jaklfj')
        ##exit()

        #print(mm.variables)
        ##jjexit()
        #jprint(self.variables)
        #exit()
        mm['name']   = self.name

        mm['netshsf']=mm['acswdnb']-mm['acswupb']

        mm['netlwsf']=mm['aclwdnb']-mm['aclwupb']

        mm['netsf']  =mm['netshsf']-mm['netlwsf']

        ltime=pd.to_datetime(mm.Time)+dt.timedelta(hours=self.UTC)
        ###########################################

        mm['netsf_dw']=mm['acswdnb']-mm['aclwdnb']

        mm['Time']=ltime

        #print(self.variables)

        self.mm = mm

        return mm
        #self.dataset.append(mm)

def concatenate_month_queue_era5(date,path,header,name,UTC=0,npp=6,variables=[]):
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = ldataset_era5(date,path,header,npp,name,UTC,variables)
    pipeline = queue.Queue()

    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=npp) as executor:
        for k in range(0,npp):

            executor.submit(producer,pipeline,event,database,k,npp)

    consumer(pipeline,database)

    return database.dataset

class ldataset_era5:

    def __init__(self,date,path,header,npp,name,UTC,variables):

        self.dataset  = []
        self.path0    = path[0] 
        #self.path1    = path[1] 
        self.header1  = header[0]
        self.header2  = header[1]
        self.name     = name 
        self.UTC      = UTC 
        self.mm       = [] 

        datei=date[0]
        datef=date[1]
        hours_step=24
        self.dates=gerate_data(datei,datef,hours_step,'%Y%m%d%H')
        self.nd=len(self.dates)
        self.ndays=int(self.nd/(npp))
        self.hours_step=3
        self.range=dates_range(npp,self.nd,self.ndays)
        self.variables=variables

        print(self.range,'rangex')

    def read(self, name):

        logging.info("Thread %s: starting read", name)
        #print(self.range[name])

        nc_files=[]

        for i in self.range[name]: 

            diag,hours=gerate_data_mpas(self.dates[i],self.dates[i+1],self.hours_step,'%Y%m%d%H')

            for diagi,hi in zip(diag,hours):
            
                if(hi[0]=='0'):

                    nc=self.path0+'/%s'%(self.header1)+'%s'%(hi)+'%s'%(self.header2)+'.'+diagi+'.grib'
                else:

                    nc=self.path0+'/%s'%(self.header1)+'0%s'%(hi)+'%s'%(self.header2)+'.'+diagi+'.grib'
                nc_files.append(nc)

                
        #dataset = xr.open_dataset(nc_files[1],engine='cfgrib',filter_by_keys={'typeOfLevel': 'isobaricInhPa'})
        dataset = xr.open_dataset(nc_files[0],engine='cfgrib',filter_by_keys={'typeOfLevel': 'surface'})

        print(dataset)
        exit()

        #dataset = xr.open_mfdataset(nc_files,combine='nested', concat_dim='Time',parallel=False,engine='grib')
        #dataset = xr.open_mfdataset(nc_files,concat_dim='time',engine='cfgrib',filter_by_keys={'typeOfLevel': 'surface'})
        #mm=xr.open_mfdataset(nc_files,combine='by_coords', engine='netcdf4')

        #if self.variables: 
        #    print('variables drops')
        #    mm=dataset.drop_vars(self.variables) 

        mm['name']   = self.name

        ltime=pd.to_datetime(mm.Time)+dt.timedelta(hours=self.UTC)
        ###########################################
        mm['time']=ltime

        self.mm = mm


        return mm

def concatenate_month_parallel(date,grid,path,header,name,UTC=0,npp=6):
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = load_dataset(date,path,grid,header,npp,name,UTC)

    #logging.info("Testing update. Starting value is %d.", database.dataset)
    with concurrent.futures.ThreadPoolExecutor(max_workers=npp) as executor:
        for k in range(0,npp):

            executor.submit(database.update, k,database.range)
    #logging.info("Testing update. Ending value is %d.", database.dataset)

    #print(database.dataset)

    return database.dataset


class load_dataset:

    def __init__(self,date,path,grid,header,npp,name,UTC):

        self.dataset  = []
        self._lock    = threading.Lock()
        self.path0    = path[0] 
        self.path1    = path[1] 
        self.grid     = grid 
        self.header1  = header[0]
        self.header2  = header[1]
        self.name     = name 
        self.UTC      = UTC 

        datei=date[0]
        datef=date[1]
        hours_step=24
        self.dates=gerate_data(datei,datef,hours_step,'%Y%m%d%H')
        self.nd=len(self.dates)
        self.ndays=int(self.nd/(npp))
        self.hours_step=1
        self.range=dates_range(npp,self.nd,self.ndays)

        print(self.range,'range')
        #print(self.name)

    def update(self, name,drange):

        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)

        #print(name,ni,ndays) print('name,ni,ndays')

        with self._lock:

            logging.debug("Thread %s has lock", name)

            nc_files=[]

            for i in drange[name]: 

                print(self.dates[i])

                diag=gerate_data_mpas(self.dates[i],self.dates[i+1],self.hours_step,'%Y-%m-%d_%H.%M'+'.00')

                for diagi in diag:
                    nc=self.path0+'/%s_%s_%s/'%(self.header1,self.dates[i],self.dates[i+1])+self.path1+'/%s'%(self.header2)+diagi+'.nc'
                    nc_files.append(nc)

        mm=ux.open_mfdataset(self.grid,nc_files,combine='nested', concat_dim='Time',parallel=False,engine='netcdf4')

        mm['name']   = self.name

        mm['netshsf']=mm['acswdnb']-mm['acswupb']

        mm['netlwsf']=mm['aclwdnb']-mm['aclwupb']

        mm['netsf']  =mm['netshsf']-mm['netlwsf']


        ltime=pd.to_datetime(mm.Time)+dt.timedelta(hours=self.UTC)
        ###########################################

        mm['netsf_dw']=mm['acswdnb']-mm['aclwdnb']

        mm['Time']=ltime

        self.dataset.append(mm)

        logging.debug("Thread %s about to release lock", name)
        logging.debug("Thread %s after release", name)
        logging.info("Thread %s: finishing update", name)


def dates_range(npp,nd,ndays):
    

    ni=0
    y=[]
    for k in range(npp):

        x=[]

        if(k+1==npp):
            lims=nd
        else:
            lims=ndays*(k+1)
        for i in  range(ni,lims): 

            x.append(i)

            ni+=1
        y.append(x)

    return y


def gerate_data(dis,dfs,nhpull,formatdate):
 
     date_format = '%Y%m%d%H%M'
 
     dis=dis
     dfs=dfs
     
     di=dt.datetime.strptime(dis, date_format)
     df=dt.datetime.strptime(dfs, date_format)
 
     d =df-di
     
     nd      =d.days
     month   =di.month
     year    =di.year
 
     date_format_mpas = formatdate 
     
     nh =int(d.total_seconds()//(3600))
 
     deltat=dt.timedelta(hours=int(nhpull))
     
     days=di
 
     #To acumulated 
     ncfiles=[]
     ncdatas=[]
     
     for i in range(0,int(nh)+1,nhpull):   #+1 for the last day 
     
         ncfile=days.strftime(date_format_mpas)
     
         ncfiles.append(ncfile)
 
         ncdatas.append(days)
     
         days=days+deltat
 
 
     return ncfiles 

def generate_data(dis,dfs,nhpull):

    #2014020100
    date_format = '%Y%m%d%H%M'

    #to add the minutes to the original date
    dis=dis+'00'
    dfs=dfs+'00'
    
    di=dt.datetime.strptime(dis, date_format)
    df=dt.datetime.strptime(dfs, date_format)

    d =df-di
    
    nd      =d.days
    month   =di.month
    year    =di.year

    #2014-09-01T20:00:
    date_format_out = '%Y-%m-%dT%H:%M'##+':00.00000000'
    
    nh =int(d.total_seconds()//(3600))

    deltat=dt.timedelta(hours=int(nhpull))
    
    days=di

    #To acumulated 
    ncfiles=[]
    
    for i in range(0,int(nh)+1,nhpull):   #+1 for the last day 
    
        ncfile=days.strftime(date_format_out)
        ncfiles.append(ncfile)
        days=days+deltat

    return ncfiles 

def gerate_data_mpas(dis,dfs,nhpull,formatout):

    #2014-02-01T00:00
    #date_format = '%Y-%m-%dT%H:%M'##+':00.00000000'

    #2014020100
    date_format = '%Y%m%d%H%M'
    #date_format = '%Y-%m-%dT%H:%M'##+':00.00000000'

    #to add the minutes to the original date
    dis=dis+'00'
    dfs=dfs+'00'
    
    di=dt.datetime.strptime(dis, date_format)
    df=dt.datetime.strptime(dfs, date_format)

    d =df-di
    
    nd      =d.days
    month   =di.month
    year    =di.year

    date_format_mpas = formatout#'%Y-%m-%d_%H.%M'+'.00'
    #default='%s/diag.2014-09-02_03.00.00.nc'%path,
    
    nh =int(d.total_seconds()//(3600))

    deltat=dt.timedelta(hours=int(nhpull))
    
    days=di

    #To acumulated 
    ncfiles=[]
    nchours=[]
    ncdatas=[]
    
    for i in range(0,int(nh)+1,nhpull):   #+1 for the last day 
    
        ncfile=days.strftime(date_format_mpas)

        ncfiles.append(ncfile)

        nchours.append(ncfile[8:10])

        ncdatas.append(days)
    
        days=days+deltat


    return ncfiles,nchours
 
    
def concatenate_month_parallellll(date,grid,path,header,name,UTC=0,np=4):

    datei=date[0]
    datef=date[1]
    hours_step=24
    dates=dn.gerate_data(datei,datef,hours_step,'%Y%m%d%H')

    #number of proces
    #np

    nd=len(dates)
    ndays=int(nd/(np))

    hours_step=1

    #to parallel
    xx=[]
    ni=0
    for k in range(0,np):

        nc_files=[]
        #print(ni,ndays+ni)
        #print('pppp')

        for i in  range(ni,ndays+ni): 

            #print(dates[i])
            diag=dn.gerate_data_mpas(dates[i],dates[i+1],hours_step,'%Y-%m-%d_%H.%M'+'.00')
    
            if(k==0):
                nc_files.append(path[0]+'/%s_%s_%s/'%(header[0],dates[i],dates[i+1])+path[1]+'/%s'%(header[1])+diag[0]+'.nc')
    
            for j in range(1,len(diag)): 
    
                nc_files.append(path[0]+'/%s_%s_%s/'%(header[0],dates[i],dates[i+1])+path[1]+'/%s'%(header[1])+diag[j]+'.nc')
    
            ni+=1
        
        mm=ux.open_mfdataset(grid,nc_files,combine='nested', concat_dim='Time',parallel=True,engine='netcdf4')

        mm['name']   = name

        mm['netshsf']=mm['acswdnb']-mm['acswupb']

        mm['netlwsf']=mm['aclwdnb']-mm['aclwupb']

        mm['netsf']  =mm['netshsf']-mm['netlwsf']


        ltime=pd.to_datetime(mm.Time)+dt.timedelta(hours=UTC)
        ###########################################

        mm['netsf_dw']=mm['acswdnb']-mm['aclwdnb']

        mm['Time']=ltime

        xx.append(mm)

    #the rest of process, does not make with the process

    for i in  range(ni,nd-1): 

        diag=dn.gerate_data_mpas(dates[i],dates[i+1],hours_step,'%Y-%m-%d_%H.%M'+'.00')

        for j in range(1,len(diag)): 

            nc_files.append(path[0]+'/%s_%s_%s/'%(header[0],dates[i],dates[i+1])+path[1]+'/%s'%(header[1])+diag[j]+'.nc')

        mm=ux.open_mfdataset(grid,nc_files,combine='nested', concat_dim='Time',parallel=True,engine='netcdf4')

        mm['name']   = name

        mm['netshsf']=mm['acswdnb']-mm['acswupb']

        mm['netlwsf']=mm['aclwdnb']-mm['aclwupb']

        mm['netsf']  =mm['netshsf']-mm['netlwsf']


        ltime=pd.to_datetime(mm.Time)+dt.timedelta(hours=UTC)
        ###########################################

        mm['netsf_dw']=mm['acswdnb']-mm['aclwdnb']

        mm['Time']=ltime

        xx.append(mm)

    return xx

def concatenate_month(date,grid,path,header,name,UTC=0,np=4):

    datei=date[0]
    datef=date[1]
    hours_step=24
    dates=dn.gerate_data(datei,datef,hours_step,'%Y%m%d%H')


    #number of proces
    #np

    nd=len(dates)
    ndays=int(nd/(np))

    hours_step=1

    #to parallel
    xx=[]
    ni=0
    for k in range(0,np):

        nc_files=[]
        #print(ni,ndays+ni)
        #print('pppp')

        for i in  range(ni,ndays+ni): 

            print(dates[i])
            diag=dn.gerate_data_mpas(dates[i],dates[i+1],hours_step,'%Y-%m-%d_%H.%M'+'.00')
    
            if(k==0):
                nc_files.append(path[0]+'/%s_%s_%s/'%(header[0],dates[i],dates[i+1])+path[1]+'/%s'%(header[1])+diag[0]+'.nc')
    
            for j in range(1,len(diag)): 
    
                nc_files.append(path[0]+'/%s_%s_%s/'%(header[0],dates[i],dates[i+1])+path[1]+'/%s'%(header[1])+diag[j]+'.nc')
    
            ni+=1
        
        mm=ux.open_mfdataset(grid,nc_files,combine='nested', concat_dim='Time',parallel=True,engine='netcdf4')

        mm['name']   = name

        mm['netshsf']=mm['acswdnb']-mm['acswupb']

        mm['netlwsf']=mm['aclwdnb']-mm['aclwupb']

        mm['netsf']  =mm['netshsf']-mm['netlwsf']


        ltime=pd.to_datetime(mm.Time)+dt.timedelta(hours=UTC)
        ###########################################

        mm['netsf_dw']=mm['acswdnb']-mm['aclwdnb']

        mm['Time']=ltime

        xx.append(mm)

    #the rest of process, does not make with the process

    for i in  range(ni,nd-1): 

        diag=dn.gerate_data_mpas(dates[i],dates[i+1],hours_step,'%Y-%m-%d_%H.%M'+'.00')

        for j in range(1,len(diag)): 

            nc_files.append(path[0]+'/%s_%s_%s/'%(header[0],dates[i],dates[i+1])+path[1]+'/%s'%(header[1])+diag[j]+'.nc')

        mm=ux.open_mfdataset(grid,nc_files,combine='nested', concat_dim='Time',parallel=True,engine='netcdf4')

        mm['name']   = name

        mm['netshsf']=mm['acswdnb']-mm['acswupb']

        mm['netlwsf']=mm['aclwdnb']-mm['aclwupb']

        mm['netsf']  =mm['netshsf']-mm['netlwsf']


        ltime=pd.to_datetime(mm.Time)+dt.timedelta(hours=UTC)
        ###########################################

        mm['netsf_dw']=mm['acswdnb']-mm['aclwdnb']

        mm['Time']=ltime

        xx.append(mm)

    return xx

def open_uxr(grid,ncfiles,path,header,name,UTC=0):

    nc_files=[path +'/%s'%(header)+ d +'.nc' for d in ncfiles] 
    mm=ux.open_mfdataset(grid,nc_files,combine='nested', concat_dim='Time',parallel=True)

    exit()

    ltime=pd.to_datetime(mm.Time)+dt.timedelta(hours=UTC)


    mm['name']=name

    mm['netshsf']=mm['acswdnb']-mm['acswupb']

    mm['netlwsf']=mm['aclwdnb']-mm['aclwupb']

    mm['netsf']  =mm['netshsf']-mm['netlwsf']

    ##########################################

    mm['netsf_dw']=mm['acswdnb']-mm['aclwdnb']

    mm['Time']=ltime


    return mm

def concatenate_uxr(grid,ncfiles,path,header,name,UTC=0):

    nc_files=[path +'/%s'%(header)+ d +'.nc' for d in ncfiles] 
    #mm=ux.open_mfdataset(grid,nc_files,combine='nested', concat_dim='Time')
    mm=ux.open_mfdataset(grid,nc_files,combine='nested', concat_dim='Time',parallel=True)

    ltime=pd.to_datetime(mm.Time)+dt.timedelta(hours=UTC)


    mm['name']=name

    mm['netshsf']=mm['acswdnb']-mm['acswupb']

    mm['netlwsf']=mm['aclwdnb']-mm['aclwupb']

    mm['netsf']  =mm['netshsf']-mm['netlwsf']

    ##########################################

    mm['netsf_dw']=mm['acswdnb']-mm['aclwdnb']

    mm['Time']=ltime


    return mm

def concatenate(ncfiles,path,header,name,UTC=0):

    nc_files=[path +'/%s'%(header)+ d +'.nc' for d in ncfiles] 

    #nc_files=[]
    #for d in ncfiles:
    #    nc_files=[path +'/%s'%(header)+ d +'.nc' ] 

    #to change the nt64 datetime format
    #data['time']=data['Time'].dt.strftime("%B %d, %Y, %r")
    
    mm=xr.open_mfdataset(nc_files,combine='by_coords', engine='netcdf4')

    ltime=pd.to_datetime(mm.Time)+dt.timedelta(hours=UTC)

    #mm.expand_dims(dim="ltime")

    #mm['ltime']=ltime

    mm['name']=name

    ##########################################

    mm['netshsf']=mm['acswdnb']-mm['acswupb']

    mm['netlwsf']=mm['aclwdnb']-mm['aclwupb']

    mm['netsf']  =mm['netshsf']-mm['netlwsf']

    ##########################################

    mm['netsf_dw']=mm['acswdnb']-mm['aclwdnb']

    mm['Time']=ltime

    return mm

def concatenate_old(di,df,nh,path,header):

    nd  =   df[1]-di[0] 

    month   =di[2]
    year    =di[3]

    if month<10:
        month='0%s'%month

    #number of days to pull 
    nday=1

    #To acumulated 
    ncfiles=[]
    ncdatas=[]

    for i in range(0,nd,nday): 

        dayi=int(di[1])+i

        for k in range(0,24,nh): 

            if k>df[0] and df[1]==dayi:

                break

            if k<10:
                #2023-02-15_00.00.00.nc
                ncfile='%s-%s-0%s_0%s.00.00.nc'%(year,month,dayi,k)
                data='%s-%s-%sT0%s:00'%(year,month,dayi,k)
            else:
                ncfile='%s-%s-0%s_%s.00.00.nc'%(year,month,dayi,k)
                data='%s-%s-%sT%s:00'%(year,month,dayi,k)
    
            ncfiles.append(ncfile)
            ncdatas.append(data)

    nc_files=[path +'/%s'%(header)+ d  for d in ncfiles] 

    mm=xr.open_mfdataset(nc_files,combine='by_coords', engine='netcdf4')

    ####################
    #print(mm.variables)
    ####################

    return mm

def data_day(data,time):

    index=0
    
    for i in range(0,len(time)): 
        #print(data,time[i])
        if(data==time[i]):
            print('index=%s'%(i),data)
            index=i
            break

    if index==0 and i>0:
    	print('Fora de alcance')

    return index
	


	
	

