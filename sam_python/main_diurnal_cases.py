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
#python 2.7

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
from    Parameters import *

################################################################ 
# to defined fig out direction 
from    files_direction import * 

# Load function to make the diurnal cycle and profiles figures.  
import  source.diurnal   as dc 


#Defined the name of the experiments defined in Parameters files 
#separate with colon
exp         =   [ ###exp###, ]

#figures name
explabel    =   ['###exp_label###',]

# label in the figures
explabel2   =   ['###exp_label###',]

# Data to plot 
exp_date    =   [ ###exp_data###, ]

#maximum height km
alt         =   [3.5, ]

#Color shade area  
color	    =    [  'black',  ] 

#Color shade area more than 2 variables 
cor1	    =    [  'blue' ,] 
cor2	    =    [  'red'  ,] 
cor3	    =    [  'black',] 


######################Massflux profile########################## 

explabel2    =   [' uMF']

#Limite of the x and y axis.
lim_massflux =   [(0,0.1)]

#Legent localitation 
# x,y,local,legent on, axis on
leg_loc      =   [( 0.02,3.0,'lower right',True,True)] 


dc.diurnal_hours_massflux(exp,exp_date,alt,lim_massflux,color,explabel,explabel2,leg_loc,show=True,diurnal=True)


####################Total Water####################### 


explabel2   =   [r' $\mathrm{\overline{w^\prime  q_t^\prime}}$']
lim_qtf     =   [(-0.0,550.0)]
leg_loc     =   [( 50,3.0,'upper right',True,True)] 

dc.diurnal_hours_qtflux(exp, exp_date,alt,lim_qtf,color,explabel,explabel2,leg_loc,show=True,diurnal=True)

#####################Buoyancy Flux################################# 


explabel2   =   [r'B']
lim_thetav  =   [(-0.7E-3,3.5E-3)]
leg_loc     =   [( 0.01E-3,3.0,'upper right',True,True)
                ] 
dc.diurnal_hours_bouyancyflux(exp, exp_date,alt,lim_thetav,color,explabel,explabel2,leg_loc,show=True,diurnal=True)


###########################TKE########################## 
explabel2   =   ['Small TKE' ]
lim_tke     =   [(0,1.5)]
leg_loc     =   [( 0.4,3.15,'lower right',False,False)] 
dc.diurnal_hours_tke(exp, exp_date,alt,lim_tke,color,explabel,explabel2,leg_loc,show=True,diurnal=True)

############################W######################### 
explabel2 =   [' w']
lim_w     =   [(-1.5,1.0,'')]
leg_loc    =   [(-1.5,0.1,'lower right',False,False),] 
dc.diurnal_hours_wobs(exp, exp_date,alt,lim_w,color,explabel,explabel2,leg_loc,show=True,diurnal=True)


############################RH######################### 
explabel2 =   ['RH' ]
lim_relh    =   [(49,93)]
leg_loc    =   [( 65.2,3.15,'center left',False,False)] 
dc.diurnal_hours_relh(exp, exp_date,alt,lim_relh,color,explabel,explabel2,leg_loc,show=True,diurnal=True)

##############################Thetaflux################

explabel2   =   [r'$\overline{w^{\prime}\theta_l^{\prime}}$']
lim_thetafl =   [(-100.0,130.)]
leg_loc     =   [( 0.000,3.0,'lower right',True,True)] 
dc.diurnal_hours_thetalflux(exp, exp_date,alt,lim_thetafl,color,explabel,explabel2,leg_loc,show=True,diurnal=True)

##############################Cloud Fraction################
explabel2   =   ['CF']
lim_cld     =   [(0,16.0),(0,16.0),(0,16.0),(0,16.0),(0,23.0),(0,23.0),(0,23.0)]
leg_loc     =   [( 1.0,3.0,'lower right',True,True),( 1.0,3.0,'lower right',False,False,),( 1.0,3.0,'lower right',False,False,)] 
dc.diurnal_hours_cld(exp, exp_date,alt,lim_cld,color,explabel,explabel2,leg_loc,show=True,diurnal=True)


##############################Q_1###########################
explabel2 =   ['Q1' ]

lim_q1     =   [(-25,25.0)]
leg_loc    =   [( 0.01,3.0,'lower right',True,True)] 
dc.diurnal_hours_q1(exp, exp_date,alt,lim_q1,color,explabel,explabel2,leg_loc,show=True,diurnal=True)

##############################q_n(snow)###########################

lim_qn     =   [(-0.0,0.040)]
leg_loc    =   [( 0.015,3.0,'lower right',True,True)] 
dc.diurnal_hours_qn(exp, exp_date,alt,lim_qn,color,explabel,explabel2,leg_loc,show=True,diurnal=True)

##############################q_l(liquid)###########################

lim_ql     =   [(-0.0,0.040),(-0.0,0.040),(-0.0,0.040),(-0.0,0.040)]
leg_loc    =   [( 0.015,3.0,'lower right',True,True)] 
dc.diurnal_hours_ql(exp, exp_date,alt,lim_ql,color,explabel,explabel2,leg_loc,show=True,diurnal=True)

#Two axis plot.
##############################Temperature_Massfraction###########################

lim_theta   =  [(297,316)]
lim_q       =  [(0,22)]
leg_loc    =   [( 302.2,3.0,'lower center',True,True)] 
dc.diurnal_hours_tq(exp, exp_date,alt,lim_theta,lim_q,cor1,cor2,explabel,explabel2,leg_loc,show=True,diurnal=True)


##############################U_V###########################
lim_uv      =   [(-14,5.0),(-14,5.0),(-14,5.0),(-14,5.0)]
dc.diurnal_hours_uv(exp, exp_date,alt,lim_uv,color,explabel,explabel2,show=True,diurnal=True)

exit()
