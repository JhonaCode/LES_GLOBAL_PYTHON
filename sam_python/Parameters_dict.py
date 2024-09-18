########################################################
#File to define the direction of the SAM runs.
########################################################

### My own files

##Adress of the computer
from     files_direction  import *

import   sam_python.var_files.var_to_load_sam_lasso  as var_l

########################################################
#Files of SAM to load.
########################################################

var        = [ 
               'MCUP'  , 'CLD' , 'TKE' , 
               'TVFLUX', 'WOBS', 'RELH',  
               'QC'    , 'Q1C' , 'Q2',  
             ]
var        = [ 
              'MCUP' 
             ]
calendar   = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']

name       = 'lasso_060615'
file1      = '%s/DADOS/raw_model/sgp20150606_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
data       = [(2015,6,6,9),(2015,6,6,18)]
f060615    =  var_l.ncload(name,data,file1,calendar, var)

name       = 'lasso_090615'
file1      = '%s/DADOS/raw_model/sgp20150606_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
file2   =   '%s/DADOS/raw_model/sgp20150609_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2015,6,9,9),(2015,6,9,18)]
f090615 = var_l.ncload(name,data,file2,calendar,var)

name       = 'lasso_270615'
file3   =   '%s/DADOS/raw_model/sgp20150627_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2015,6,27,9),(2015,6,27,18)]
f270615 = var_l.ncload(name,data,file3,calendar,var)

name       = 'lasso_010815'
file4   =   '%s/DADOS/raw_model/sgp20150801_alpha1r.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2015,8,1,9),(2015,8,1,18)]
f010815 = var_l.ncload(name,data,file4,calendar,var)

name       = 'lasso_290815'
file5   =   '%s/DADOS/raw_model/sgp20150829_rerun2020.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2014-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2015,8,29,9),(2015,8,29,18)]
f290815 = var_l.ncload(name,data,file5,calendar,var)

file6   =   '%s/DADOS/raw_model/sgp20160518_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2016,5,18,9),(2016,5,18,18)]
f180516 = var_l.ncload(name,data,file6,calendar,var)

file7   =   '%s/DADOS/raw_model/sgp20160530_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2016,5,30,9),(2016,5,30,18)]
f300516 = var_l.ncload(name,data,file7,calendar,var)

file8   =   '%s/DADOS/raw_model/sgp20160614_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2016,6,14,9),(2016,6,14,18)]
f140616 = var_l.ncload(name,data,file8,calendar,var)

file9   =   '%s/DADOS/raw_model/sgp20160625_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2016,6,25,9),(2016,6,25,18)]
f250616 = var_l.ncload(name,data,file9,calendar,var)

file10  =   '%s/DADOS/raw_model/sgp20160716_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2016,7,16,9),(2016,7,16,18)]
f160716 = var_l.ncload(name,data,file10,calendar,var)

file11  =   '%s/DADOS/raw_model/sgp20160719_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2016,7,19,9),(2016,7,19,18)]
f190716 = var_l.ncload(name,data,file11,calendar,var)

file12  =   '%s/DADOS/raw_model/sgp20160720_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2016,7,20,9),(2016,7,20,18)]
f200716 = var_l.ncload(name,data,file12,calendar,var)

file13  =   '%s/DADOS/raw_model/sgp20160819_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2016,8,19,9),(2016,8,19,18)]
f190816 = var_l.ncload(name,data,file13,calendar,var)

file14 =   '%s/DADOS/raw_model/sgp20160830_alpha2.varanal_300km_25mb_ls.varanal_300km_25mb_sf.sonde_init.144.nc'%(computer)
calendar = ["days  since 2015-12-31 00:00:00 +06:00:00",'gregorian']
data       = [(2016,8,30,9),(2016,8,30,18)]
f300816 = var_l.ncload(name,data,file14,calendar,var)

