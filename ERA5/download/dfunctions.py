#!/usr/bin/env python

import cdsapi

c = cdsapi.Client()

def download_15lev(var,name,datain,datafi,dire):

    name   ='era5.%s.%s_%s-%s'%(var,name,datain,datafi) 
    c.retrieve("reanalysis-era5-pressure-levels",
    {
    "variable": var,
    
    "pressure_level": [
                        '1000', 
                        '950' , 
                        '900' , 
                        '850' , 
                        '800' , 
                        '750' , 
                        '700' , 
                        '650' , 
                        '600' , 
                        '550' , 
                        '500' , 
                        '450' , 
                        '400' , 
                        '300' , 
                        '250' , 
                      ],
    'area': [
            15, -90, -60,
            -30,
        ],
    "product_type": "reanalysis",
    "year"  : "%s"%(datain[0:4]),
    'month':[
            datain[4:6], datafi[4:6],
            ],
    "day":  [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
            ],
    "time": [
                '00:00',
                '04:00',
                '08:00',
                '12:00',
                '16:00',
                '20:00',
        ],
    "format": "netcdf"
    }, "%s/%s.nc"%(dire,name))

    return 

def download_4lev(var,name,datain,datafi,dire):

    name   ='era5.%s.%s_%s-%s'%(var,name,datain,datafi) 

    c.retrieve("reanalysis-era5-pressure-levels",
    {
    "variable": var,
    
    "pressure_level": [
                        '1000', 
                        '850' , 
                        '500' , 
                        '250' , 
                      ],
    'area': [
            15, -90, -60,
            -30,
        ],
    "product_type": "reanalysis",
    "year"  : "%s"%(datain[0:4]),
    'month':[
            datain[4:6], datafi[4:6],
            ],
    "day":  [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
            ],
    "time": [
                '00:00',
                '04:00',
                '08:00',
                '12:00',
                '16:00',
                '20:00',
        ],
    "format": "netcdf"
    }, "%s/%s.nc"%(dire,name))

    return 

def download_sfclev(var,name,datain,datafi,dire):

    name   ='era5.%s.%s_%s-%s'%(var,name,datain,datafi) 

    c.retrieve("reanalysis-era5-single-levels",
    {
    "variable": var,
    'area': [
            15, -90, -60,
            -30,
        ],
    "product_type": "reanalysis",
    "year"  : "%s"%(datain[0:4]),
    'month':[
            datain[4:6], datafi[4:6],
            ],
    "day":  [
            '01', '02', '03',
            '04', '05', '06',
            '07', '08', '09',
            '10', '11', '12',
            '13', '14', '15',
            '16', '17', '18',
            '19', '20', '21',
            '22', '23', '24',
            '25', '26', '27',
            '28', '29', '30',
            '31',
            ],
    "time": [
                '00:00',
                '04:00',
                '08:00',
                '12:00',
                '16:00',
                '20:00',
        ],
    "format": "netcdf"
    }, "%s/%s.nc"%(dire,name))

    return 

def download_lev_mpas(var,vname,vnum,datain,dataout,dire):

    name   ='e5.oper.an.pl.128_%s_%s.ll025sc.%s_%s'%(vname,vnum,datain,dataout) 
    c.retrieve("reanalysis-era5-pressure-levels",
    {
    "variable": var,
    
    "pressure_level": [
                        '1000', '975', '950', '925', '900',
                        '875' , '850', '825', '800', '775',
                        '750' , '700', '650', '600', '550', 
                        '500' , '450', '400', '350', '300',
                        '250' , '225', '200', '175', '150', 
                        '125' , '100', '70' , '50' , '30' , 
                        '20'  , '10' , '7'  , '5'  , '3'  , 
                        '2'   , '1'  ,
                      ],
    "product_type": "reanalysis",
    "year"  : "%s"%(datain[0:4]),
    "month" : "%s"%(datain[4:6]),
    "day"   : "%s"%(datain[6:8]),
    "time"  : "%s:00"%(datain[8:10]),
    "format": "grib"
    }, "%s/%s.grb"%(dire,name))

    return 

def download_sfc_mpas(var,vname,vnum,datain,dataout,dire):

    name   ='e5.oper.an.sfc.128_%s_%s.ll025sc.%s'%(vname,vnum,datain) 
    c.retrieve("reanalysis-era5-single-levels",
    {
    "variable": var,
    "product_type": "reanalysis",
    "year"  : "%s"%(datain[0:4]),
    "month" : "%s"%(datain[4:6]),
    "day"   : "%s"%(datain[6:8]),
    "time"  : "%s:00"%(datain[8:10]),
    "format": "grib"
    }, "%s/%s.grb"%(dire,name))

    return 
