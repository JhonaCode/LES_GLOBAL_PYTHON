########################################################
#File to define the direction of the SAM runs.
########################################################

### My own files

##Adress of the computer
from     files_direction_example1  import *

import   sam_python.var_files.var_to_load_ccpp  as ccpp

########################################################
#Files of SAM to load.
########################################################

var2d      = ['ql','T','w_ls']
var        = ['shf','lhf', 'tprcp_inst']


#Make the first dictionary 
name       = 'goamazon_iop1'
file1      = '%s/git_repositories/ccpp-scm/scm/run/output_goamazon_iop1_A_SCM_GFS_v16/output.nc'%(computer)
data       = [(2014,2,15,0),(2014,3,10,0)]
cal        = ["seconds  since 2014-2-15 00:00:00 +00:00:00",'gregorian']
goa1       = ccpp.ncload(name,data,file1,cal,var,var2d) 

name       = 'goamazon_iop2'
file2      = '%s/git_repositories/ccpp-scm/scm/run/output_goamazon_iop2_A_SCM_GFS_v16/output.nc'%(computer)
data       = [(2014,2,15,0),(2014,3,10,0)]
cal        = ["seconds  since 2014-2-15 00:00:00 +00:00:00",'gregorian']
goa2       = ccpp.ncload(name,data,file2,cal,var,var2d) 
