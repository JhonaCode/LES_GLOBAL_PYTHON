import  os,sys

import cartopy.crs as ccrs
plotdef='mapa1'
#Latex width 
wf=0.7
hf=1.0
cmmais=0.0
#plot size of the figures
#cmmais are the cm to put the cbbar  without modified the size of the fig
projection=ccrs.PlateCarree(central_longitude=180.0, globe=None)
#############plot formated
# make the map global rather than have it zoom in to
# the extents of any plotted data
###################################3
#skip poitnt in vector plot
npp=10

extend='both'

#Path to the files 
path='/dados/bamc/jhonatan.aguirre/DATA/ERA5/goamazon_south_america' 

# Out figure folder
out_fig='/dados/bamc/jhonatan.aguirre/git_repositories/ERA_python/document/fig'

#out python nc files
out_files= path+'/python_nc'

# Check if the directory exists
if not os.path.exists(out_fig):
    # If it doesn't exist, create it
    os.makedirs(out_fig)

# Check if the directory exists
if not os.path.exists(out_files):
    # If it doesn't exist, create it
    os.makedirs(out_files)
