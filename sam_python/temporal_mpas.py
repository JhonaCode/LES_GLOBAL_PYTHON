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

    #if legend: 
    #    ax.text(legend[0][0], legend[0][1], r' %s'%(explabel1), fontsize=8, color='black')
    #    ax.text(legend[1][0], legend[1][1], r' %s'%(explabel2), fontsize=8, color='black')

    if( legend[3][1]==True):
        plt.xlabel(r'%s'%(xlabel)) 

    if( legend[4][1]==True):
        plt.ylabel(r'%s'%(ylabel)) 

    if( legend[2][1]==True):
    	plt.legend(frameon=False,loc=legend[2][0])

    return ax

def temporal_ex_hours_mpas(exp,exp2,exp3,di,df,variables,variables2,variables3,explabel1=[],explabel2=[],lev=[],lim=[],var21=[],var22=[],var23=[],color=[],leg_loc=[],diurnal=[],show=[]): 

    #Date to referece
    year   =2024
    month_0=1
    day_0  =1

    #date_format = '%Y%m%d%H'
    date_format = '%Y%m%d%H'
    di=dt.datetime.strptime(di, date_format)
    df=dt.datetime.strptime(df, date_format)

    j=0
    for var in variables:

        size_wg = leg_loc[j][5][0]
        size_hf = leg_loc[j][5][1]

        pp.plotsize(size_wg,size_hf, 0.0,'temporal')

        #To plot 
        fig     = plt.figure()
        ax      = plt.axes()

        print("___________________")
        print("______%s_____"%(var))
        print("___________________")


        if lim:

            lim[j][0]=dt.datetime.strptime(lim[j][0], date_format)
            lim[j][1]=dt.datetime.strptime(lim[j][1], date_format)


        i=0
        for ex in exp: 
            name    =   str(ex.name.values)
            print("__%s__"%(name))

            tall=[]
            hours=[]
            k=0
            #To reference data change if change the day
            d0=-1
            day1_0=day_0

            tomean = ex.sel(Time=slice(di,df))

            for d in tomean.Time: 


                tomean = ex.sel(Time=[d.values],method='nearest')


                if lev: 
                    tomean= tomean.sel(level=[lev],method='nearest')
                    #tomean= np.squeeze(tomean,1)

                day=d.dt.day.values

                #if day==d0+1:
                #    day1_0+=1
                #date,d0=down.data_to_reference(d,month_0,day1_0,year)
                #print(date)
                #print(d.values)
                #hours.append(date)
                #hours.append(date.values.astype('datetime64[s]'))
                hours.append(d.values)

                vlat        =   tomean[var].mean(dim='latitude') 
                vmean       =   vlat.mean(dim='longitude')

                tlat        =   ex.t_isobaric.mean(dim='latitude')
                tmean       =   tlat.mean(dim='longitude') 
                temperature =   tmean[0,::].values
                pressure    =   ex.level[::].values

                if(k==0):
                    vall=vmean
                else:
                    vall=xr.merge([vmean,vall])

                k+=1

            var1plot=vall[var]*var21[j]

            plt.plot(hours,var1plot.values ,label='%s'%(explabel1[j][i]),color=color[j][i],linewidth=1.0,alpha=1.0)#,dashes=line)

            i+=1


        for ex2 in exp2: 

            #n0,n1   =   down.data_n(di+dt.timedelta(hours=-0),df,ex2.ltime.values.astype('datetime64[s]'))
            n0,n1   =   down.data_n(di,df,ex2.ltime.values.astype('datetime64[s]'))

            var2    =   variables2[j]

            try:
                var2plot=ex2[var2][n0:n1,0].values
            except:
                var2plot=ex2[var2][n0:n1].values

            var2plot=   var2plot*var22[j]

            time2   =   ex2.ltime[n0:n1].values

            #hours   =   down.data_to_reference_vector(time2,day_0,month_0,year)
            #plt.plot(hours,var2plot ,label='%s'%(explabel1[j][i]),color=color[j][i],linewidth=1.0,alpha=1.0,marker='')#,dashes=line)

            plt.plot(time2,var2plot ,label='%s'%(explabel1[j][i]),color=color[j][i],linewidth=1.0,alpha=1.0,marker='')#,dashes=line)

            i+=1

        for ex3 in exp3: 

            n0,n1   =   down.data_n(di,df,ex3.ltime.values.astype('datetime64[s]'))

            var3     =   variables3[j]
            var3plot =   ex3[var3][n0:n1,0,0].values
            var3plot =   var3plot*var23[j]
            time3    =   ex3.ltime[n0:n1]
            hours    =   down.data_to_reference_vector(time3,day_0,month_0,year)
            plt.plot(time3,var3plot ,label='%s'%(explabel1[j][i]),color=color[j][i],linewidth=1.0,alpha=1.0,marker='')#,dashes=line)

            i+=1

            #lim,var_to,color,explabel1,explabel2,leg_loc,show=df.default_temporal_mpas(ex,vall,var,hours,lim,var_to,color,explabel1,explabel2,leg_loc,diurnal,show)

        #plt.axis([lim[j][0],lim[j][1],lim[j][2],lim[j][3]])

        ax=label_plots(ax,leg_loc[j],'','')

        label="%s"%(explabel2[j]+'_'+var)

        fig.savefig('%s/temporal_%s.pdf'%(pars.out_fig,label),bbox_inches='tight',dpi=200, format='pdf')

        if show[j]=='True':
            plt.show()

        plt.close()

        j+=1

    return 

def temporal_hours_mpas(ex,dates,variables,explabel1=[],explabel2=[],lev=[],lim=[],var_to=[],color=[],leg_loc=[],diurnal=[],show=[]): 


    name    =   str(ex.name.values)+'_'+dates[0]

    print("__%s__"%(name))

    j=0
    for var in variables:

        print("___________________")
        print("______%s_____"%(var))
        print("___________________")

        if lim:

            date_format = '%Y%m%d%H'
            lim[j][0]=dt.datetime.strptime(lim[j][0], date_format)
            lim[j][1]=dt.datetime.strptime(lim[j][1], date_format)


        tall=[]
        hours=[]
        k=0
        for d in dates: 
     
            print("___________________")
            print(d)
            print("___________________")

            tomean = ex.sel(Time=[d],method='nearest')

            if lev: 
                tomean= tomean.sel(level=[lev],method='nearest')
                #tomean= np.squeeze(tomean,1)

            date=tomean.Time[0]
            tall.append(date.values)
            #hours.append(date.dt.hour.values)
            #datetime64[D] day precistion
            #datetime64[ns] microsecond  precistion
            #hours.append(date.values.astype('datetime64[s]'))
            # convert datetime64 to datetime object
            #dt = dt64.astype(datetime)
            #Trasformn nanosecon to seconds
            hours.append(date.values.astype('datetime64[s]'))

            vlat        =   tomean[var].mean(dim='latitude') 
            vmean       =   vlat.mean(dim='longitude')

            tlat        =   ex.t_isobaric.mean(dim='latitude')
            tmean       =   tlat.mean(dim='longitude') 
            temperature =   tmean[0,::].values
            pressure    =   ex.level[::].values

            if(k==0):
                vall=vmean
            else:
                vall=xr.merge([vmean,vall])

            k+=1

        lim,var_to,color,explabel1,explabel2,leg_loc,show=df.default_temporal_mpas(ex,vall,var,hours,lim,var_to,color,explabel1,explabel2,leg_loc,diurnal,show)


        var2plot=vall[var]*var_to[j]


        fig_label=name+'_'+var

        figs,axis = main_plot_temporal(var2plot,hours,lim[j],color[j],[fig_label,explabel1[j],explabel2[j]],leg_loc[j])

        #if show[j]:
        #    plt.show()

        j+=1

    return 




def main_plot_temporal(vartoplot,hours,lim,color,explabel,leg_loc):


    size_wg = leg_loc[5][0]
    size_hf = leg_loc[5][1]

    pp.plotsize(size_wg,size_hf, 0.0,'diurnal')

    #To plot 
    fig     = plt.figure()
    ax      = plt.axes()

    plt.plot(hours,vartoplot.values ,label='%s'%(explabel[1]),color=color,linewidth=1.0,alpha=1.0)#,dashes=line)


    plt.axis([lim[0],lim[1],lim[2],lim[3]])

    ax=label_plots(ax,leg_loc,explabel[1],explabel[2])

    label="%s"%(explabel[0])

    plt.savefig('%s/temporal_%s.pdf'%(pars.out_fig,explabel[0]),bbox_inches='tight',dpi=200, format='pdf')



    return fig,ax

