#IN
#data: my data
#time: Time vectors with data.
#Out
#index

import datetime as dt

import xarray as xr

import pandas as pd

import uxarray as ux


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
    
        print(i)
        ncfile=days.strftime(date_format_out)
        ncfiles.append(ncfile)
        days=days+deltat

    return ncfiles 

def gerate_data_mpas(dis,dfs,nhpull):

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

    date_format_mpas = '%Y-%m-%d_%H.%M'+'.00'
    #default='%s/diag.2014-09-02_03.00.00.nc'%path,
    
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

def concatenate_uxr(grid,ncfiles,path,header,name,UTC=0):

    nc_files=[path +'/%s'%(header)+ d +'.nc' for d in ncfiles] 


    #mm=ux.open_mfdataset(grid,nc_files,combine='nested', concat_dim='time')
    mm=ux.open_mfdataset(grid,nc_files,combine='nested', concat_dim='Time')

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
	
	
	


	
"""
    #number of days to pull 
    nday=1

    #To acumulated 
    ncfiles=[]
    ncdatas=[]

    nf=int(nd)*24/int(nh)


    date_format_mpas = '%Y-%m-%d_%H.%M'+'.00'
    deltat=dt.timedelta(hours=int(nh))

    days=di

    for i in range(0,int(nf)): 
"""
	
	
	
	

