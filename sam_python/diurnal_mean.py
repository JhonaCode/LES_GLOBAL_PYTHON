import  numpy       as     np

#Python standard library datetime  module
import  datetime    as dt

import  data_own    as down

import  figure_own  as fown

import  campain_data as cd

import  matplotlib          as mpl

import  matplotlib.pyplot   as plt

from    files_direction import file_fig 

from plotparameters import *

#To control de zaixs label and legend on in the figure
zaxis=False
legen_on=False

def color_hours(hour):
    line=[1,0]
    color='k'
    if hour==9:
        #line=[3,2,1,2]

        color='darkcyan'

    if   hour==10:

        line=[2,2,1,2]
        color='blue'


    if    hour==11:

    	#line=[2, 1]
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
          color='y'

    elif  hour==19:

          line=[1,2,4,2]
          color='peru'
    
    return line,color

#Level max

lmax	=5.0
ano 	=2014

def label_plots(ax,lim,explabel): 

    ax.text(lim[0], lim[1]-0.3, r' %s'%(explabel[1]), fontsize=8, color='black')

    if(zaxis==True):
        plt.ylabel(r'z [km]') 
    if(legen_on==True):
        plt.legend(frameon=False)
    
    
    if(explabel[0]=='march_10' or explabel[0]=='oct_05'):
           	plt.ylabel(r'z [km]') 
    
    if( explabel[0]=='oct_01' or explabel[0]=='mean_shallow'):
    	plt.legend(frameon=False)

    return ax


def diurnal_hours_massflux(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("MASSFLUX"  )
    print("__________")

    var =[]
    data=[]
    z=[]

    name='massflux'

    for ex in exp:

        var.append(ex.MC)
        data.append(ex.data)
        z.append(ex.z)

    figs,axis = main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

    if show:
        plt.show()

    return 
    plt.close('all')

def diurnal_hours_tke(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("TKE"       )
    print("__________")

    var =[]
    data=[]
    z=[]

    name='tke'

    for ex in exp:

        var.append(ex.TKE)
        data.append(ex.data)
        z.append(ex.z)
    
    figs,axis = main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

    if show:
        plt.show()

    plt.close('all')

    return 

def diurnal_hours_cld(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("CLOUD FRACTION")
    print("__________")

    var =[]
    data=[]
    z=[]

    name='cld'

    for ex in exp:

        var.append(ex.CLD[:]*100.0)
        data.append(ex.data)
        z.append(ex.z)
    
    figs,axis = main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

    if show:
        plt.show()

    plt.close('all')

    return 

def diurnal_hours_thetae(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("Potetial Equivalent Temperature")
    print("__________")

    var =[]
    data=[]
    z=[]

    name='thetae'

    for ex in exp:

        var.append(ex.THETAE[:])
        data.append(ex.data)
        z.append(ex.z)
    
    figs,axis =main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

    if show:
        plt.show()

    plt.close('all')

    return 

def diurnal_hours_se(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("Static Energy")
    print("__________")

    var1 =[]
    var2 =[]
    var3 =[]
    data=[]
    z=[]

    name='se'

    for ex in exp:

        var1.append(ex.DSE[:])
        var2.append(ex.MSE[:])
        var3.append(ex.SSE[:])
        data.append(ex.data)
        z.append(ex.z)
    
    figs,axis= main_plot_diurnal_3var(var1,var2,var3,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

    if show:
        plt.show()

    plt.close('all')

    return 

def diurnal_hours_cld_core(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("Cloud Fraction Core")
    print("__________")

    var1 =[]
    var2 =[]
    data=[]
    z=[]

    name='cld_core'

    for ex in exp:

        var1.append(ex.CLD[:]*100)
        var2.append(ex.CORECL[:]*100) 
        data.append(ex.data)
        z.append(ex.z)
    
    figs,axis = main_plot_diurnal_2var(var1,var2,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

    for ax in axis:
	    ax.text(0.025, 0.45, r'Core' , fontsize=12, color='gray')
	    ax.text(0.045, 2.5 , r'Cloud', fontsize=12, color='navy')

    if show:
        plt.show()

    plt.close('all')
    return 

def diurnal_hours_ql(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("Liquid Water")
    print("__________")

    var =[]
    data=[]
    z=[]

    name='ql'

    for ex in exp:

        var.append(ex.QC[:])
        data.append(ex.data)
        z.append(ex.z)
    

    
    figs,axis = main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

    for ax in axis:
        ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))

    if show:
        plt.show()

    plt.close('all')

    return 


def diurnal_hours_uv(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 


    print("__________")
    print("U_V"       )
    print("__________")

    var1 =[]
    var2 =[]
    data=[]
    z=[]

    name='u_v'

    for ex in exp:

        var1.append(ex.U[:])
        var2.append(ex.V[:])
        data.append(ex.data)
        z.append(ex.z)
    
    figs,axis = main_plot_diurnal_2var(var1,var2,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

    k=0
    for ax in axis:
        ax.text(-10.5, 3.0, r'u $\rightarrow$ ')
        ax.text( 1.0, 3.0, r'$\leftarrow$ v')

        #ax.text(-10.5, 0.3, r' %s'%(explabel2[k]), fontsize=12, color='black')
        plt.savefig('%sdiurnal_uv_%s.pdf'%(file_fig,explabel[k]),bbox_inches='tight', format='pdf', dpi=1000)
        k=+1

    if show:

        plt.show()

    plt.close('all')

    return 


def diurnal_hours_tq(exp,days,alt,lim1,lim2,cor1,cor2,explabel,explabel2,show,diurnal): 


    print("__________"          )
    print("Temperature Humidity")
    print("__________"          )

    var1 =[]
    var2 =[]
    data=[]
    z=[]

    name='tq'

    for ex in exp:

        var1.append(ex.THETA[:])
        var2.append(ex.QT[:])
        data.append(ex.data)
        z.append(ex.z)
    
    figs,axis1,axis2 = main_plot_diurnal_2axis(var1,var2,data,z,days,alt,lim1,lim2,cor1,cor2,name,explabel,explabel2,diurnal)

    #k=0
    #for ax1 in axis1:

    #    ax1.set_xlabel(r'$\mathrm{\theta\quad [K]}$', color=cor1[k])
    #    axis2[k].set_xlabel(r'q [$\mathrm{gkg^{-1}}$]', color=cor2[k])

    if show:

        plt.show()

    plt.close('all')
    return 

def diurnal_hours_qlflux(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print "QLFLUX_ Liquid water flux"
    print("__________")

    var =[]
    data=[]
    z=[]

    name='qlflux'

    for ex in exp:

        var.append(ex.QCFLUX[:])
        data.append(ex.data)
        z.append(ex.z)
    
    
    figs,axis = main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

    if show:
        plt.show()

    plt.close('all')

    return 

def diurnal_hours_qtflux(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("QTFLUX_ Non precipitatin total water flux")
    print("__________")

    var =[]
    data=[]
    z=[]

    name='qtflux'

    for ex in exp:

        var.append(ex.QTFLUX[:])
        data.append(ex.data)
        z.append(ex.z)
    
    
    figs,axis = main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

    if show:
        plt.show()

    plt.close('all')

    return 


def diurnal_hours_thetalflux(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("THETALFLUX static energuy flux")
    print("__________")

    var =[]
    data=[]
    z=[]

    name='thetalflux'

    for ex in exp:

        var.append(ex.TLFLUX[:])
        data.append(ex.data)
        z.append(ex.z)
    
    
    figs,axis = main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

    if show:
        plt.show()

    plt.close('all')

    return 

def diurnal_hours_bouyancyflux(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("Bouyancy flux")
    print("__________")

    var =[]
    data=[]
    z=[]

    name='buoyancyflux'
    #print "The vertical kinematic flux of virtual potential temperature
    #ams2001glos-Bex04
    #, which when multiplied by the buoyancy parameter (g/Tv) yields a flux that is proportional to buoyancy, that is," 

    for ex in exp:

        var.append(ex.TVFLUX[:])
        data.append(ex.data)
        z.append(ex.z)
    
    
    figs,axis = main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

	#ax.text(lim[k][0]+(lim[k][1]-lim[k][0])/4.0, 3.8, r' %s'%(explabel2[k]), fontsize=12, color='black')


    if show:
        plt.show()

    plt.close('all')

    return 



def diurnal_hours_w2(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("W2_Variance of veritcal velocity ")
    print("__________")

    var =[]
    data=[]
    z=[]

    name='w2'
    #print "The vertical kinematic flux of virtual potential temperature
    #ams2001glos-Bex04
    #, which when multiplied by the buoyancy parameter (g/Tv) yields a flux that is proportional to buoyancy, that is," 

    for ex in exp:

        var.append(ex.W2[:])
        data.append(ex.data)
        z.append(ex.z)
    
    
    figs,axis = main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)

	#ax.text(lim[k][0]+(lim[k][1]-lim[k][0])/4.0, 3.8, r' %s'%(explabel2[k]), fontsize=12, color='black')


    if show:
        plt.show()

    plt.close('all')

    return 

def diurnal_hours_q1(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("Q1")
    print("__________")

    var =[]
    data=[]
    z=[]

    name='q1'

    for ex in exp:

        var.append(ex.Q1C[:])
        data.append(ex.data)
        z.append(ex.z)
    
    
    figs,axis = main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)


    if show:
        plt.show()

    plt.close('all')

    return 

def diurnal_hours_q2(exp,days,alt,lim,color,explabel,explabel2,show,diurnal): 

    print("__________")
    print("Q2")
    print("__________")

    var =[]
    data=[]
    z=[]

    name='q2'

    for ex in exp:

        var.append(ex.Q2[:])
        data.append(ex.data)
        z.append(ex.z)
    
    
    figs,axis = main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal)


    if show:
        plt.show()

    plt.close('all')

    return 


def main_plot_diurnal(var,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal):

    fig=[]
    axis=[]

    nfig=0

    k=0
    for vartoplot in var:

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
        meanvar,hour = diurnal_main(data[k],z[k],vartoplot,idi,idf,k,hi,hf,ch)

        ##plt.rcParams['figure.figsize'] = [2, 2]

        # \showthe\columnwidth overleaf!
        columnwidth = 397.485# value given by Latex
        figsize=get_figsize(columnwidth, wf=0.23, hf=1.5)
        plt.rcParams['figure.figsize'] = figsize

        #To plot 
        fn  = plt.figure(nfig)
        ax  = plt.axes()



        jj=0

        if diurnal:
            for j in range(0,hf-hi+ch,ch):
    
                line,col =color_hours(hour[j])

                plt.plot(meanvar[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.5,alpha=1.0,dashes=line)
    
                jj=jj+1
    

        fn,ax=fown.splot_own(nfig,vartoplot[ni:nf,:],z[k][:]/1000.0,color[k])
        plt.axis([lim[k][0],lim[k][1],0,alt[k]])

        ax=label_plots(ax,[lim[k][0],alt[k]],[explabel[k],explabel2[k]])

        label="%s_%s"%(name,explabel[k])

        plt.savefig('%sdiurnal_%s.pdf'%(file_fig,label),bbox_inches='tight',dpi=1000, format='pdf')

        k=k+1

        nfig=nfig+1

        fig.append(fn)

        axis.append(ax)

    #if show:

    #    plt.show()

    #plt.close('all')

    return fig,axis

def main_plot_diurnal_2var(var1,var2,data,z,days,alt,lim,color,name,explabel,explabel2,diurnal):

    fig=[]
    axis=[]

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

        #To plot 
        fn  = plt.figure(nfig)
        ax  = plt.axes()

        jj=0

        if diurnal:
            for j in range(0,hf-hi+ch,ch):
    
                line,col =color_hours(hour[j])

                plt.plot(meanvar1[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.5,alpha=1.0,dashes=line)
    
                plt.plot(meanvar2[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.5,alpha=1.0,dashes=line)

                jj=jj+1
    

        fn,ax=fown.splot_own(nfig,vartoplot[ni:nf,:],z[k][:]/1000.0,color[k])
        fn,ax=fown.splot_own(nfig,var2[k][ni:nf,:],z[k][:]/1000.0,color[k])
        plt.axis([lim[k][0],lim[k][1],0,alt[k]])

        ax=label_plots(ax,[lim[k][0],alt[k]],[explabel[k],explabel2[k]])

        label="%s_%s"%(name,explabel[k])

        plt.savefig('%sdiurnal_%s.pdf'%(file_fig,label),bbox_inches='tight', format='pdf', dpi=1000)

        k=k+1

        nfig=nfig+1

        fig.append(fn)
        axis.append(ax)


    return fig,axis 

def main_plot_diurnal_2axis(var1,var2,data,z,days,alt,lim1,lim2,cor1,cor2,name,explabel,explabel2,diurnal):

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

        #To plot 
        fn  = plt.figure(nfig)
        ax1 = plt.axes()
        ax2 = ax1.twiny() 

        jj=0

        if diurnal:

            for j in range(0,hf-hi+ch,ch):
    
                line,col =color_hours(hour[j])
                ax1.plot(meanvar1[j,:] ,z[k][:]/1000.0,label='%d'%(hour[j]),color=col,linewidth=1.5,alpha=1.0,dashes=line)
    
                ax2.plot(meanvar2[j,:] ,z[k][:]/1000.0,color=col,linewidth=1.5,alpha=1.0,dashes=line)

                jj=jj+1

        fn=fown.splot_own_ax(fn,ax1,vartoplot[ni:nf,:],z[k][:]/1000.0,cor1[k])

        fn=fown.splot_own_ax(fn,ax2,var2[k][ni:nf,:]   ,z[k][:]/1000.0,cor2[k])


        ax1.axis([lim1[k][0],lim1[k][1],0,alt[k]])
        ax2.axis([lim2[k][0],lim2[k][1],0,alt[k]])
        #ax1.text(lim1[k][0]+2, alt[k]-1.2, r'          %s'%(explabel2[k]), fontsize=12, color='black')

        ax1=label_plots(ax1,[lim1[k][0],alt[k]],[explabel[k],explabel2[k]])

        label="%s_%s"%(name,explabel[k])

        plt.savefig('%sdiurnal_%s.pdf'%(file_fig,label),bbox_inches='tight', format='pdf', dpi=1000)

        fig.append(fn)

        axis1.append(ax1)
        axis2.append(ax2)

        k=k+1



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

def diurnal_main(data,z,var,idi,idf,k,hi,hf,ch): 

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
    timebefore=dt.datetime(2000,01,01,00,00)
    
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
