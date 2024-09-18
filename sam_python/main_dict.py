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
# path of the ncfile
#
from    Parameters_dict import *

################################################################ 
# to defined fig out direction 
from    files_direction import *

# Load function to make the diurnal cycle and profiles figures.  
import  sam_python.diurnal   as dc


#Defined the name of the experiments defined in Parameters files 
#separate with colon

exp          =  [f060615,f090615,f270615] 


lim         =  [
                (0,0.1),(0,15),(0,3),
                (-0.7E-3,5.5E-3),(-1.5,2.0),(20,90),
                (0, 0.04),(-20,20),(-80,90),
               ]

var_to      =  [
                    1, 100, 1,  
                    9.81/(exp[0].THETA[10,10]*1005.0*exp[0].RHO[10,10]), 100, 1,  
                    1, 1 , 1,                    
               ]

#figures name
exp_label   =  [ 
                 'uMF', 'CF'  , 'TKE',
                 'B'  , 'Wobs', 'RH',
                 'CLW', 'Q1'  , 'Q2',
               ]

l1           =  ( 0.00,4.0,'lower right',True,True)
lrh          =  ( 70.0,4.0,'lower right',True,True)

leg_loc      =  [ 
                l1,l1,l1,
                l1,l1,lrh,
                l1,l1,l1,
                ]

alt         =  [
                5.0, 5.0, 5.0, 
                5.0, 5.0, 5.0, 
                5.0, 5.0, 5.0, 
               ]

color       =  [
                'black','black','black',
                'black','black','black',
                'black','black','black',
               ]

show       =  [
                True,True,True,
                True,True,True,
                True,True,True,
               ]

diurnal     =  [
                True,True,True,
                True,True,True,
                True,True,True,
              ]

#Minimum calll
#fig,ax      =   dc.diurnal_hours_dict(ex,name,var,ex_date)
#complete call

for ex in exp:

    dc.diurnal_hours_dict(ex,explabel=exp_label,alt=alt,leg_loc=leg_loc,lim=lim,color=color,show=show,diurnal=diurnal)
