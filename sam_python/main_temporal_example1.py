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
from    Parameters_ccpp import *

################################################################ 
# to defined fig out direction, and others important parameters 
from    files_direction_example1 import *

# Load function to make the diurnal cycle and profiles figures.  
#import  sam_python.diurnal   as dc

import  sam_python.temporal_plot   as tp

import  datetime as dt 

#separate with colon

exp         =  [goa1,goa2] 

c1          =  ['green','magenta']

color       =  [
                c1,c1
               ]
lim         =  [
                (0,150),(0,350),(0,250)
               ]


X           =  'Hours LT (UTC-4)'
Y           =  'Sensible Heat FLux $\mathrm{ [W m^{-2}]}$'
Y2          =  'Latent   Heat FLux $\mathrm{ [W m^{-2}]}$'
Y3          =  'Precipitation  [mm]$'

l1          =  [ [X,Y], ['a)',dt.datetime(2014,3,5,0),120],[False,'upper left']]
l2          =  [ [X,Y2],['b)',dt.datetime(2014,3,5,0),300],[False,'upper left']]
l3          =  [ [X,Y3],['C)',dt.datetime(2014,3,5,0),300],[False,'upper left']]

plot_def    =  [ 
                l1,l2,l3
                ]


#To transform the units of the variable to plot 
var_to      =  [
                  [1,1],  [1,1] ,  [1000,1000]  
               ]

#figures name
exp_label   =  [ 
                 ['SHF_IOP1','SHF_IOP2'],['LHF_IOP1','LHF_IOP2'],
                 ['PREC_IOP1','PREC_IOP2']
               ]


show        =  [
                [False,False,False],[False,False,False]
                #True, True
               ]


#for ex in exp:
#
#    tp.temporal_plot_dict(ex,lim=lim,var_to=var_to,exp_label=exp_label,plot_def=plot_def,color=color)

tp.temporal_plot_exp(exp,var_to=var_to,lim=lim,exp_label=exp_label,plot_def=plot_def,color=color,show=True)


