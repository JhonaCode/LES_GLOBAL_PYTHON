import datetime as dt

import xarray as xr

import pandas as pd

import uxarray as ux

import numpy as np

from collections import deque

###import variables_to_drop as vd

import threading

import concurrent.futures

import queue

import logging

# Global counter and lock
completed_lock = threading.Lock()
completed = 0  # will reset per function call

# Progress bar function
def update_progress_bar(total_tasks, bar_length=30):
    global completed
    with completed_lock:
        completed += 1
        percent = completed / total_tasks
        filled = int(bar_length * percent)
        bar = "#" * filled + "-" * (bar_length - filled)
        print(f"\r[{bar}] {percent*100:.1f}%", end="")
        if completed == total_tasks:
            print()  # new line at 100%


def producer(queue, database, k, total_tasks):
    try:
        mm = database.read(k)
        queue.put(mm)
    finally:
        update_progress_bar(total_tasks)

# Consumer function
def consumer(queue, database, n_tasks):
    finished_producers = 0
    while True:
        item = queue.get()
        if item is None:  # sentinel
            finished_producers += 1
            if finished_producers == n_tasks:
                break
            else:
                continue
        database.dataset.append(item)

# Main function
def concatenate_month_queue(date, grid, path, header, name, UTC=0, npp=6, variables=[]):
    global completed
    completed = 0  # reset counter for each function call

    print(f"Reading and concatenating files of {name}")
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")

    database = ldataset(date, path, grid, header, npp, name, UTC, variables)
    pipeline = queue.Queue()

    # Determine actual number of tasks to avoid IndexError
    n_tasks = len(database.range)
    if n_tasks == 0:
        print("No files to read.")
        return database.dataset

    # Limit number of threads to available tasks
    npp = min(npp, n_tasks)

    # Submit producer tasks for valid indices only
    with concurrent.futures.ThreadPoolExecutor(max_workers=npp) as executor:
        for k in range(n_tasks):
            executor.submit(producer, pipeline, database, k, n_tasks)

    # Add sentinels for consumer
    for _ in range(n_tasks):
        pipeline.put(None)

    # Start consumer
    consumer(pipeline, database, n_tasks)

    print("End of Reading")
    return database.dataset

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

        #print(self.range,'rangex')
        #print(self.name)

    def read(self, name):

        #logging.info("Thread %s: starting read", name)
        #print(self.range[name])

        nc_files=[]

        for i in self.range[name]: 


            diag=gerate_data_mpas(self.dates[i],self.dates[i+1],self.hours_step,'%Y-%m-%d_%H.%M'+'.00')


            for diagi in diag[0]:
                nc=self.path0+'/%s_%s_%s/'%(self.header1,self.dates[i],self.dates[i+1])+self.path1+'/%s'%(self.header2)+diagi+'.nc'
                nc_files.append(nc)
                #print( nc)

        # Get a list of all variables in the first file
        #all_vars = list(xr.open_dataset(nc_files[0], engine='netcdf4').variables)
        
        # Compute variables to drop
        #drop_vars = [v for v in all_vars if v not in self.variables] 

        #print(drop_vars)

        mm = ux.open_mfdataset(
                                self.grid,
                                nc_files,
                                combine='nested', 
                                concat_dim='Time',
                                parallel=False,
                                engine='netcdf4',
                                drop_variables=self.variables,
                                #drop_variables=drop_vars,
        )

        #if self.variables: 
        #   #print('variables drops')
        #   mm=mm.drop_vars(self.variables) 

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

        #print(self.range,'rangex')

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

        #print(self.range,'range')
        #print(self.name)

    def update(self, name,drange):

        logging.info("Thread %s: starting update", name)
        logging.debug("Thread %s about to lock", name)

        #print(name,ni,ndays) print('name,ni,ndays')

        with self._lock:

            logging.debug("Thread %s has lock", name)

            nc_files=[]

            for i in drange[name]: 

                #print(self.dates[i])

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
	


	
	

