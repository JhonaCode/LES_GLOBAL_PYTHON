#from  Parameters_SAM_tupa import * 

import  numpy as np

import  cftime

import  matplotlib          as mpl

import  matplotlib.pyplot   as plt

# Python standard library datetime  module
import  datetime as dt  

#import  campain_data  as cd
import  sam_python.data_own       as down

import  sam_python.figure_own_xr       as fown

import  sam_python.default_values as df

import  importlib

import  subprocess, sys

import  xarray as xr

#to cp the parametres defaul 
subprocess.run('cp Parameters_default.py /pesq/dados/bamc/jhonatan.aguirre/git_repositories/MAPS_python/sam_python/', shell = True, executable="/bin/bash")

#used the user parameter to plot(plotparameter.py) if para:
#pars=__import__('source.Parameters_default',globals())
pars=importlib.import_module('.Parameters_default','sam_python',)

def default_values(ex,var,lim,alt,var_to,color,explabel,axis_on,show): 

        maxh  = np.max(ex.z[:]/1000.0)
        minv  = np.min(var)
        maxv  = np.max(var)
        name  = ex.name

        lim.append([minv,maxv,21])      #[0]
        alt.append(maxh)                #[1]
        var_to.append(1.0)              #[2]
        color.append('RdBu_r')          #[3]
        explabel.append(name)           #[4]
        axis_on.append((True,False,False,False,0.35,0.00))##[5]
        show.append(True)               #[6]

        #defaul=[lim,alt,var_to,color,explabel2,leg_loc,diurnal,show]
        default=[lim,alt,var_to,color,explabel,axis_on,show]


        return default


def two_dimensional_sam_xr(ex,variables,date,name=[],explabel1=[],explabel2=[],alt=[],contour=[],var_to=[],color=[],leg_loc=[],show=[]):

    print("___________________")
    print("__%s__"%(ex.name))
    print("___________________")

    #date_format = '%Y%m%d%H%M%S'
    date_format = '%Y-%m-%dT%H'
    datei=dt.datetime.strptime(date[0], date_format)
    datef=dt.datetime.strptime(date[1], date_format)

    time1 = np.datetime64(date[0]) 
    time2 = np.datetime64(date[1])


    ni,nf=down.data_n(time1,time2,ex.time.values) 

    tovar= ex.sel(time=slice(ex.time[ni],ex.time[nf]))

    #if name:
    name    =   str(ex.name.values)#+'_'+dates[0]

    print("_les__%s__"%(name))

    j=0
    for var in variables:

    
        print("___________________")
        print("%s"%(var))
        print("___________________")

        #Its no necessary to calculate de height
        z=ex.z.values

        hours=[datei,datef]

        contour,alt,var_to,color,explabel1,explabel2,leg_loc,show=df.default_values_sam_2d_kj(ex,var,z,contour,alt,var_to,color,explabel1,explabel2,leg_loc,show,0,j)

        data=tovar[var][:,:]*var_to[j]


        fig_label='les_'+name+'_'+var

        figs,axis  = fown.d2_plot_im_diff(data,z,alt[j],contour[j],color[j],[fig_label,explabel1[j],explabel2[j]],leg_loc[j],hours=hours)

        if show[j]:

            plt.show()

        j+=1


        plt.close('all')

    return 


def two_dimensional_exps_sam_xr(exp,variables,date,name=[],explabel1=[],explabel2=[],alt=[],contour=[],var_to=[],color=[],leg_loc=[],show=[]):

    k=0
    for ex in exp:

        print("___________________")
        print("__%s__"%(ex.name))
        print("___________________")

        #date_format = '%Y%m%d%H%M%S'
        date_format = '%Y-%m-%dT%H'
        datei=dt.datetime.strptime(date[k][0], date_format)
        datef=dt.datetime.strptime(date[k][1], date_format)

        time1 = np.datetime64(date[k][0]) 
        time2 = np.datetime64(date[k][1])

        ni,nf=down.data_n(time1,time2,ex.time.values) 

        tovar= ex.sel(time=slice(ex.time[ni],ex.time[nf]))

        #if name:
        name    =   str(ex.name.values)#+'_'+dates[0]

        print("_les__%s__"%(name))

        j=0
        for var in variables:

        
            print("___________________")
            print("%s"%(var))
            print("___________________")

            #Its no necessary to calculate de height
            z=ex.z.values

            hours=[datei,datef]

            contour,alt,var_to,color,exl1,exl2,leg_loc,show=df.default_values_sam_2d_kj(ex,var,z,contour,alt,var_to,color,explabel1,explabel2,leg_loc,show,k,j)


            data=tovar[var][:,:]*var_to[j]


            fig_label='les_'+name+'_'+var


            figs,axis  = fown.d2_plot_im_diff(data,z,alt[j],contour[j],color[j],[fig_label,exl1,exl2],leg_loc[j],hours=hours)


            j+=1


        k+=1

    if show:

        plt.show()
    
    plt.close('all')

    return 


