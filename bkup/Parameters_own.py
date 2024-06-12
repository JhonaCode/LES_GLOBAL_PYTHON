# Function to load the ncfiles
import xarray as xr

import  source.var_load_era5 as e5 

path='/dados/bamc/liviany.viana/era5'

#
#Feb      = '%s/day/feb_1960a2023_anomaly.nc'%(path)
#feb_mean =  xr.open_dataset(Feb)
#
#
#Feb_rain      = '%s/day/rain_feb_era5.nc'%(path)
#feb_rain      =  xr.open_dataset(Feb_rain)

#Feb   = '%s/day/fev_2023.nc'%(path)
#feb   =  xr.open_dataset(Feb)



#out_folder='/home/jhona/repositories/robin/bloking/document/bloking/figs/' 
out_fig='/home/jhonatan.aguirre/git_report/mpas/document/fig/'
out_files='%s/day'%(path)

