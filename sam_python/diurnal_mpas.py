#Python standard library datetime  module

import  numpy               as np

import  datetime            as dt

import  cftime              as cf

import  pandas              as pd

import  matplotlib.pyplot   as plt

import  sam_python.data_own            as down

import  sam_python.figure_own          as fown

import  sam_python.campain_data        as cd

import  sam_python.plotparameters      as pp

import  sam_python.forcing_file_common as ffc

import  sam_python.default_values      as df

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
def diurnal_hours_mpas(ex,dates,variables,explabel1=[],explabel2=[],alt=[],lim=[],var_to=[],color=[],leg_loc=[],diurnal=[],show=[]): 

    ###To put 00 in the hour: 08,09,
    ###nh  = [i for i in range(hi,hf,hour_step)]
    ###hours = [f'{int(h):0>2}' for h in nh]

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


            vlat        =   tomean[var].mean(dim='latitude') 
            vmean       =   vlat.mean(dim='longitude')

            tlat        =   ex.t_isobaric.mean(dim='latitude')
            tmean       =   tlat.mean(dim='longitude') 
            temperature =   tmean[0,::].values

            pressure    =   ex.level[::].values

            if(k==0):
                #Pressure in Pa and T in K
                z=ffc.get_height_from_pres(temperature, pressure, z_sfc)
                vall=vmean
            else:
                vall=xr.merge([vmean,vall])

            k+=1
    

        lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show=df.default_values_mpas(ex,vall,var,z,lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show)

        var2plot=vall[var]*var_to[j]


        fig_label=name+'_'+var

        figs,axis = main_plot_diurnal(var2plot,hours,z,alt[j],lim[j],color[j],[fig_label,explabel1[j],explabel2[j]],leg_loc[j],diurnal[j])


        if show[j]:
            plt.show()

        j+=1

    return 

def diurnal_hours_mpas_ux(ex,dates,variables,explabel1=[],explabel2=[],alt=[],lim=[],var_to=[],color=[],leg_loc=[],diurnal=[],show=[]): 

    ###To put 00 in the hour: 08,09,
    ###nh  = [i for i in range(hi,hf,hour_step)]
    ###hours = [f'{int(h):0>2}' for h in nh]

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
    

        lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show=df.default_values_mpas(ex,vall,var,z,lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show)

        var2plot=vall[var]*var_to[j]


        fig_label=name+'_'+var

        figs,axis = main_plot_diurnal(var2plot,hours,z,alt[j],lim[j],color[j],[fig_label,explabel1[j],explabel2[j]],leg_loc[j],diurnal[j])

        if show[j]:
            plt.show()

        j+=1

    return 


def main_plot_diurnal(vartoplot,hours,z,alt,lim,color,explabel,leg_loc,diurnal):


    size_wg = leg_loc[5][0]
    size_hf = leg_loc[5][1]

    pp.plotsize(size_wg,size_hf, 0.0,'diurnal')

    #To plot 
    fig     = plt.figure()
    ax      = plt.axes()

    if diurnal:
        j=0
        for h in hours:

            line,col =color_hours(j)

            plt.plot(vartoplot[j,:].values ,z[:]/1000.0,label='%s'%(h),color=col,linewidth=1.0,alpha=1.0,dashes=line)
    
            j+=1

        #ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
        #ax.xaxis.get_offset_text().set_visible(False)
        ##
        #xFormatter = FormatStrFormatter('%.f')
        #ax.xaxis.set_major_formatter(xFormatter)  

    label=['mean',False]

    fig,ax=shade_plot(fig,ax,vartoplot,z[:]/1000.0,hours,color,label)

    plt.axis([lim[0],lim[1],alt[0],alt[1]])

    ax=label_plots(ax,leg_loc,explabel[1],explabel[2])

    label="%s"%(explabel[0])

    plt.savefig('%s/diurnal_%s.pdf'%(pars.out_fig,explabel[0]),bbox_inches='tight',dpi=200, format='pdf')

    return fig,ax


def shade_plot(fig,ax,data,z,time,cor,label):

    ####################################
    est =  np.mean(data, axis=0)
    sd  =   np.std(data, axis=0)

    cis =   (est[:] - sd[:]/2.0, est[:] + sd[:]/2.0)

    #cis =   (est - sd, est + sd)
    #cis =   (est*0.90, est*1.10)

    ax.fill_betweenx(z,cis[0],cis[1],alpha=0.3,color=cor)# **kw)


    if label[1]:
        ax.plot(est[:],z,color=cor,label=label[0])
    else:
        ax.plot(est[:],z,color=cor)

    return fig,ax


def color_hours(hour):
    line=[1,0]
    color='k'

    if hour==0:
          #line=[3,2,1,2]
          line=[1,0]
          color='darkcyan'

    elif  hour==1:

          line=[2,2,1,2]
          color='blue'

    elif  hour==2:
          #line=[2, 1]
          line=[1,0]
          color='cyan'

    elif  hour==3:

          line=[3, 1]
          color='green'

    elif  hour==4:

          color='r'

    elif  hour==5:

          color='tab:orange'

    elif  hour==6:

          line=[1,2,1,2]
          color='tab:brown'

    elif  hour==7:

          line=[2,1,1,3]
          color='m'

    elif  hour==8:

          line=[2,1,5,3]
          color='tab:purple'

    elif  hour==9:

          #line=[4,2,1,2]
          line=[1,0]
          color='y'

    elif  hour==10:

          line=[1,2,4,2]
          color='peru'
    
    return line,color
