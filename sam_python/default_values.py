import  numpy               as np

# Python standard library datetime  module
import  datetime as dt  
##################################

##################################
def default_values_2d(exp,varst,lim,alt,var_to,color,explabel1,explabel2,axis_on,show,k): 

    el=len(exp) 
    vl=len(varst)

    ex=exp[k]

    name=ex.name


    a1          =  [(True,True,True ,True,0.35,1.34)]

    lim1=[]
    alt1=[]
    var_to1=[]
    label1=[]
    label2=[]
    color1=[]
    ax1=[]
    show1=[]


    for i in range(0, vl):

        var=varst[i]
        #Getting the Defaul values
        maxv=np.max(ex.nc_f[var])
        minv=np.min(ex.nc_f[var])

        minh=np.min(ex.z[:]/1000.0)
        maxh=np.max(ex.z[:]/1000.0)

        lim1.append([minv,maxv])
        alt1.append([minh,maxh])         

        var_to1.append(1)

        color1.append('RdBu_r')

        label1.append(var+'_'+ex.name)
        label2.append('')

        ####bar ,x,y axis, top_lfc_pbl,size,cm a mais do grafico
        ax1.append(a1)

        show1.append('True')

    lim.append(lim1)
    var_to.append(var_to1)
    color1.append(color1)
    explabel1.append(label1)
    explabel2.append(label2)
    axis_on.append(ax1)
    show.append(show1)

    return lim,alt,var_to,color,explabel1,explabel2,axis_on,show

#######################

def default_values_diff(exp,varst,lim,alt,var_to,color,explabel1,explabel2,axis_on,show): 

    el=1#len(exp) 
    vl=len(varst)

    ex=exp

    name=ex.name


    a1          =  [(True,True,True ,True,0.35,1.34)]

    lim1=[]
    alt1=[]
    var_to1=[]
    label1=[]
    label2=[]
    color1=[]
    ax1=[]
    show1=[]


    for i in range(0, vl):

        var=varst[i]
        #Getting the Defaul values
        maxv=np.max(ex.nc_f[var])
        minv=np.min(ex.nc_f[var])

        minh=np.min(ex.z[:]/1000.0)
        maxh=np.max(ex.z[:]/1000.0)

        lim1.append([minv,maxv])
        alt1.append([minh,maxh])         

        var_to1.append(1)

        color1.append('RdBu_r')

        label1.append(var+'_'+ex.name)
        label2.append('')

        ####bar ,x,y axis, top_lfc_pbl,size,cm a mais do grafico
        ax1.append(a1)

        show1.append('True')

    lim.append(lim1)
    var_to.append(var_to1)
    color1.append(color1)
    explabel1.append(label1)
    explabel2.append(label2)
    axis_on.append(ax1)
    show.append(show1)

    return lim,alt,var_to,color,explabel1,explabel2,axis_on,show

def default_values_1d(exp,varst,lim,alt,var_to,color,explabel1,explabel2,plot_def,show,k): 

    el=len(exp) 
    vl=len(varst)

    ex=exp[k]

    name=ex.name

    X=''
    Y=''

    a1          =  ( [X,Y],[X,0,0],[False,'upper left'],[0.35,0])

    lim1=[]
    alt1=[]
    var_to1=[]
    label1=[]
    label2=[]
    color1=[]
    ax1=[]
    show1=[]


    interval_x=4


    for i in range(0, vl):

        var=varst[i]

        #Getting the Defaul values
        maxv=np.max(ex.nc_f[var])
        minv=np.min(ex.nc_f[var])
        interval_y=int(maxv/4)

        maxt=np.max(0)
        mint=np.min(len(ex.nc_f[var]))

        lim1.append([mint,maxt,interval_x])
        alt1.append([minv,maxv,interval_y])         


        var_to1.append([1])

        color1.append('blue')

        label1.append(var+'_'+ex.name)
        label2.append([''])

        ####bar ,x,y axis, top_lfc_pbl,size,cm a mais do grafico
        ax1.append([a1])

        show1.append('True')

    lim.append(lim1)
    alt.append(alt1)
    var_to.append(var_to1)
    color1.append(color1)
    explabel1.append(label1)
    explabel2.append(label2)
    plot_def.append(ax1)
    show.append(show1)

    return lim,alt,var_to,color,explabel1,explabel2,plot_def,show
        #return lim1,alt1,var_to1,color,label1,label2,ax1,show1

def default_temporal_mpas(ex,var,vname,hours,lim,var_to,color,explabel1,explabel2,leg_loc,diurnal,show): 

    name=ex.name.values

    maxv=np.min(var[vname].values)#.max
    minv=np.max(var[vname].values)#.min

    maxh=hours[0]
    minh=hours[len(hours)-1]

    lim.append([minh,maxh,minv,maxv])

    var_to.append(1)

    color.append('Red')

    explabel1.append('')
    explabel2.append('')
    #legent loc
    l1         = (['upper right',False],['%s'%vname,True],['hours',True],[1,1])

    leg_loc.append(l1)

    show.append('True')


    return lim,var_to,color,explabel1,explabel2,leg_loc,show

##################################
def default_values_sam_diurnal(ex,vname,z,lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show): 

    name    =   str(ex.name.values)#+'_'+dates[0]

    maxv=np.min(ex[vname].values)#.max
    minv=np.max(ex[vname].values)#.min


    minh=np.min(z[:]/1000.0)
    maxh=np.max(z[:]/1000.0)


    lim.append([minv,maxv])
    alt.append([minh,maxh])         

    var_to.append(1)


    color.append('Red')

    explabel1.append('')
    explabel2.append('')

    ll1=[(maxv-minv)/4.0+minv,maxh*0.90]
    #legent loc
    l1         = (ll1,ll1,['upper right',False],['%s'%vname,True],['z',True],[1,1])

    leg_loc.append(l1)

    diurnal.append('True')

    show.append('True')

    return lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show

##################################
def default_values_mpas(ex,var,vname,z,lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show): 

    name=ex.name.values

    maxv=np.min(var[vname].values)#.max
    minv=np.max(var[vname].values)#.min

    minh=np.min(z[:]/1000.0)
    maxh=np.max(z[:]/1000.0)

    lim.append([minv,maxv])
    alt.append([minh,maxh])         

    var_to.append(1)

    color.append('Red')

    explabel1.append('')
    explabel2.append('')

    ll1=[(maxv-minv)/4.0+minv,maxh*0.90]
    #legent loc
    l1         = (ll1,ll1,['upper right',False],['%s'%vname,True],['z',True],[1,1])

    leg_loc.append(l1)

    diurnal.append('True')

    show.append('True')


    return lim,alt,var_to,color,explabel1,explabel2,leg_loc,diurnal,show

def default_values_horizontal(ex,var,lim,xlim,ylim,var_to,color,explabel1,explabel2,axis_on,leg_loc,show): 

    #Getting the Defaul values
    maxv=np.max(var)
    minv=np.min(var)

    minx=np.min(ex.x[:])/1000.0
    maxx=np.max(ex.x[:])/1000.0
                               
    miny=np.min(ex.y[:])/1000.0
    maxy=np.max(ex.y[:])/1000.0

    name=ex.name


    try:
        units=var.units
    except AttributeError:
        units ='' 

    lim.append([[minv,maxv,20,'%s'%units]])
    xlim.append([[minx,maxx,10]])         
    ylim.append([[miny,maxy,10]])         

    var_to.append([1])

    color.append('RdBu_r')

    explabel1.append([name])
    explabel2.append([''])

    ####bar ,x,y axis, top_lfc_pbl,size,cm a mais do grafico
    a1          =  [(True,True,True,0.35,1.34)]
    axis_on.append([a1])

    dx=(ex.x[1]-ex.x[0])/1000.0
    dy=(ex.y[1]-ex.y[0])/1000.0

    l1  =[True,minx+100*dx,maxy-100*dy]
    leg_loc.append([l1])


    show.append(['True'])

    return lim,xlim,ylim,var_to,color,explabel1,explabel2,axis_on,leg_loc,show
