import numpy as np
import xarray as xr
import datetime as dt
import pandas as pd

def mean_hours_xr(data,name,day):

    """
    data=data to mean 
    day =day of the new metric in a reference time.
    """

    hour =[0,4,8,12,16,20]
    hours=['00','04','08','12','16','20',]

    var=[]

    k=0
    for j in hour: 

        time='%sT%s:00'%(day,hours[k])
        dd = dt.datetime.strptime(time,"%Y-%m-%dT%H:%M")
        dd = pd.to_datetime(dd) 

        tomean=data.sel(time=data.time.dt.hour.isin([j]),method='nearest')
        mean= tomean.mean(dim='time')
        mean= mean.assign_coords(time = dd)
        mean= mean.expand_dims(dim="time")

        #print(mean)
        #exit()
        ##if k==0:
        ##    #print(data.time.dt.hour.isin([j]))
        ##    var=mean
        ##else:
        ###    #var.append(mean)
        ###    #var.concatenate(mean)
        ###    xr.concat(var,mean)

        var.append(mean)

        k+=1

    var = xr.combine_by_coords(var)

    var['name'] = name

    return var

def shallow_xarray(data,days):

    dates=[]

    hour=['00','04','08','12','16','20']

    for i in days:

        for j in hour: 
        
            date_format = '%Y-%m-%dT%H'

            dt_obj=dt.datetime.strptime( '2014-'+i+'T'+j,date_format,) 

            date_obj='2014-'+i+'T'+(j)

            dates.append(date_obj)


    var= data.sel(time=dates,method='nearest')

    #print('creating %s.nc ........... '%(name))
    #var.to_netcdf('%s/%s.nc'%(out_files,name))

    return var

def season_xarray(data,var,lats,lons,levs):

    #summer = var.sel(time=var.time.dt.month.isin([1, 2, 12]))
    #autum  = var.sel(time=var.time.dt.month.isin([3, 4, 5]))
    #winter = var.sel(time=var.time.dt.month.isin([6, 7, 8]))
    #spring = var.sel(time=var.time.dt.month.isin([9, 10, 11]))
    feb    = var.sel(time=var.time.dt.month.isin([2]))

    dd = xr.Dataset(
             data_vars={
                        #'summer':(['timesummer','lev','latitude','longitude'],summer.data),
                        #'winter':(['timewinter','lev','latitude','longitude'],winter.data),
                        #'autum':(['timeautum ' ,'lev','latitude','longitude'],autum.data),
                        #'spring':(['timespring','lev','latitude','longitude'],spring.data),
                        'feb':(['time','levs','latitude','longitude'],feb.data),
                        },
             coords={
             'latitude'   :lats.data,
             'longitude'  :lons.data,
             'levs':levs.data,
             'time':feb.time.data,
             #'timesummer':summer.time.data,
             #'timewinter':winter.time.data,
             #'timeautum': autum.time.data,
             #'timespring':spring.time.data,
             },
        )

    return dd

def anom(index1,index2,data,lats,lons):

	anomalia=np.zeros((index2-index1,len(lats),len(lons)))
	anualmedia=np.mean(data[index1:index2,:,:],axis=0)

	j=0
	for i in range(index1,index2):

		anomalia[j,:,:] = data[i,:,:] - anualmedia[:,:]
		j+=1

	return anomalia
	

def anom2(data,time):

    media=np.mean(data,axis=0)
    std=np.std(data,axis=0)
    
    #anomalia = (datatoanom-media)

    anomalia = (data-media)/std


    return anomalia,media,std

def anom_xarray(data,dim):


    #media=np.mean(data,axis=0)
    mean=data.mean(dim='time')
    std=np.std(data,axis=0)




    #anomalia = (data-data.mean(dim='%s'%(dim)))
    anomalia = (data-mean)/std
    #anomalia = (data-mean)
    dd = xr.Dataset(
             data_vars={'anomaly':(['time','levs','latitude','longitude'],anomalia.data),
                        'mean_time':(['levs','latitude','longitude'],mean.data),
                   'standart_deviation':(['lev.','latitude','longitude'],std.data)
                        },
             coords={
             'latitude':data.latitude.data,
             'longitude':data.longitude.data,
             'levs':data.levs.data,
             'time':data.time.data,
             },
             #name='dsummer'
        )
    
    return dd#,anomalia,media,std

    #anomalia > 0 = chuva maior que a media
    #anomali < 0 = seca
    #

