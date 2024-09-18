# python library to work with netcdf4 
#from    netcdf4         import dataset

# to save the time coordinate in specific format 
from    netCDF4         import num2date, date2num

# Python standard library datetime  module
import datetime as dt  

#Function to know 
#the data interval to make 
#the statitics analysis of that interval.
#CREATED:Jhonatan Aguirre
#Covid19
#Data   :27-04-2020

#In:
#    idi: first data to search  
#    idf: last data to search  
#    data: data arrange

#Out:
#    ni:initial interval data indix
#    ni: final interval data indix

def data_ind(idi,data): 

    #indices achados
    ni=0

    #banderas 
    b1=0

    for i in range(0,data.shape[0]-1):

        if data[i]>=idi and b1==0: 
            ni =i  
            b1 =1
            print("Date found:")
            print("Data1:", data[i],i)

    return ni

def data_n(idi,idf,data): 

    #idi = dt.datetime(2014, 9, 26, 1) 
    #idf = dt.datetime(2014, 10,01, 1) 
    
    #tu = "days  since 2013-12-31"
    #tu = "days  since 2013-12-31 00:00:00 -00:00:00"
    #tc = "gregorian"
    
    #idin=date2num(idi,units=tu,calendar=tc)
    #idfn=date2num(idf,units=tu,calendar=tc)


    #indices achados
    ni=0
    nf=0

    #banderas 
    b1=0
    b2=0

    for i in range(0,data.shape[0]-1):

        if data[i]>=idi and b1==0: 
            ni =i  
            b1 =1
            print("From:")
            print("Data1:", data[i],i)

        if data[i]>=idf and b2==0:  
            nf =i  
            b2 =1
            print("To:")
            print("Data2:", data[i],i) 
    if nf==0:

        nf=data.shape[0]-1

    return ni,nf

def level_n(idi,idf,data): 

    #indices achados
    ni=0
    nf=0

    #banderas 
    b1=0
    b2=0

    for i in range(0,data.shape[0]-1):

        if data[i]>=idi and b1==0: 
            ni =i  
            b1 =1
            print("Level1:", data[i]) 

        if data[i]>=idf and b2==0:  
            nf =i  
            b2 =1
            print("Level2:", data[i]) 

    # To found the maximum date, even 
    # that required date not exists
    if nf==0:

        nf=data.shape[0]-1

    return ni,nf

def pressure_n(idi,idf,data,exp): 

    #indices achados
    ni=0
    nf=0

    #banderas 
    b1=0
    b2=0


    for i in range(0,data.shape[0]-1):

        if(data[i]<=idi and b1==0): 
            #print(data[i],idi,b1)
            ni =i  
            b1 =1
            #print("Level1:", data[i],idi,exp.z[i]) 

        if data[i]<=idf and b2==0:  
            #print(data[i],idf)
            nf =i  
            b2 =1
            #print("Level2:", data[i],exp.z[i]) 
    return ni,nf

def data_n_goa(idi,idf,data): 

    #idi = dt.datetime(2014, 9, 26, 1) 
    #idf = dt.datetime(2014, 10,01, 1) 
    
    #tu = "days  since 2013-12-31"
    tu = "days  since 2013-12-31 00:00:00 +04:00:00"
    tc = "gregorian"
    
    idin=date2num(idi,units=tu,calendar=tc)
    idfn=date2num(idf,units=tu,calendar=tc)

    #indices achados
    ni=0
    nf=0

    #banderas 
    b1=0
    b2=0

    for i in range(0,data.shape[0]-1):

        if data[i]>=idi and b1==0: 
            ni =i  
            b1 =1
            print("Data1:", data[i]) 

        if data[i]>=idf and b2==0:  
            nf =i  
            b2 =1
            print("Data2:", data[i]) 
    
    return ni,nf

#To put the differents datas in the 
#same reference hours, to plot in the same 
#graph

def data_to_reference(data,day_0,year): 

    i=0

    
    data_ref = data

    #to change the month, if 0 does change
    month_0= 0

    for d in data:

        month   =   d.month-month_0
        day     =   d.day-day_0
        hour    =   d.hour 
        minute  =   d.minute 
        second  =   d.second 
        micro   =   d.microsecond


        data_ref[i] =   dt.datetime( year ,month,day,hour,minute, second,micro)

        i=i+1

    return data_ref 

def data_all(data,k): 

    i=0

    if k>31:
        m=m+1
        k=k-31

    data_ref = data

    mm=1
    dd=k+1

    day_ant=0

    for d in data:

        day     =   d.day 
        hour    =   d.hour 
        minute  =   d.minute 
        second  =   d.second 
        micro   =   d.microsecond


        if day!=day_ant and i>0:
            dd+=1
            hour=0
            #print d

        #TO NOT PASS OF THE DAY
        #if hour>23 and minute >59 :
        #    #break

        data_ref[i] =   dt.datetime( 2022 ,mm,dd,hour,minute, second,micro)

        day_ant=day
        i=i+1

    return data_ref 
