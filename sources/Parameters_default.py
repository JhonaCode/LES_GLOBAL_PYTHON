import  os,sys
import cartopy.crs as ccrs
MODEL='MPAS'

plotdef='2d'
#Latex width 
wf=0.33
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

egeon='/pesq'

UTC=-4

path=egeon+'/dados/bamc/jhonatan.aguirre/git_repositories/MPAS_shca' 

# Out figure folder
out_fig=path+'/document/fig_sep02'

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
