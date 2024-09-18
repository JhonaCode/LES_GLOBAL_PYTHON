#from  Parameters_SAM_tupa import * 

import  numpy as np

import  cftime

import  matplotlib          as mpl

import  matplotlib.pyplot   as plt

# Python standard library datetime  module
import  datetime as dt  

#import  campain_data  as cd
import  sam_python.data_own       as down

import  sam_python.figure_own_2d  as fown

import  sam_python.default_values as df

#mUSH BE CHANGE, 
from    files_direction     import file_fig 


#def defaul_values(lim,maxv,minv,alt,maxh,var_to,name,color,explabel,leg_loc,diurnal,show): 

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


def plot2d_contour(exp,var=[],contour=[],alt=[],days=[],explabel1=[],explabel2=[],color=[],var_to=[],axis_on=[],show=[]):

    #if var:
    #    exp_var=var
    #else:
    #    exp_var=ex.var_to_plot

    exp_var=var

    k=0
    for ex in exp:

        if k==0:
            if not var:
                exp_var=ex.var2d

        print('\n')
        print('_______________________________________')
        print('       ________%s_______'%(ex.name))
        print('_______________________________________')
        print('\n')


        lim,alt,var_to,color,explabel1,explabel2,axis_on,show = df.default_values_2d(exp,exp_var,contour,alt,var_to,color,explabel1,explabel2,axis_on,show,k)


        j=0
        for vtex in exp_var:

            if days:

                idi     = dt.datetime(days[k][j][0][0], days[k][j][0][1] ,days[k][j][0][2], days[k][j][0][3],days[k][j][0][4],0) 
                idf     = dt.datetime(days[k][j][1][0], days[k][j][1][1] ,days[k][j][1][2], days[k][j][1][3],days[k][j][1][4],0)

                ni,nf= down.data_n(idi,idf,ex.date[:])

                if ni>len(ex.date):
                    ni=ni-1

            else:
                #days=ex.datei+ex.datef
                ni,nf= down.data_n(ex.datei,ex.datef,ex.date[:])


            var=getattr(ex, vtex)


            li,lf= down.level_n(alt[k][j][0],alt[k][j][1],ex.z[:]/1000.0)

            #To scale de var
            var=var[ni:nf,li:lf+1]*var_to[k][j]
            date=ex.date[ni:nf]
            z=ex.z[li:lf+1]/1000.0


            fn,ax   = fown.d2_plot_im_diff(ex,date,z,var,contour[k][j],explabel1[k][j],'lower',color[k][j],axis_on[k][j])
            
            #ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

            ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )

            #ax.ticklabel_format(axis="x", style="sci", scilimits=(0,0))

            if(axis_on[k][j][1]):
                #plt.xlabel(r'Hours LT (UTC-4)') 
                plt.xlabel(r'Horas HL (UTC-6)') 
            if(axis_on[k][j][2]):
                plt.ylabel(r'z [km]')

            plt.savefig('%s/%s_2d_%s.pdf'%(file_fig,ex.name,vtex), format='pdf',bbox_inches='tight', dpi=1000)
            
            #print(defaul )
            if show[k][j]:

                plt.show()

            plt.close('all')

            j+=1
        k+=1



    return 

def plot2d_im_diff(ex1,ex2,variables,days=[],alt=[],color=[],explabel1=[],explabel2=[],var_to=[],contour=[],axis_on=[],keyf=[],show=[]):

    print("___________________")
    print("Difference %s-%s   "%(ex2.name,ex1.name))
    print("___________________")


    #Experimento base 
    ex=ex1

    j=0


    for var in variables:


        print("____Variable_______")
        print("       %s          "%(var))
        print("___________________")

        nivel1  = 0.0
        nivel2  = alt[0]

        
        if days:

            idi     = dt.datetime(days[j][0][0], days[j][0][1] ,days[j][0][2], days[j][0][3],5,0) 

            idf     = dt.datetime(days[j][1][0], days[j][1][1] ,days[j][1][2], days[j][1][3],5,0)

            ###########
            #print(idi)
            ###########

            h1i=days[j][0][3]
            h2i=days[j][1][3]

            n1i,n1f= down.data_n(idi,idf,ex1.date[:])
            n2i,n2f= down.data_n(idi,idf,ex2.date[:])

            if n1f-n1i!=n2f-n2i:

                print("The period os the date must be the same, with the same number os points. Use interpolation function to others cases ")
                exit()

        else:
            #initial hour
            h1i=ex1.datei.hour
            #final hour
            h1f=ex1.datef.hour

            n1i,n1f= down.data_n(ex1.datei,ex1.datef,ex1.date[:])


            h2i=ex2.datei.hour
            #final hour
            h2f=ex2.datef.hour
            n2i,n2f= down.data_n(ex2.datei,ex2.datef,ex2.date[:])

            n1i=n1i-1
            n1f=n1f+1
            n2i=n2i-1
            n2f=n2f+1


        var1     = ex1.nc_f[var][n1i:n1f,:]
        var2     = ex2.nc_f[var][n2i:n2f,:]

        diff     = var2-var1

        #mean     = (var2+var1)/2.0
        #dp       = np.sqrt(0.5*((var1-mean)**2+(var2-mean)**2))
        #diff     = (var2-var1)/dp

        #default= default_values(ex,diff,contour,alt,var_to,color,explabel,axis_on,show)

        lim,alt,var_to,color,explabel1,explabel2,axis_on,show = df.default_values_diff(ex,variables,contour,alt,var_to,color,explabel1,explabel2,axis_on,show)

        li,lf= down.level_n(alt[j][0],alt[j][1],ex.z[:]/1000.0)

        #To scale the var
        #diff=diff[:,li:lf]*default[2][j]
        #date=ex.date[n2i:n2f]
        #z=ex.z[li:lf]/1000.0

        #To scale the var
        var2pl=diff[:,li:lf+1]*var_to[j]
        date=ex.date[n1i:n1f]
        z=ex.z[li:lf+1]/1000.0

        fn,ax   = fown.d2_plot_im_diff(ex,date,z,var2pl,contour[j],explabel1[j],'lower',color[j],axis_on[j])

        #ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

        ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )


        if(axis_on[j][1]):
            #plt.xlabel(r'Hours LT (UTC-6)') 
            plt.xlabel(r'Horas HL (UTC-6)') 

        if(axis_on[j][2]):
                plt.ylabel(r'z [km]')

        
        plt.savefig('%s/diff_%s_2d_%s_%s.pdf'%(file_fig,var,ex1.name+'_'+ex2.name,keyf[0]), format='pdf',bbox_inches='tight', dpi=1000)


        if show[j]:
            plt.show()

        plt.close()

        j+=1

    return

def plot2d_wind(exp,lev,contour=[],xlim=[],ylim=[],days=[],explabel=[],explabel2=[],color=[],var_to=[],axis_on=[],leg_loc=[],show=[]):

    #if var:
    #    exp_var=var
    #else:
    #    exp_var=ex.var_to_plot


    k=0
    j=0
    for ex in exp:

        print('_________________')
        print('________%s_______'%(ex.name))
        print('_________________')

        U='U%s'%(lev[k])
        V='V%s'%(lev[k])
        var1=getattr(ex, U)
        var2=getattr(ex, V)

        if days:

            idi = dt.datetime(days[k][j][0], days[k][j][1] ,days[k][j][2], days[k][j][3],days[k][j][4],0) 

            ni= down.data_ind(idi,ex.date[:])

        else:
            days=ex.datei
            ni= down.data_n(ex.datei,ex.date[:])
        
        #module of velocity 
        #MF      =   np.sqrt(var1[:]**2+var2[:]**2)
        MF      =getattr(ex, V)

        lim,xlim,ylim,var_to,color,explabel1,explabel2,axis_on,leg_loc,show = df.default_values_horizontal(ex,MF,contour,xlim,ylim,var_to,color,explabel,explabel2,axis_on,leg_loc,show)


        #To scale de var
        var1=var1[ni,:,:]*var_to[k][j]
        var2=var2[ni,:,:]*var_to[k][j]
        x  =ex.x[:]/1000.0
        y =ex.y[:]/1000.0


        fn,ax   = fown.d2_plot_wind(ex,x,y,var1,var2,contour[k][j],xlim[k][j],ylim[k][j],explabel[k][j],'lower',color[k][j],axis_on[k][j],leg_loc[k][j])

        #ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

        #ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )

        if(axis_on[k][j][1]):
            plt.xlabel(r'x [km]') 
        if(axis_on[k][j][2]):
            plt.ylabel(r'y [km]')

        plt.savefig('%s/%s_2d_horizontal_U%s.pdf'%(file_fig,ex.name,lev[k]), format='pdf',bbox_inches='tight', dpi=1000)
        
        #print(defaul )
        if show[k][j]:

            plt.show()

        k+=1

        plt.close('all')

    return 
        
def plot2d_horizontal(exp,var=[],contour=[],xlim=[],ylim=[],days=[],explabel=[],explabel2=[],color=[],var_to=[],axis_on=[],leg_loc=[],show=[]):

    #if var:
    #    exp_var=var
    #else:
    #    exp_var=ex.var_to_plot

    exp_var=var


    k=0
    for ex in exp:

        if k==0:
            if not var:
                exp_var=ex.var2d

        print('_________________')
        print('________%s_______'%(ex.name))
        print('_________________')

        j=0
        for vtex in exp_var:


            if days:

                idi = dt.datetime(days[k][j][0], days[k][j][1] ,days[k][j][2], days[k][j][3],days[k][j][4],0) 

                ni= down.data_ind(idi,ex.date[:])

            else:
                days=ex.datei
                ni= down.data_n(ex.datei,ex.date[:])


            var=getattr(ex, vtex)

            lim,xlim,ylim,var_to,color,explabel1,explabel2,axis_on,leg_loc,show = df.default_values_horizontal(ex,vtex,contour,xlim,ylim,var_to,color,explabel,explabel2,axis_on,leg_loc,show)


            #li,lf= down.level_n(alt[k][j][0],alt[k][j][1],ex.z[:]/1000.0)

            #To scale de var
            #var=var[ni:nf,li:lf]*var_to[k][j]
            var=var[ni,:,:]*var_to[k][j]
            #x  =ex.x[ni:nf]
            x  =ex.x[:]/1000.0
            #zy =ex.z[li:lf]/1000.0
            y =ex.y[:]/1000.0


            fn,ax   = fown.d2_plot_horizontal(ex,x,y,var,contour[k][j],xlim[k][j],ylim[k][j],explabel[k][j],'lower',color[k][j],axis_on[k][j],leg_loc[k][j])

            #ax.yaxis.set_major_locator(plt.MultipleLocator(0.5))

            #ax.grid(axis='y',linewidth=1.0,alpha=0.5,dashes=[1,1,0,0] )

            if(axis_on[k][j][1]):
                plt.xlabel(r'x [km]') 
            if(axis_on[k][j][2]):
                plt.ylabel(r'y [km]')

            #plt.savefig('%s/%s_2d_horizontal_%s.pdf'%(file_fig,ex.name,vtex), format='pdf',bbox_inches='tight', dpi=1000)
            
            #print(defaul )
            if show[k][j]:

                plt.show()

            j+=1

        k+=1

        plt.close('all')

    return 


def plot2d_media_ctn(exp,days,alt,explabel,hours,contour,axis_on,show):

    print('_________________')
    print('Cloud Fraction 2d')
    print('_____Mean________')

    #wherever day
    i=0

    nivel1=0.0
    nivel2=alt[i]

    var,time,data,lev= media(exp,days)


    idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
    idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])

    var[:,:]= var[:,:]*100#%

    fn,ax=fown.d2_plot_im_ctn(ex,days[i],time[i],data[i],var,lev[i][:]/1000.0,contour[i][0],contour[i][1],idi,idf,nivel1,nivel2,'lower','whbuyl',axis_on[i])

    ax.yaxis.set_major_locator(plt.MultipleLocator(1.0))
    plt.ylabel(r'z [km]') 
    #plt.xlabel(r'$\mathrm{Cloud Fraction}$') 

    plt.savefig('%scloudfraction_6cases_mean.pdf'%(file_fig), format='pdf',bbox_inches='tight', dpi=1000)

    if show:
        plt.show()

def media(exp,days):
    
    clf_d=[]

    time=[]
    lev=[]
    data_p=[]

    k=0


    for ex in exp:

	#run begin 08 and end 19
        idi     = dt.datetime(days[i][0], days[i][1] ,days[i][2], days[i][3]) 
        idf     = dt.datetime(days[i][4], days[i][5] ,days[i][6], days[i][7])


        ni,nf   = down.data_n(idi,idf,ex.data[:])

        #number of levels
        nl      =  ex.z[:].shape[0]

        time.append(ex.time[ni:nf])
        data_p.append(ex.data[ni:nf])
        lev.append(ex.z[0:nl])

        #clf_d.append(ex.cld_frac_mpl[ni:nf,0:nl])
        clf_d.append(ex.CLD[ni:nf,0:nl])

        k+=1

    mean =np.mean(clf_d,axis=0)

    return mean,time,data_p,lev  

def get_figsize(columnwidth, wf=0.5, hf=(5.**0.5-1.0)/2.0, ):

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

