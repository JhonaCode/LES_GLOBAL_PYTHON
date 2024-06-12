# Function to load the ncfiles
import xarray as xr

import  source.var_load_era5 as e5 

import pygrib                        # Provides a high-level interface to the ECWMF ECCODES C library for reading GRIB files

import iris as ir
#import iris_grib as ir

import os


path='/dados/bamc/public_pablo/PAPER_EE23/models/BAM' 

path2='/dados/bamc/public_nilo/EXP_goAMZ_MOA/Exp3cp_paraMoa/201410/2014101012'

#bam15   = '%s/2023021500/GPOSNMC20230215002023021500P.fct.TQ0666L064.grb'%(path)
bam15   = '%s/2023021800/GPOSNMC20230218002023021918P.fct.TQ0666L064.grb'%(path)

#grib = pygrib.open(bam15)

bam16   = '%s/GPOSCPT20141010122014101209P.fct.TQ0299L064'%(path2)

grib = pygrib.open(bam16)


#ds = xr.open_dataset(bam16,engine='cfgrib')
#ds = xr.open_dataset(bam16,engine='cfgrib', backend_kwargs={'indexpath':'/dados/bamc/public_jhona/{short_hash}.idx','errors': 'ignore'})


#
#print(grib)

#exit()

f = open("variables.txt", "w") # Create and open the file

for variables in grib:
    # Put the variables in the txt file
    print(variables, file=f)
    # Print the variables in the terminal
    print(variables)

f.close()
#
exit()

#grbs.seek(0)
#for grb in grbs:
#    print(grb)


#print(selected_grb)

#exit()




#bam15   = '%s/2023021600/'%(path)
#bam15   = '%s/2023021500/GPOSNMC2023021500P.fct.TQ0666L064.idx'%(path)
#bam15   =  xr.open_dataset(bam15)

#ds = xr.open_dataset(bam15,engine='cfgrib', backend_kwargs={'indexpath':'/dados/bamc/public_jhona/{short_hash}.idx','errors': 'ignore'})
#ds = xr.open_dataset(bam15, backend_kwargs={'indexpath':'/dados/bamc/public_jhona/{short_hash}.idx'})


#ds = xr.open_mfdataset("*.grib", engine="cfgrib", backend_kwargs={"/dados/bamc/public_jhona/": 'writable_folder{path}.{short_hash}.idx'})

# Read in some data within a constrained timeframe
#startyr = 2003
#endyr = 2014
#nyear = endyr-startyr+1
#constraint = ir.Constraint(time=lambda cell:
#                             startyr <= cell.point.year <= endyr)
#    
## Set data_path to location of files
##data_path = str(os.getcwd()) + bam15
#data_path =  bam15
#
#print(data_path)
#
## precipitation
#pre = ir.load_cube(data_path,'Relative humidity')
#                     #constraint=constraint)
#print(pre)
#
#exit()
#
#
#cubes = ir.load(bam15)
#print(cubes)
#print(cubes['Relative humidity'])
#
#exit()
#cubes = ir.load_cubes(bam15)
#
#ir.save_grib2(cubes, 'my_file.grib2')
#
#cubes=list(cubes)
#print(cubes)
##print(cubes.pressure)
#exit()
#print(ds)
#
#exit()




#out_folder='/home/jhona/repositories/robin/bloking/document/bloking/figs/' 
out_fig='/home/jhonatan.aguirre/git_report/mpas/document/fig/'
out_files='%s/day'%(path)

