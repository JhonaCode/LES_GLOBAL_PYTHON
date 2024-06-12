#!/usr/bin/env python

'''
**************************
Program Download the data of ERA5 to run de MPAS 

#################################################
To run:

Define :
    INITIAL DATA  
        datain ='1995010100'
    FINAL DATA  
        datain ='1995010123'
    Path to save the data 
        path= '/pwd'

#################################################
Before run the first time :

    *see: https://cds.climate.copernicus.eu/api-how-to

    *https://github.com/joaohenry23/Download_ERA5_with_python


    1) Go to  CDS registration page and make the sing in 

        creates the file $HOME/.cdsapirc


    2) Get the uid and api-key in your login information, CLick in your name upper rigth conner 

        Copy the next code within .cdsapirc
        url: https://cds.climate.copernicus.eu/api/v2
        key: uid:api-key 

    3) Install pytho lib of era5: pip install cdsapi 

#################################################
Data:25-04-24
Created by: Jhonatan A. A. Manco
**************************
python 3.9

'''

import  os,sys


import  dfunctions as df 

path='/dados/bamc/jhonatan.aguirre/DATA/ERA5/'

name='goamazon_south_america'

#iop1
datain ='2014020100'
datafi='2014033023'

#iop2
#datain ='2014081500'
#datafi ='2014103123'

#Directory
dire='%s/%s'%(path,name)

#Directory 2
# Check if the directory exists
if not os.path.exists(dire):
    # If it doesn't exist, create it
    os.makedirs(dire)

#df.download_4lev('temperature'        ,name,datain,datafi,dire)
#
#df.download_4lev('geopotential'             ,name,datain,datafi,dire)
#df.download_4lev('vertical_velocity'        ,name,datain,datafi,dire)
#df.download_4lev('fraction_of_cloud_cover'  ,name,datain,datafi,dire)
#
#df.download_15lev('u_component_of_wind'      ,name,datain,datafi,dire)
#df.download_15lev('v_component_of_wind'      ,name,datain,datafi,dire)
#df.download_15lev('relative_humidity'        ,name,datain,datafi,dire)
#df.download_15lev('specific_humidity'        ,name,datain,datafi,dire)

df.download_sfclev('vertical_integral_of_eastward_water_vapour_flux'   ,name,datain,datafi,dire)
df.download_sfclev('vertical_integral_of_northward_water_vapour_flux'  ,name,datain,datafi,dire)


#df.download_sfclev('surface_latent_heat_flux'   ,name,datain,datafi,dire)
#df.download_sfclev('surface_sensible_heat_flux' ,name,datain,datafi,dire)
#df.download_sfclev('total_precipitation'        ,name,datain,datafi,dire)
#df.download_sfclev('convective_precipitation'   ,name,datain,datafi,dire)
#df.download_sfclev('large_scale_precipitation'  ,name,datain,datafi,dire)
#df.download_sfclev('total_cloud_cover'  ,name,datain,datafi,dire)
#df.download_sfclev('low_cloud_cover'    ,name,datain,datafi,dire)
#df.download_sfclev('medium_cloud_cover' ,name,datain,datafi,dire)
#df.download_sfclev('high_cloud_cover'  ,name,datain,datafi,dire)
#df.download_sfclev('cloud_base_height'  ,name,datain,datafi,dire)
#df.download_sfclev('vertically_integrated_moisture_divergence' ,name,datain,datafi,dire)
