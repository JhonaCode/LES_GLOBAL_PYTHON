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

import sources.data_own  as dn

#parallel
import concurrent.futures
import logging
import threading
import time
import queue

"""
def producer(queue, event,database,npp):

    while not event.is_set():

        #message = random.randint(1, 101)
        for k in range(0,npp):

            executor.submit(database.update, k,database.range)

        logging.info("Producer got message: %s", message)
        queue.put(message)

    logging.info("Producer received event. Exiting")

def consumer(queue, event):
    """Pretend we're saving a number in the database."""
    while not event.is_set() or not queue.empty():
        message = queue.get()
        logging.info(
            "Consumer storing message: %s (size=%d)", message, queue.qsize()
        )

    logging.info("Consumer received event. Exiting")


def concatenate_month_queue(date,grid,path,header,name,UTC=0,npp=6):
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    database = load_dataset(date,path,grid,header,npp,name,UTC)

    pipeline = queue.Queue(maxsize=10)

    event = threading.Event()

    with concurrent.futures.ThreadPoolExecutor(max_workers=npp) as executor:
        for k in range(0,npp):

            executor.submit(producer,pipeline,event,database)
            executor.submit(consumer,pipeline,event,database)

            logging.info("Main: about to set event")
            event.set()

    return database.dataset
"""


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

    print(database.dataset)

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
        self.dates=dn.gerate_data(datei,datef,hours_step,'%Y%m%d%H')
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

                diag=dn.gerate_data_mpas(self.dates[i],self.dates[i+1],self.hours_step)

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

            print(dates[i])
            diag=dn.gerate_data_mpas(dates[i],dates[i+1],hours_step)
    
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

        diag=dn.gerate_data_mpas(dates[i],dates[i+1],hours_step)

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
            diag=dn.gerate_data_mpas(dates[i],dates[i+1],hours_step)
    
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

        diag=dn.gerate_data_mpas(dates[i],dates[i+1],hours_step)

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
	


	
	

