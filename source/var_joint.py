
import source.functions as fnc

import xarray as xr

def joint(de,days,name='',outf='',save=False):


    T    =fnc.shallow_xarray(de.temp  ,days)
    cf   =fnc.shallow_xarray(de.cf    ,days)
    z    =fnc.shallow_xarray(de.z     ,days)
    u    =fnc.shallow_xarray(de.u     ,days)
    v    =fnc.shallow_xarray(de.v     ,days)
    w    =fnc.shallow_xarray(de.w     ,days)
    q    =fnc.shallow_xarray(de.q     ,days)
    rh   =fnc.shallow_xarray(de.rh    ,days)
    md   =fnc.shallow_xarray(de.md    ,days)
    tprec=fnc.shallow_xarray(de.tprec ,days)
    cprec=fnc.shallow_xarray(de.cprec ,days)
    lcld =fnc.shallow_xarray(de.lcld  ,days)
    mcld =fnc.shallow_xarray(de.mcld  ,days)
    hcld =fnc.shallow_xarray(de.hcld  ,days)
    shf  =fnc.shallow_xarray(de.shf   ,days)
    lhf  =fnc.shallow_xarray(de.lhf   ,days)
    qu   =fnc.shallow_xarray(de.qu    ,days)
    qv   =fnc.shallow_xarray(de.qv    ,days)
    
    iop = xr.merge([
                        T,cf,z,u,v,w,
                        q,rh,md,tprec,cprec,
                        lcld,mcld,hcld,shf,lhf,
                        qu,qv
                        ])
#    iop = xr.concat([
#                        T,cf,u,v,w,
#                        q,rh,md,tprec,cprec,
#                        lcld,mcld,hcld,shf,lhf,
#                        qu,qv
#                        ],dim='time',coords='minimal')
#                        #],dim='time',coords='different')
#

    iop=iop.drop_duplicates(dim='time')


    if save:

        print('creating %s.nc ........... '%(name))
        iop.to_netcdf('%s/%s.nc'%(outf,name))


    return iop
