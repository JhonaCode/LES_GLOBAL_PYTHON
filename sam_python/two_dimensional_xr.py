#from  Parameters_SAM_tupa import * 

import  numpy as np

import  cftime

import matplotlib.patches as mpatches

import  matplotlib          as mpl

import  matplotlib.pyplot   as plt

# Python standard library datetime  module
import  datetime as dt  

#import  campain_data  as cd
import  sam_python.data_own       as down

import  sam_python.figure_own_xr       as fown

import  sam_python.default_values as df

#To work with date in plots 
import  matplotlib.dates as mdates

import  importlib

import  subprocess, sys

import  xarray as xr

import pandas as pd

import seaborn as sns

import  sam_python.plotparameters      as pp


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


def mean_tomean_xarray(tomean, tolerance_sec=60):
    """
    Compute the mean of all variables in a list of xarray datasets,
    aligning by time-of-day within a tolerance (seconds) across multiple days.

    Parameters
    ----------
    tomean : list of xarray.Dataset
        List of experiments/datasets
    tolerance_sec : int
        Maximum difference in seconds to align times (default: 60)

    Returns
    -------
    meanxt : xarray.Dataset
        Dataset with the mean of all variables
    """
    # Step 1: convert time to seconds since midnight
    for t in tomean:
        dtimes = pd.to_datetime(t.time.values)
        seconds = dtimes.hour*3600 + dtimes.minute*60 + dtimes.second
        t.coords["sec"] = ("time", seconds)
    
    # Step 2: reference seconds from first experiment
    ref_sec = tomean[0].sec.values
    
    # Step 3: align each experiment to reference seconds within tolerance
    aligned = []
    for t in tomean:
        nearest_idx = []
        for s in ref_sec:
            diffs = np.abs(t.sec.values - s)
            idx = np.argmin(diffs)
            if diffs[idx] <= tolerance_sec:
                nearest_idx.append(idx)
            else:
                nearest_idx.append(-1)  # mark missing
        valid_idx = [i for i in nearest_idx if i >= 0]
        aligned.append(t.isel(time=valid_idx))
    
    # Step 4: compute mean for all variables
    mean_data = {}
    for var in tomean[0].data_vars.keys():

        # Check if variable is numeric
        if np.issubdtype(tomean[0][var].dtype, np.number):
            mean_data[var] = xr.concat([t[var] for t in aligned], dim="experiment").mean("experiment", skipna=True)
    
    # Step 5: build final dataset and assign time
    meanxt = xr.Dataset(mean_data)
    meanxt = meanxt.assign_coords(time=tomean[0].time.isel(time=slice(len(meanxt.time))))


    #print(tomean[0].time[0:20].values)
    #print(tomean[10].time[0:20].values)

    #exit()


    """
    ref_time = tomean[0].time

    tomean_aligned = [ex.reindex(time=ref_time, method="nearest") for ex in tomean]
    mean_all = xr.concat(tomean_aligned, dim="new")
    meanxt = mean_all.mean(dim="new")
    meanxt = meanxt.assign_coords(name="mean_all")

    When you force a common time axis (common_time) before concatenating, xarray has to shift or fill values (depending on method and join), which changes the numbers.
But when you did the NumPy approach (tomean2 with .values), you skipped the whole time alignment step — so you got the “raw” mean.
    #j.print(tomean[0].time[0:20].values)
    #print(tomean[10].time[0:20].values)
    """

    

    """
    ref_time = tomean[0].time
    this solution is no good, very slowly, because the data all in not the same time, seconds and minutes,
    then it will, extrapolate.... 
    # Step 1: add hour:minute coordinate
    for t in tomean:
        hhmm = pd.to_datetime(t.time.values).strftime("%H:%M")
        t.coords["hm"] = ("time", hhmm)
    
    # Step 2: concatenate along 'experiment'
    all_vars = xr.concat([t for t in tomean], dim="experiment")
    
    # Step 3: group by hour:minute and mean
    meanxt = all_vars.groupby("hm", squeeze=False).mean("stacked_experiment_time")
    
    # Step 4: assign a pseudo-time coordinate for plotting
    meanxt = meanxt.assign_coords(time=pd.to_datetime("2014-02-27 " + meanxt.hm.values))
    
    # Step 5: optional name
    meanxt = meanxt.assign_coords(name="mean_all")


    meanxt = mean_tomean_xarray(tomean, tolerance_sec=60)
    meanxt = meanxt.assign_coords(name="mean_all")
    
    """
    return meanxt


def mean_all_exps_sam_xr(exp,variables,date,name=[],explabel1=[],explabel2=[],key=[],alt=[],contour=[],var_to=[],color=[],leg_loc=[],show=[],temporal=None):

    print("_mean_les__%s__"%(name))

    if temporal is None: temporal = []

    k=0
    tomean=[]
    tomean2=[]
    for ex in exp:

        print("___________________")
        print("__%s__"%(ex.name))
        print("___________________")

        date_format = '%Y-%m-%dT%H'
        datei=dt.datetime.strptime(date[k][0], date_format)
        datef=dt.datetime.strptime(date[k][1], date_format)

        time1 = np.datetime64(date[k][0]) 
        time2 = np.datetime64(date[k][1])

        ni,nf=down.data_n(time1,time2,ex.time.values) 


        tovar= ex.sel(time=slice(ex.time[ni],ex.time[nf]))


        tomean.append(tovar)

        #tovar = tovar.where(tovar != 0)

        #method of positioon to compared the value
        #tomean2.append(tovar.CLD.values)

        #if name:
        name    =   str(ex.name.values)#+'_'+dates[0]

        k+=1


    #"""
    #FAZ O MESMO QUE O METODO DE APPEDN E FAZER A MEDIA MAS COM 
    #XARRAY.
    ###############1
    # Find minimum time length across all experiments
    minlen = min(ex.sizes["time"] for ex in tomean)
    
    arrays_by_pos = []

    for ex in tomean:
        # Cut each experiment to the same length
        da = ex.isel(time=slice(0, minlen))
    
        # Drop the real time coordinate, replace with positional index
        da = da.drop_vars("time")
        da = da.rename({"time": "k"})
        da = da.assign_coords(k=np.arange(minlen))
    
        arrays_by_pos.append(da)
    
    # Concatenate along a new experiment dimension
    mean_all = xr.concat(arrays_by_pos, dim="experiment")
    
    # Take mean across experiments
    meanxt = mean_all.mean("experiment", skipna=True)
    
    # Restore a time coordinate (optional, from first experiment)
    meanxt = meanxt.rename({"k": "time"})
    meanxt = meanxt.assign_coords(time=tomean[0].time.isel(time=slice(0, minlen)))
    
    # Add a label
    meanxt = meanxt.assign_coords(name="mean_all")


    #"""
    ##################3
    #tmp     =np.mean(tomean2,axis=0)
    #meanxt['CLD2']= (('time','z'),tmp) 

    #"""

    datei=dt.datetime.strptime(date[0][0], date_format)
    datef=dt.datetime.strptime(date[0][1], date_format)

    #print(datei,datef)


    #how to make the diurnal cycle
    #diurnal = mean_all.groupby("time.second").mean(dim="time")


    j=0
    for var in variables:

    
        print("___________________")
        print("%s"%(var))
        print("___________________")

        #Its no necessary to calculate de height
        z=meanxt.z.values

        hours=[datei,datef]

        contour,alt,var_to,color,exl1,exl2,leg_locu,show=df.default_values_sam_2d_kj(meanxt,var,z,contour,alt,var_to,color,explabel1,explabel2,leg_loc,show,-1,0)
        
        data=meanxt[var][:,:]*var_to[j]


        #fig_label='les_'+name+'_'+var
        fig_label='les_'+var

        figs,axis  = fown.d2_plot_im_diff(data,z,alt[j],contour[j],color[j],[fig_label,exl1,exl2[j]],leg_locu,hours=hours)


        if temporal:

            #if temporal[0][j]:

            figs,axis,axis2=fown.temporal(figs,axis,meanxt,temporal[1::])
        #print(leg_locu[5][0])
        #if(leg_locu[5][0]):

        #    figs,axis=fown.base_top_cloud(figs,axis,meanxt)

        if not key:

            figs.savefig('%s/mean_all_2d_%s.pdf'%(pars.out_fig,fig_label),bbox_inches='tight',dpi=200, format='pdf')

        else:
            figs.savefig('%s/mean_all_2d_%s_%s.pdf'%(pars.out_fig,fig_label,key),bbox_inches='tight',dpi=200, format='pdf')
            print('%s/mean_all_2d_%s_%s.pdf'%(pars.out_fig,fig_label,key))

        j+=1


    if show[0]:

        plt.show()
    
    plt.close('all')

    return 

def mean_box_sam_xr(exp,variables,date,name=[],explabel1=[],explabel2=[],key=[],alt=[],contour=[],var_to=[],color=[],leg_loc=[],show=[],temporal=[]):

    print("_mean_les__%s__"%(name))

    k=0
    mean=[]
    for ex in exp:

        print("___________________")
        print("__%s__"%(ex.name))
        print("___________________")

        date_format = '%Y-%m-%dT%H'
        datei=dt.datetime.strptime(date[k][0], date_format)
        datef=dt.datetime.strptime(date[k][1], date_format)

        time1 = np.datetime64(date[k][0]) 
        time2 = np.datetime64(date[k][1])

        ni,nf=down.data_n(time1,time2,ex.time.values) 
        tovar= ex.sel(time=slice(ex.time[ni],ex.time[nf]))

        #ni,nf=down.data_n(time1,time2,ex.time.values) 
        #tovar= ex.sel(ltime=slice(ex.ltime[ni],ex.ltime[nf]))

        mean.append(tovar)


        #if name:
        name    =   str(ex.name.values)#+'_'+dates[0]

        k+=1


    #print(tovar.time)


    mean_all=xr.concat(mean,dim='time')#,dim='new') 


    #print(mean_all.time[:])

    #make a grup with all with the same time, no date, time is hours, seconds...

    #toplot=mean_all.groupby('time.time')

    #toplot = mean_all.resample(time="10M")


    #mean_all = mean_all.assign_coords(

    #time_of_day = mean_all['time'].dt.floor("120s").time  # or "1s", "5min")
    #toplot = mean_all.groupby("time_of_day.time")

    #print(mean_all.time_of_day[:])

    #exit()

    #"""
    # seconds since midnight
    secs = (mean_all["time"].dt.hour * 3600
            + mean_all["time"].dt.minute * 60
            + mean_all["time"].dt.second)
    
    # tolerance in minutes
    tol_minutes = 2
    bin_size = tol_minutes * 60  # in seconds
    
    # create bins 0–86400
    bins = np.arange(0, 24*3600 + bin_size, bin_size)
    #this because a each 2 minutes in 24 hours, the seconds will be fall in 
    # some bin

    # assign bin index (integer) to each time

    #is the proper way to assign each timestamp to a bin index
    #np.digitize returns indices starting at 1, so we subtract 1 to make it 0-based.

    #The last value of secs might exactly equal bins[-1] (24*3600), which would give an index len(bins). To prevent an out-of-bounds error, we set those to len(bins)-2.
    bin_idx = np.digitize(secs, bins) - 1  # subtract 1 to make 0-indexed

    # assign to dataset
    mean_all = mean_all.assign_coords(time_of_day_bin=("time", bin_idx))
    
    # Optional: get bin start times as timedelta
    bin_start_times = pd.to_timedelta(bins[bin_idx], unit='s')
    mean_all = mean_all.assign_coords(time_of_day_dt=("time", bin_start_times))

    # Optional: convert to pandas Timestamp on a dummy date (say 2000-01-01)
    time_of_day_datetime = pd.Timestamp("2000-01-01") + bin_start_times
    
    # Assign back to dataset
    mean_all = mean_all.assign_coords(
        time_of_day_dt=("time", time_of_day_datetime)
    )

    # Example: compute mean ZCB per time-of-day bin
    binned = mean_all.groupby("time_of_day_bin")

    #for key, group in binned:

    #    print("First key:", key)
    #    first_group = group
    #    #this was the dimension to group, does not change, show all
    #    print(group.time_of_day_dt.values)
    #    print(group['ZCB'].values)
    #


    i=0
    for var in variables:


        k =0
        tobox=[]
        for name, group in binned:

            # Make a boxplot
            if k==5:
                print(f"Group Key: {name}")

                #extrac the variable, if not it is very slowly
                #data=binned[name][var].to_dataframe().reset_index()
                #toplot=group['ZCB'] 
                #print(group['time'],group['ZCB']) 
                #print('xxxx') 
                
                data=binned[name][var].to_dataframe().reset_index()

                data['time']=data.time

                data['timedt']=data.time.dt.time


                toplot=group[var] 

                tobox.append(data)

                k=0
            #print('yyyyy') 
            k+=1

        toboxall = pd.concat(tobox, ignore_index=True)

        contouru,altu,var_tou,coloru,explabel1u,explabel2u,leg_locu,showu=df.default_values_sam_box(toboxall,var,contour,alt,var_to,color,explabel1,explabel2,leg_loc,show,0,i)

        toboxall[var] = toboxall[var]*var_tou
        #Data to plot 
        #used user parameter to plot(plotparameter.py
        #mpl.rcParams.update(params_2d)

        size_wg = leg_locu[6][0]
        size_hf = leg_locu[6][1]
        cmas    = leg_locu[6][2]

        tama= pp.plotsize(size_wg,size_hf, cmas,pars.plotdef)


        if i==0:
        ################################3
            fig = plt.figure()
            ###New axis
            ax  = plt.axes()

        toboxall["time_str"] = toboxall["time"].dt.strftime("%H:00")

        #print(toboxall["time_str"])


        sns.boxplot(data=toboxall, x='time_str', y=var,palette=coloru, notch=False, showcaps=False, width=0.5,linewidth='1',
    flierprops={"marker": "x"},
    #boxprops={"facecolor": (.4, .6, .8, .5)},
    medianprops={"color": "coral"},)
        #sns.boxplot(data=toboxall, x='time_str', y=var,palette=coloru)
        #diverging_c = sns.diverging_palette(coloru[0], coloru[1] ,as_cmap=False) # Or as_cmap=True for a colormap
        #sns.boxplot(data=toboxall, x='time_str', y=var,palette=diverging_c)

        #ax.xaxis_date()

        #date_form = mdates.DateFormatter("%H" )
        #ax.xaxis.set_major_formatter(date_form)

        #locatormax = mdates.HourLocator(interval=2)
        #locatormin = mdates.HourLocator(interval=1)
        #ax.xaxis.set_minor_locator(locatormin)
        #ax.xaxis.set_major_locator(locatormax)

        ax.set_ylim([altu[0],altu[1]])

        ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))

        ax=fown.label_plots(toboxall['time'],ax,leg_locu,explabel1u,explabel2u,tama)

        # Define custom colors and labels for the legend
        colors = ['lightblue','lightcoral' ]
        labels = [r'Cloud Top',r'Cloud Base']
        
        # Create proxy artists for the legend
        patches = [mpatches.Patch(color=colors[i], label=labels[i]) for i in range(len(labels))]
        
        # Apply colors to the boxes (optional, but demonstrates matching legend to plot)
        for i, patch in enumerate(ax.artists):
            patch.set_facecolor(colors[i])
        
        # Add the custom legend
        ax.legend(handles=patches, frameon=False, fontsize=tama)
        

        plt.grid(True, axis="y", linestyle="--", alpha=0.6)

        fig_label='les_box_plot'+'_'+var+'_'+key

        if i==0:

            fig.savefig('%s/%s.pdf'%(pars.out_fig,fig_label),bbox_inches='tight',dpi=200, format='pdf')

        i+=1


    if show[0]:

        plt.show()
    
    plt.close('all')

    return 


def two_dimensional_exps_sam_xr(exp,variables,date,name=[],explabel1=[],explabel2=[],key=[],alt=[],contour=[],var_to=[],color=[],leg_loc=[],show=[],temporal=None):

    

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

            contour,alt,var_to,color,exl1,exl2,leg_locu,show=df.default_values_sam_2d_kj(ex,var,z,contour,alt,var_to,color,explabel1,explabel2,leg_loc,show,k,j)
            

            data=tovar[var][:,:]*var_to[j]


            fig_label='les_'+name+'_'+var


            figs,axis  = fown.d2_plot_im_diff(data,z,alt[j],contour[j],color[j],[fig_label,exl1,exl2],leg_locu,hours=hours)

            if temporal:

                    figs,axis,axis2=fown.temporal(figs,axis,tovar,temporal[1::])

            #print(leg_locu[5][0])
            if(leg_locu[5][0]):

                figs,axis=fown.base_top_cloud(figs,axis,ex)

            if not key:

                figs.savefig('%s/vertical_2d_%s.pdf'%(pars.out_fig,fig_label),bbox_inches='tight',dpi=200, format='pdf')
                print(key)
                print('%s/vertical_2d_%s.pdf'%(pars.out_fig,fig_label))

            else:
                figs.savefig('%s/vertical_2d_%s_%s.pdf'%(pars.out_fig,fig_label,key),bbox_inches='tight',dpi=200, format='pdf')
                print('else',key)
                print('%s/vertical_2d_%s_%s.pdf'%(pars.out_fig,fig_label,key))



            j+=1

        k+=1

    if show[0]:

        plt.show()
    
    plt.close('all')

    return 

def two_dimensional_diff_xr(exp,variables,date,name=[],explabel1=[],explabel2=[],alt=[],contour=[],var_to=[],color=[],leg_loc=[],show=[]):

    k=0
    for ex in exp:

        name="%s-%s"%(ex[0].name.values,ex[1].name.values)

        print("___________________")
        print("__%s-%s__"%(ex[0].name.values,ex[1].name.values))
        print("___________________")

        #date_format = '%Y%m%d%H%M%S'
        date_format = '%Y-%m-%dT%H'
        datei=dt.datetime.strptime(date[k][0], date_format)
        datef=dt.datetime.strptime(date[k][1], date_format)

        time1 = np.datetime64(date[k][0]) 
        time2 = np.datetime64(date[k][1])

        ni,nf=down.data_n(time1,time2,ex[0].time.values) 
        tovar1= ex[0].sel(time=slice(ex[0].time[ni],ex[0].time[nf]))

        ni,nf=down.data_n(time1,time2,ex[1].time.values) 
        tovar2= ex[1].sel(time=slice(ex[1].time[ni],ex[1].time[nf]))

        j=0
        for var in variables:
        
            print("___________________")
            print("%s"%(var))
            print("___________________")

            #Its no necessary to calculate de height
            z=ex[0].z.values

            hours=[datei,datef]

            contour,alt,var_to,color,exl1,exl2,leg_locu,show=df.default_values_sam_2d_kj(ex[0],var,z,contour,alt,var_to,color,explabel1,explabel2,leg_loc,show,k,j)

            data=(tovar1[var][:,:]-tovar2[var][:,:])*var_to[j]

            fig_label='diff_'+name+'_'+var

            figs,axis  = fown.d2_plot_im_diff(data,z,alt[j],contour[j],color[j],[fig_label,exl1,exl2],leg_locu,hours=hours)

            if(leg_locu[5][0]):

                figs,axis=fown.base_top_cloud(figs,axis,ex[0])

                plt.savefig('%s/vertical_2d_%s.pdf'%(pars.out_fig,fig_label),bbox_inches='tight',dpi=200, format='pdf')


            j+=1

        k+=1

    if show[0]:

        plt.show()
    
    plt.close('all')

    return 

