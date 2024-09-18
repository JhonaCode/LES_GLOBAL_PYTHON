import os

#Repository location 
computer   = '/home/jhona'

#Figure out folder  
path = "%s/git_repositories/goamazon_ccpp/doc/fig"%(computer)

# Check if the directory exists
if not os.path.exists(path):
    # If it doesn't exist, create it
    os.makedirs(path)


file_fig= path
file_temporal= path


#Size in inches to make the temporal plots
tplot_size=1.0
