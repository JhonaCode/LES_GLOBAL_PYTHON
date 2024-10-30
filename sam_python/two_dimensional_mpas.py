#Python standard library datetime  module

import  numpy               as np

import  datetime            as dt

import  cftime              as cf

import  matplotlib.pyplot   as plt

import  sam_python.data_own            as down

import  sam_python.plotparameters      as pp

import  sam_python.forcing_file_common as ffc

import  sam_python.default_values      as df

import  sam_python.figure_own_xr       as fown

import importlib

import subprocess, sys

import xarray as xr

#to cp the parametres defaul 
subprocess.run('cp Parameters_default.py /pesq/dados/bamc/jhonatan.aguirre/git_repositories/MAPS_python/sam_python/', shell = True, executable="/bin/bash")

#used the user parameter to plot(plotparameter.py) if para:
#pars=__import__('source.Parameters_default',globals())
pars=importlib.import_module('.Parameters_default','sam_python',)

def label_plots(ax,legend,explabel1,explabel2): 

#leg_loc      =  ( [ 0.5,4.2],[ 0.5,4.2],'center right',[xlabel,'True'],[ylabel,'True'],[size_wg,size_hf])

    xlabel=legend[3][0]

    ylabel=legend[4][0]

    ax.text(legend[0][0], legend[0][1], r' %s'%(explabel1), fontsize=8, color='black')

    ax.text(legend[1][0], legend[1][1], r' %s'%(explabel2), fontsize=8, color='black')

    if( legend[3][1]==True):
        plt.xlabel(r'%s'%(xlabel)) 

    if( legend[4][1]==True):
        plt.ylabel(r'%s'%(ylabel)) 

    if( legend[2][1]==True):
    	plt.legend(frameon=False,loc=legend[2][0])

    return ax

def contourn_mpas_ux(ex,dates,variables,explabel1=[],explabel2=[],alt=[],contour=[],var_to=[],color=[],leg_loc=[],show=[]): 

    #Initial heigth in meters
    z_sfc=60

    #Variables to accumulate the variables in differents hours 
    name    =   str(ex.name.values)+'_'+dates[0]

    print("__%s__"%(name))

    j=0
    for var in variables:

        print("___________________")
        print("______%s_____"%(var))
        print("___________________")

        tall=[]
        hours=[]
        k=0


        for d in dates: 
     
            print("___________________")
            print(d)
            print("___________________")

            tomean = ex.sel(Time=[d],method='nearest')
            date=tomean.Time[0]

            tall.append(date.values)
            hours.append(date.dt.hour.values)

            vmean       =   tomean[var].mean(dim='n_face') 

            tmean       =   ex.t_isobaric.mean(dim='n_face')

            temperature =   tmean[0,::].values

            pressure    =   ex.nIsoLevelsT[::].values

            if(k==0):
                #Pressure in Pa and T in K
                z=ffc.get_height_from_pres(temperature, pressure, z_sfc)
                vall=vmean
            else:
                vall=xr.merge([vmean,vall])

            k+=1

        #need in the defaul
        diurnal=[]
        lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show=df.default_values_mpas(ex,vall,var,z,contour,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show)

        var2plot=vall[var]*var_to[j]

        fig_label=name+'_'+var

        figs,axis  = fown.d2_plot_im_diff(var2plot,z,alt[j],contour[j],color[j],[fig_label,explabel1[j],explabel2[j]],leg_loc[j])
            

        if show[j]:
            plt.show()

        j+=1

    return 
