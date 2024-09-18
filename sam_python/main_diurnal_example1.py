################################################################
#Program to plot meteorological date
#of the OUT_STAT files of SAM with
#python and  Netcdf library.

###########################
#Modified:23/01/23
# To run using the same files
# python_src files

###########################
#Create by: Jhonatan Aguirre
#Date:07/04/2022
#working
#python 3.9

################################################################
# To activate this environment, use
#
# $ conda activate py37
# Went panda is use
# To deactivate an active environment, use
#
# $ conda deactivate
#
# path of the ncfile or data to plot
from    Parameters import *

################################################################ 
# to defined fig out direction, and others important parameters 
from    files_direction import *

# Load function to make the diurnal cycle and profiles figures.  
#import  sam_python.diurnal   as dc

# Load function to make the diurnal cycle and profiles figures.  
import  sam_python.diurnal   as dc

import  datetime as dt 

#separate with colon

exp         =  [
                goa1,goa1
                ]

lim         =  [
                (230,290),(0,0.001),(-0.1,0.1),
               ]

var_to      =  [
                    1, 1, 1,  
               ]

#figures name
exp_label   =  [ 
                 'T', 'ql'  , 'w_ls',
               ]

l1           =  ( 240.00,12.0,'upper right',True,True)
l2           =  ( 0,12.0,'upper right',True,True)
l3           =  ( -0.1,12.0,'upper right',True,True)

leg_loc      =  [ 
                l1,l2,l3,
                ]

alt         =  [
                15.0, 15.0, 15.0, 
               ]

color       =  [
                'black','black','black',
               ]

show       =  [
                True,True,True,
               ]

diurnal     =  [
                True,True,True,
              ]

#Minimum calll
#fig,ax      =   dc.diurnal_hours_dict(ex,name,var,ex_date)
#complete call

#for ex in exp:

    #dc.diurnal_hours_dict(ex,explabel=exp_label,alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)
dc.diurnal_hours_dict_ccpp(exp,explabel=exp_label,alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)


