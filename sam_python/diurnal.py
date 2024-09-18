#Python standard library datetime  module

import  numpy               as np

import  datetime            as dt

import  cftime              as cf

import  matplotlib.pyplot   as plt

import  matplotlib          as mpl

from    matplotlib.ticker   import MultipleLocator, FormatStrFormatter

import  sam_python.data_own            as down

import  sam_python.figure_own          as fown

import  sam_python.campain_data        as cd

from    sam_python.plotparameters      import *

from    files_direction     import file_fig 

import sam_python.forcing_file_common as ffc

import sam_python.default_values as df



def label_plots(ax,legend,explabel,explabel2,xlabel): 

###Text position x
#legend[0]=0.0
###Text position y
#legend[1]=0.0
###Z label
#legend[2]=True
###hours label
#legend[3]=True


    ax.text(legend[0][0], legend[0][1], r' %s'%(explabel), fontsize=8, color='black')

    ax.text(legend[1][0], legend[1][1], r' %s'%(explabel2), fontsize=8, color='black')

    if( legend[3]==True):
        plt.ylabel(r'z [km]') 

    if( legend[4]==True):
        plt.xlabel(r'%s'%(xlabel)) 

    if( legend[5]==True):
    	plt.legend(frameon=False,loc=legend[2])


    return ax

def diurnal_hours_sam(ex,var,explabel=[],explabel2=[],alt=[],lim=[],var_to=[],color=[],leg_loc=[],diurnal=[],show=[]): 

    print("___________________")
    print("__%s__"%(ex.name))
    print("___________________")

    print("___________________")
    print("%s"%(var))
    print("___________________")

    #Its no necessary to calculate de height
    z=ex.z

    #Getting the Defaul values
    maxv=np.max(ex.nc_f[var])
    minv=np.min(ex.nc_f[var])
    maxh=np.max(z[:]/1000.0)

    name=ex.name
    date=ex.date


    defaul=default(ex,var,lim,alt,var_to,color,explabel2,leg_loc,diurnal,show)
    ###defaul=check_list(ex,var,lim,alt,var_to,color,explabel,leg_loc,diurnal,show,0,0)
    ###defaul=[lim,alt,var_to,color,explabel2,leg_loc,diurnal,show]

    data=ex.nc_f[var][:,:]*defaul[2]
    
    #lines per hour
    ch=2
    figs,axis = main_plot_diurnal_new(ex,data,ch,date,z,defaul[1],defaul[0],defaul[3],name+'_'+var,defaul[4],defaul[5],defaul[6])

    if defaul[7]:

        plt.show()


    plt.close('all')

    return 

def diurnal_hours_exp_var_sam(exp,variables,explabel=[],explabel2=[],alt=[],lim=[],var_to=[],color=[],leg_loc=[],diurnal=[],show=[]): 


    k=0

    for ex in exp:

        print("___________________")
        print("__%s__"%(ex.name))
        print("___________________")

        j=0

        for var in variables:

            print("___________________")
            print("%s"%(var))
            print("___________________")

            #Its no necessary to calculate de height
            z=ex.z


            name=ex.name
            date=ex.date

            lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show=df.default_values(exp,variables,lim,alt,var_to,color,explabel,explabel2,leg_loc,diurnal,show,k)

            data=ex.nc_f[var][:,:]*var_to[k][j]
            #

            #(ex,vartoplot,date,z,alt,lim,color,name,explabel2,leg_loc,diurnal)
            #lines per hour
            ch=2
            figs,axis = main_plot_diurnal_new(ex,data,ch,date,z,alt[k][j],lim[k][j],color[k][j],name+'_'+var,explabel2[k][j],leg_loc[k][j],diurnal[k][j])

            if show[k][j]:

                plt.show()

            j+=1

        k+=1


        plt.close('all')

    return 

###To plot a defined hour of the experiment. 
def diurnal_exp_var_hour_sam(exp,variables,hour,fig_name,explabel=[],explabel2=[],explabel3=[],xlabel=[],alt=[],lim=[],var_to=[],color=[],leg_loc=[],diurnal=[],show=[]): 


    j=0
    for var in variables:
    
        print("___________________")
        print("%s"%(var))
        print("___________________")


        figs,axis = main_plot_hour(exp,var,hour,fig_name,j,explabel,explabel2,explabel3,xlabel,alt,lim,var_to,color,leg_loc,diurnal,show)
    
        j+=1
    

    plt.close('all')

    return 

def diurnal_hours_dict_sam(exp,explabel=[],alt=[],lim=[],var_to=[],color=[],leg_loc=[],diurnal=[],show=[]): 


    j=0
    for ex in exp:

        print("___________________")
        print("__%s__"%(ex.name))
        print("___________________")

        #Function to defined the defaul values
        k=0

        for var in ex.vars_diurnal:


            print("___________________")
            print("%s"%(ex.nc_f[var].name))
            print("___________________")


            #Its no necessary to calculate de height
            z=ex.z

            #Getting the Defaul values
            maxv=np.max(ex.nc_f[var])
            minv=np.min(ex.nc_f[var])
            maxh=np.max(z[:]/1000.0)

            name=ex.name

            defaul=df.defaul_values(lim,maxv,minv,alt,maxh,var_to,name,color,explabel,leg_loc,diurnal,show)
            ###defaul=[lim,alt,var_to,color,explabel2,leg_loc,diurnal,show]

            data=ex.nc_f[var][:,:]*defaul[2][k]

            date=ex.date

            #lines per hour
            ch=2
            figs,axis = main_plot_diurnal_new(ex,data,ch,date,z,defaul[1][k],defaul[0][k],defaul[3][k],name+'_'+var,defaul[4][k],defaul[5][k],defaul[6][k])


            #print(defaul )
            if defaul[7][k]:

                plt.show()

            k+=1

    j+=1
    plt.close('all')

    return 

def diurnal_hours_dict_ccpp(exp,explabel=[],alt=[],lim=[],var_to=[],color=[],leg_loc=[],diurnal=[],show=[]): 


    for ex in exp:

        print("___________________")
        print("__%s__"%(ex.name))
        print("___________________")

        #Function to defined the defaul values
        k=0
        for var in ex.vars_diurnal:




            print("___________________")
            print("%s"%(ex.nc_f[var].name))
            print("___________________")


            #print(pressure[0,:,0])
            #print(pressure[0,:,0])


            ni,nf= down.data_n(ex.datei_diurnal,ex.datef_diurnal,ex.date[:])
            pressure=ex.pres[ni,:,0]
            
            #Initial heigth in meters
            z_sfc=60

            #Pressure in Pa and T in K
            z=ffc.get_height_from_pres(ex.T[ni,:,0], pressure, z_sfc)

            #Getting the Defaul values
            maxv=np.max(ex.nc_f[var])
            minv=np.min(ex.nc_f[var])
            maxh=np.max(z/1000.0)

            name=ex.name

            defaul=df.defaul_values(lim,maxv,minv,alt,maxh,var_to,name,color,explabel,leg_loc,diurnal,show)


            data=ex.nc_f[var][:,:,0]*defaul[2][k]
            date=ex.date

            #lines per hour
            ch=2
            #def main_plot_diurnal_new(ex,vartoplot,date,z,alt,lim,color,name,explabel2,leg_loc,diurnal):
            figs,axis = main_plot_diurnal_new(ex,data,ch,date,z,defaul[1][k],defaul[0][k],defaul[3][k],name+'_'+var,defaul[4][k],defaul[5][k],defaul[6][k])


            #print(defaul )
            if defaul[7][k]:

                plt.show()

            k+=1


    plt.close('all')

    return 


def diurnal_hours(exp,name_ex,exp_var,days,alt=[],lim=[],var_to=[],color=[],explabel2=[],leg_loc=[],diurnal=[],show=[]): 


    for ex in exp:

        print("___________________")
        print("________%s___"%(exp))
        print("___________________")

        #Function to defined the defaul values
        k=0
        for var in exp_var:

            maxh=np.max(ex.z)/1000.0
            maxv=np.max(var)
            minv=np.min(var)

            name=var.name

            defaul=df.defaul_values(lim,maxv,minv,alt,maxh,var_to,name,color,explabel2,leg_loc,diurnal,show)



            print("___________________")
            print("%s"%(var.long_name))
            print("___________________")

            #lines per hour
            ch=2

            figs,axis = main_plot_diurnal_new(var[:]*defaul[2][k],ch,ex.data,ex.z,days[k],defaul[1][k],defaul[0][k],defaul[3][k],name_ex[0]+'_'+name,defaul[4][k],defaul[5][k],defaul[6][k])

            #print(defaul )
            if defaul[7][k]:

                plt.show()

            k+=1

    plt.close('all')

    return 


def d_time(data,days):

    #Inicial hour
    hi= days[3]    
    #Final hour
    hf= days[7] 
                         #ano	    #me  	#dia	#Hour
    #Initial day
    idi     = dt.datetime(days[0], days[1] ,days[2], days[3]) 
    idf     = dt.datetime(days[4], days[5] ,days[6], days[7])

    #print("Data", idi, ' to ', idf) 
    ni,nf = down.data_n(idi,idf,data)

    return idi, idf,ni, nf,hi,hf


def diurnal_tke_budget(exp,days,alt,hour_step,lim,color,explabel,explabel2,leg_loc,show,diurnal): 


    print("__________")
    print("   TKE    ")
    print("__________")

    
    k=0
    nfig=0

    for ex in exp:

        size_wg = 0.33
        size_hf = 1.50
        if (explabel=='small'):
            plotsize(size_wg,size_hf, 1.0,'diurnal')
        else:
            plotsize(size_wg,size_hf, 0.0,'diurnal')

        #To plot 
        fn  = plt.figure(nfig)
        ax  = plt.axes()

        
        #Data and heigh index for the vectors
        idi,idf,ni,nf,hi,hf   =   d_time(ex.data,days[k][:])

        ##interval hour
        ch=hour_step

        #Falta dividir pelo tempo, derivada temporal no budget
        #var1=ex.TKE[:]  +ex.TKES[:]

        var2=ex.SHEAR[:]#+ex.SHEARS[:]
        var3=ex.BUOYA[:]#+ex.BUOYAS[:]
        var4=ex.ADVTR[:]#+ex.ADVTRS[:]
        var5=ex.PRESSTR[:]
        var6=ex.DISSIP[:]#+ex.DISSIPS[:]

        var1=var2+var3+var4+var5+var6

        #mean diurnal function 
        meanvar1,hour = diurnal_main(ex.data,ex.z[:]/1000.0,var1,idi,idf,k,hi,hf,ch)
        meanvar2,hour = diurnal_main(ex.data,ex.z[:]/1000.0,var2,idi,idf,k,hi,hf,ch)
        meanvar3,hour = diurnal_main(ex.data,ex.z[:]/1000.0,var3,idi,idf,k,hi,hf,ch)
        meanvar4,hour = diurnal_main(ex.data,ex.z[:]/1000.0,var4,idi,idf,k,hi,hf,ch)
        meanvar5,hour = diurnal_main(ex.data,ex.z[:]/1000.0,var5,idi,idf,k,hi,hf,ch)
        meanvar6,hour = diurnal_main(ex.data,ex.z[:]/1000.0,var6,idi,idf,k,hi,hf,ch)


        fn,ax=fown.splot_own_label(nfig,var2[ni:nf,:],ex.z[:]/1000.0,'blue'   , 'S'  )
        fn,ax=fown.splot_own_label(nfig,var3[ni:nf,:],ex.z[:]/1000.0,'red'    , 'B'  )
        fn,ax=fown.splot_own_label(nfig,var4[ni:nf,:],ex.z[:]/1000.0,'magenta', 'P'  )
        fn,ax=fown.splot_own_label(nfig,var5[ni:nf,:],ex.z[:]/1000.0,'cyan'   , 'T'  )
        fn,ax=fown.splot_own_label(nfig,var6[ni:nf,:],ex.z[:]/1000.0,'green'  , 'D'  )

        if diurnal==True:

            jj=0

            for j in range(0,hf-hi+ch,ch):
    
                line,col =color_hours(hour[j])

                plt.plot(meanvar2[j,:] ,ex.z[:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.0,alpha=1.0,dashes=line)
                plt.plot(meanvar3[j,:] ,ex.z[:]/1000.0,color=col,linewidth=1.0,alpha=1.0,dashes=line)
                plt.plot(meanvar4[j,:] ,ex.z[:]/1000.0,color=col,linewidth=1.0,alpha=1.0,dashes=line)
                plt.plot(meanvar5[j,:] ,ex.z[:]/1000.0,color=col,linewidth=1.0,alpha=1.0,dashes=line)

                jj=jj+1



        plt.axis([lim[k][0],lim[k][1],0,alt[k]])

        ax=label_plots(ax,leg_loc[k],[explabel[k],explabel2[k]])

        plt.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
        plt.legend(frameon=False)
        plt.ylabel(r'z[km]') 

        plt.xlabel(r'TKE BUDGET $\mathrm{[m^{2}s^{-3}]}$') 

        plt.savefig('%sdiurnal_tke_budget_%s.pdf'%(file_fig,explabel[k]),bbox_inches='tight',dpi=1000, format='pdf')

        nfig=nfig+1

        k=k+1

    if show:
        plt.show()

    plt.close('all')

    return fig 

def main_plot_deep(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal):

    f=open('cloud_deep_%s.dat'%(explabel[0][0:3]),'w+')
    f.write('Case\t\ttop\t\tbase\t\tDeep\n')


    k=0
    for vartoplot in var:

        #Initial day
        idi     = dt.datetime(days[k][0], days[k][1] ,days[k][2], days[k][3],00) 
        idf     = dt.datetime(days[k][4], days[k][5] ,days[k][6], days[k][7],00)
        #initial hour
        hi=days[k][3]
        #final hour
        hf=days[k][7]

        ni,nf= down.data_n(idi,idf,data[k][:])


        mean=   np.mean(vartoplot[ni:nf,:], axis=0)

        band=0
        for nn in range(0,len(z[k][:])):

            if ( mean[nn]>0.0010 and band==0):
                band=1
                base=z[k][nn]/1000.0
                print(base)
            if ( mean[nn]<0.0010 and band==1):
            
                top=z[k][nn]/1000.0
                print(top)
                break
        deep=top-base

        f.write('%s\t%f\t%f\t%f\n'%(explabel[k],top,base,deep))
        print('DEEP',top-base,explabel[k])
        k=k+1

    f.close()


    return 

def main_plot_hour(exp,var,hour,fig_name,vv,explabel1,explabel2,explabel3,xlabel,alt,lim,var_to,color,leg_loc,diurnal,show):


    size_wg = 0.28
    size_wg = 0.33
    size_hf = 1.50

    plotsize(size_wg,size_hf, 0.0,'diurnal2')
    #To plot 
    fig  = plt.figure()
    ax   = plt.axes()

    k=0
    for ex in exp:

        z   =ex.z
        name=ex.name
        date=ex.date


        lim,alt,var_to,color,explabel1,explabel2,explabel3,leg_loc,diurnal,show=df.default_values_old(ex,var,lim,alt,var_to,color,explabel1,explabel2,explabel3,leg_loc,diurnal,show)


        #print(alt)

        vartoplot=ex.nc_f[var][:,:]*var_to[vv]

        #initial hour
        hi=ex.datei_diurnal.hour
        #final hour
        hf=ex.datef_diurnal.hour

        ni,nf= down.data_n(ex.datei_diurnal,ex.datef_diurnal,ex.date[:])

        ch      = 1

        idi=ex.datei_diurnal
        idf=ex.datef_diurnal

        #mean diurnal function 
        meanvar,hours = diurnal_main(date,z,vartoplot,idi,idf,hi,hf,ch)

        jj=0
        for j in range(0,hf-hi+ch,ch):

            if  hours[j]==hour:

                if color:
                    line =color[k][0]
                    col  =color[k][1]
                else:
                    line,col =color_exp(k)

                #print(col,j)
                plt.plot(meanvar[j,:] ,z[:]/1000.0,label='%s'%(explabel1[k]),color=col,linewidth=1.0,alpha=1.0,dashes=line)
        
            jj=jj+1

       #(ax,legend,explabel): 

        k+=1


    explabel2=explabel2[vv]
    explabel3=explabel3[vv]


    #def label_plots(ax,legend,explabel,xlabel): 
    ax=label_plots(ax,leg_loc[vv],explabel2,explabel3,xlabel)


    if len(alt)>len(exp):

        plt.axis([lim[vv][0],lim[vv][1],alt[vv][0],alt[vv][1]])

    else:
        l1=np.min(lim[0][:])
        l2=np.max(lim[1][:])
        l3=np.min(alt[0][:])
        l4=np.max(alt[1][:])
        plt.axis([l1,l2,l3,l4])

    plt.savefig('%s/%s_hour_%s_%s.pdf'%(file_fig,var,hour,fig_name),bbox_inches='tight',dpi=1000, format='pdf')

    if(show):
        plt.show()

    return fig,ax

def main_plot_diurnal_new(ex,vartoplot,ch,date,z,alt,lim,color,name,explabel2,leg_loc,diurnal):

    #initial hour
    hi=ex.datei_diurnal.hour
    #final hour
    hf=ex.datef_diurnal.hour
    #print(hi,hf)

    ni,nf= down.data_n(ex.datei_diurnal,ex.datef_diurnal,ex.date[:])

    ##interval hour
    ch      = ch

    idi=ex.datei_diurnal
    idf=ex.datef_diurnal

    #mean diurnal function 
    meanvar,hour = diurnal_main(date,z,vartoplot,idi,idf,hi,hf,ch)

    size_wg = 0.28
    size_wg = 0.33
    size_hf = 1.50

    plotsize(size_wg,size_hf, 0.0,'diurnal')

    #To plot 
    fig  = plt.figure()
    ax   = plt.axes()

    jj=0

    if diurnal:

        for j in range(0,hf-hi+ch,ch):
    
            line,col =color_hours(hour[j])

            #print(col,j)
            plt.plot(meanvar[j,:] ,z[:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.0,alpha=1.0,dashes=line)
    
            jj=jj+1


    if( name=='buoyancyflux'):

        ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))
        ax.xaxis.get_offset_text().set_visible(False)


    elif( name=='relh' or name=='cld' or name=='qtflux'or name=='thetalflux'):
        xFormatter = FormatStrFormatter('%.f')
        ax.xaxis.set_major_formatter(xFormatter)


    label=['mean',False]

    fn,ax=fown.splot_own(fig,ax,vartoplot[ni:nf,:],z[:]/1000.0,date,color,label)

    plt.axis([lim[0],lim[1],alt[0],alt[1]])

    #def label_plots(ax,legend,explabel,xlabel): 
    ax=label_plots(ax,leg_loc,name,explabel2)

    label="%s"%(name)

    plt.savefig('%s/diurnal_%s.pdf'%(file_fig,label),bbox_inches='tight',dpi=1000, format='pdf')

    #plt.show()

    return fig,ax

def main_plot_diurnal_2var(var1,var2,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal):

    fig =[]
    axis=[]

    nfig=0
    k   =0

    for vartoplot in var1:

        idi     = dt.datetime(days[k][0], days[k][1] ,days[k][2], days[k][3]) 
        idf     = dt.datetime(days[k][4], days[k][5] ,days[k][6], days[k][7])

        hi=days[k][3]
        hf=days[k][7]

        ni,nf= down.data_n(idi,idf,data[k][:])

        ##interval hour
        ch      = 1

        #mean diurnal function 
        meanvar1,hour = diurnal_main(data[k],z[k],var1[k],idi,idf,k,hi,hf,ch)
        meanvar2,hour = diurnal_main(data[k],z[k],var2[k],idi,idf,k,hi,hf,ch)

        size_wg=0.33
        size_hf=1.5

        plotsize(size_wg,size_hf, 0.0,'diurnal')

        fn  = plt.figure(nfig)
        ax  = plt.axes()

        jj=0

        if diurnal:
            for j in range(0,hf-hi+ch,ch):
    
                line,col =color_hours(hour[j])

                plt.plot(meanvar1[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.0,alpha=1.0,dashes=line)
    
                plt.plot(meanvar2[j,:] ,z[k][:]/1000.0,color=col,linewidth=1.0,alpha=1.0,dashes=line)

                jj=jj+1
    

        #fn,ax=fown.splot_own(nfig,var1[k][ni:nf,:],z[k][:]/1000.0,color[k])
        #fn,ax=fown.splot_own(nfig,var2[k][ni:nf,:],z[k][:]/1000.0,color[k])
        plt.axis([lim[k][0],lim[k][1],0,alt[k]])

        ax.text(lim[k][0], 0.1, r' %s'%(explabel2[k]), fontsize=8, color='black')

        label="%s_%s"%(name,explabel[k])

        if(name=='u_v'):
            ax.text(lim[k][0]+0.5, 2.5, r'u $\rightarrow$ ')
            ax.text(lim[k][1]-4, 2.5, r'$\leftarrow$ v')

        plt.savefig('%sdiurnal_%s.pdf'%(file_fig,label),bbox_inches='tight',dpi=1000, format='pdf')

        k=k+1
        nfig=nfig+1
        fig.append(fn)
        axis.append(ax)


    return fig,axis 

def main_plot_diurnal_2axis(var1,var2,data,z,days,alt,lim1,lim2,cor1,cor2,name,explabel,explabel2,leg_loc,diurnal):

    fig=[]
    axis1=[]
    axis2=[]

    nfig=0

    k=0

    for vartoplot in var1:

        #Initial day
        idi     = dt.datetime(days[k][0], days[k][1] ,days[k][2], days[k][3]) 
        idf     = dt.datetime(days[k][4], days[k][5] ,days[k][6], days[k][7])
        #initial hour
        hi=days[k][3]
        #final hour
        hf=days[k][7]

        ni,nf= down.data_n(idi,idf,data[k][:])

        ##interval hour
        ch      = 1

        #mean diurnal function 
        meanvar1,hour = diurnal_main(data[k],z[k],vartoplot,idi,idf,k,hi,hf,ch)
        meanvar2,hour = diurnal_main(data[k],z[k],var2[k],idi,idf,k,hi,hf,ch)

        size_wg = 0.28
        size_wg = 0.33
        size_hf = 1.50

        if (explabel=='small'):

            plotsize(size_wg,size_hf, 1.0,'diurnal')

        else:

            plotsize(size_wg,size_hf, 0.0,'diurnal')

        #To plot 
        fn  = plt.figure(nfig)
        ax1 = plt.axes()
        ax2 = ax1.twiny() 

        jj=0

        label=['mean',False]

        if diurnal:

            for j in range(0,hf-hi+ch,ch):
    
                line,col =color_hours(hour[j])

                ax1.plot(meanvar1[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.5,alpha=1.0,dashes=line)
    
                ax2.plot(meanvar2[j,:] ,z[k][:]/1000.0,color=col,linewidth=1.0,alpha=1.0,dashes=line)

                jj=jj+1

        fn,ax=fown.splot_own(fig,ax1,vartoplot[ni:nf,:],z[k][:]/1000.0,data[k],cor1[k],label)

        fn,ax=fown.splot_own(fig,ax2,var2[k][ni:nf,:],z[k][:]/1000.0,data[k],cor2[k],label)

        ax1.axis([lim1[k][0],lim1[k][1],0,alt[k]])
        ax2.axis([lim2[k][0],lim2[k][1],0,alt[k]])

        ax1=label_plots(ax1,leg_loc[k],[explabel[k],explabel2[k]])

        label="%s_%s"%(name,explabel[k])

        plt.savefig('%sdiurnal_%s.pdf'%(file_fig,label),bbox_inches='tight', format='pdf', dpi=1000)

        fig.append(fn)

        axis1.append(ax1)
        axis2.append(ax2)

        k=k+1

        nfig=nfig+1



    return fig,axis1,axis2 

def main_plot_diurnal_3var(var1,var2,var3,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal):

    fig=[]

    nfig=0

    k=0
    for vartoplot in var1:

        #Initial day
        idi     = dt.datetime(days[k][0], days[k][1] ,days[k][2], days[k][3]) 
        idf     = dt.datetime(days[k][4], days[k][5] ,days[k][6], days[k][7])
        #initial hour
        hi=days[k][3]
        #final hour
        hf=days[k][7]

        ni,nf= down.data_n(idi,idf,data[k][:])

        ##interval hour
        ch      = 1

        #mean diurnal function 
        meanvar1,hour = diurnal_main(data[k],z[k],vartoplot,idi,idf,k,hi,hf,ch)
        meanvar2,hour = diurnal_main(data[k],z[k],var2[k],idi,idf,k,hi,hf,ch)
        meanvar3,hour = diurnal_main(data[k],z[k],var3[k],idi,idf,k,hi,hf,ch)

        #To plot 
        fn  = plt.figure(nfig)
        ax  = plt.axes()

        jj=0

        if diurnal:
            for j in range(0,hf-hi+ch,ch):
    
                line,col =color_hours(hour[j])

                plt.plot(meanvar1[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.5,alpha=1.0,dashes=line)
    
                plt.plot(meanvar2[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.5,alpha=1.0,dashes=line)

                plt.plot(meanvar3[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.5,alpha=1.0,dashes=line)

                jj=jj+1
    

        fn,ax=fown.splot_own(nfig,vartoplot[ni:nf,:],z[k][:]/1000.0,color[k])
        fn,ax=fown.splot_own(nfig,var2[k][ni:nf,:],z[k][:]/1000.0,color[k])
        fn,ax=fown.splot_own(nfig,var3[k][ni:nf,:],z[k][:]/1000.0,color[k])
        plt.axis([lim[k][0],lim[k][1],0,alt[k]])

        ax=label_plots(ax,[lim[k][0],alt[k]],[explabel[k],explabel2[k]])
        fig.append(fn)


        label="%s_%s"%(name,explabel[k])

        plt.savefig('%sdiurnal_%s.pdf'%(file_fig,label),bbox_inches='tight', format='pdf', dpi=1000)

        k=k+1

        nfig=nfig+1


    return fig,ax 

def diurnal_main(data,z,var,idi,idf,hi,hf,ch): 

    ni,nf   = down.data_n(idi,idf,data)

    #number of levels
    nl      = z.shape[0]

    #Lengh of the time array to search
    ndtp        =   len(data) 

    #Hour array
    #+ch to reach the final hour in the loop
    hour    = np.zeros(hf-hi+ch)

    #Sum variable to the mean 
    varsum  = np.zeros([hf-hi+ch,nl])

    meanvar = np.zeros([hf-hi+ch,nl])

    #var     = np.zeros([nl])
    meanvar = np.zeros([hf-hi+ch,nl])

    #Number of  time thar variable was sum 
    cont    = np.zeros(hf-hi+ch)
    

    #nf+1 because for does arrive to n+1, but  n its necessary
    for i in range(ni,nf+1):
    
        for j in range(0,hf-hi+ch,ch):

            if int(data[i].hour)==j+hi: 

                hour[j]     =   j+hi

                varsum[j,:] =   varsum[j,:]+var[i,:]

                cont[j]     =   cont[j]+1


    for j in range(0,hf-hi+ch,ch):
        
        meanvar[j,:] = varsum[j,:]/cont[j]


    return meanvar,hour



def diurnal_function(time,variable): 


    #Number of hour
    ndh     = 24
    #Hour array
    hour    = np.zeros(ndh)
    #Sum variable to the mean 
    varsum   = np.zeros(ndh)
    #Number of  time thar variable was sum 
    cont    = np.zeros(ndh)

    
    #Lengh of the time array to search
    ndtp    = len(time) 
    
    for i in range(0,ndtp):
    
        for j in range(0,ndh):
    
            if int(time[i].hour)==j : 
    
                hour[j]=j
                varsum[j]=varsum[j]+variable[i]
                cont[j]=cont[j]+1

   
    meanvar = varsum/cont

    return meanvar,hour 

def diurnal_function_exp(time,variable): 

#print timed.datetime.hour

    #Number of hour
    ndh     = 24
#Hour array
    hour    = np.zeros(ndh)
    #Sum variable to the mean 
    varsum   = np.zeros(ndh)
    #Number of  time thar variable was sum 
    cont    = np.zeros(ndh)
    
    #Lengh of the time array to search
    ndtp    = len(time) 

    #defaul time
    timebefore=dt.datetime(2000,1,1,0,0)
    
    for i in range(0,ndtp):
    
        for j in range(0,ndh):
    
            #to fund in an hour 
            if int(time[i].hour)==j: 

                hour[j]=j

                #to found in the half of an hour on time  
                if int(time[i].minute)<30: 

                    #to no stay in the same hour 
                    if int(time[i].hour)!=timebefore.hour: 

                        varsum[j]=varsum[j]+variable[i]
                        cont[j]=cont[j]+1

                        #print time[i]
                        timebefore=time[i] 

                        continue

                
    
    meanvar = varsum/cont


    return meanvar,hour 

def color_exp(hour):
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

def color_hours(hour):
    line=[1,0]
    color='k'

    if hour==9:
          #line=[3,2,1,2]
          line=[1,0]
          color='darkcyan'

    elif  hour==10:

          line=[2,2,1,2]
          color='blue'

    elif  hour==11:
          #line=[2, 1]
          line=[1,0]
          color='cyan'

    elif  hour==12:

          line=[3, 1]
          color='green'

    elif  hour==13:

          color='r'

    elif  hour==14:

          color='tab:orange'

    elif  hour==15:

          line=[1,2,1,2]
          color='tab:brown'

    elif  hour==16:

          line=[2,1,1,3]
          color='m'

    elif  hour==17:

          line=[2,1,5,3]
          color='tab:purple'

    elif  hour==18:

          #line=[4,2,1,2]
          line=[1,0]
          color='y'

    elif  hour==19:

          line=[1,2,4,2]
          color='peru'
    
    return line,color

def get_figsize(columnwidth, wf=0.24, hf=(5.**0.5-1.0)/2.0, ):

      """Parameters:
        - wf [float]:  width fraction in columnwidth units
        - hf [float]:  height fraction in columnwidth units.
                       Set by default to golden ratio.
        - columnwidth [float]: width of the column in latex. Get this from LaTeX
                               using \showthe\columnwidth
      Returns:  [fig_width,fig_height]: that should be given to matplotlib
      """
      fig_width_pt = columnwidth*wf
      inches_per_pt = 1.0/72.27               # Convert pt to inch
      fig_width = fig_width_pt*inches_per_pt  # width in inches
      fig_height = fig_width*hf      # height in inches
      return [fig_width, fig_height]
