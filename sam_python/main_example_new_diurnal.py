import numpy as np

import matplotlib.pyplot as plt

import netCDF4 as nc
#from metpy.units import *
#from metpy.calc import density
from  scipy.special import gamma

#import h5py,bokeh,seaborn,dask,distributed
#import notebook,pandas,xarray,graphviz,pandas_datareader
import xarray as xr


data_path=''


nc_fit=nc.Dataset(data_path+'wrfout_d01_2019-05-18_02:00:00.nc')

data_inf= ncdump(nc_fit)
# Load the Drive helper and mount


# open a single file, just as an example
ncfile = xr.open_dataset(data_path+'wrfout_d01_2019-05-18_02:00:00.nc')

# number of variables in the file
print('Number of variables = ', len(ncfile.variables))

# summary of the file content
ncfile.keys()


# list the variables in the file (long list)
list(ncfile.variables)

# only the first 20 variables
#list(ncfile.variables)[:20]


# get the temperature
T2 = ncfile['T2']
# and print its dimensions
print(T2.shape)
np.unique(T2)


# plot last time of the first file (~ 1h).
# this should be after 1h of simulation. Because LES is initialized with uniform
# fields, the initial differences are very small.
cf = plt.pcolormesh(T2[0,:,:] - 273.15)
plt.xlabel('x [grid points]')
plt.ylabel('y [grid points]')
plt.title('T-2m [degC]')
plt.colorbar(cf)



plt.title('Cloud Fraction ')

plt.subplot(3, 2, 1)

plt.xlabel('x [grid points]')
plt.ylabel('y [grid points]')
cf = plt.pcolormesh(CLD[40,50,:,:] )

plt.subplot(3, 2, 2)
cf = plt.pcolormesh(CLD[45,50,:,:] )

plt.subplot(3, 2, 3)
cf = plt.pcolormesh(CLD[50,50,:,:] )

plt.subplot(3, 2, 4)
cf = plt.pcolormesh(CLD[55,50,:,:] )

plt.subplot(3, 2, 5)
cf = plt.pcolormesh(CLD[60,50,:,:] )

plt.subplot(3, 2, 6)
cf = plt.pcolormesh(CLD[65,50,:,:] )

#plt.subplot(3, 3, 1)
#plt.colorbar(cf)


cf = plt.pcolormesh(CLD[45,50,:,:] )
plt.xlabel('x [grid points]')
plt.ylabel('y [grid points]')
plt.title('Cloud Fraction ')
plt.colorbar(cf)


# now let's open all the files

# these files are not CF-compliant, so we have to force concatenation on the time dimension
ncfile = xr.open_mfdataset(data_path+'wrfout_d01_2019-05-*.nc', combine='nested', concat_dim='Time',decode_cf=False)


from pickle import TUPLE3
# what do we have now?

T2  = ncfile['T2']
CLD = ncfile['CLDFRA']

np.shape(T2)
#T2
