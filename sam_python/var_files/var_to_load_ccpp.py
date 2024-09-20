################################################## 
# Program to read variable of a nc file 
# using python with NetCdf
# resulting of SCAM run (docker run, tutorial).
# Create by: Jhonatan Aguirre 
# Date:10/18/2021
# working:yes
#################################################

# Python library to work with Netcdf4 
from    netCDF4         import Dataset

# To save the time coordinate in specific format 
from    netCDF4         import num2date, date2num

from cftime import num2date, num2pydate

import datetime as dt

class variables(object):

    def __init__(self):

        self.time_inst          =('time_inst')
        self.time_diag          =('time_diag')
        self.time_swrad         =('time_swrad')
        self.time_lwrad         =('time_lwrad')
        self.time_rad           =('time_rad')
        self.pres               =('pres')
        self.pres_i             =('pres_i')
        self.sigma              =('sigma')
        self.sigma_i            =('sigma_i')
        self.pres_s             =('pres_s')
        self.qv                 =('qv')
        self.T                  =('T')
        self.u                  =('u')
        self.v                  =('v')
        self.ql                 =('ql')
        self.qi                 =('qi')
        self.qc                 =('qc')
        self.qv_force_tend      =('qv_force_tend')
        self.T_force_tend       =('T_force_tend')
        self.u_force_tend       =('u_force_tend')
        self.v_force_tend       =('v_force_tend')
        self.w_ls               =('w_ls')
        self.u_g                =('u_g')
        self.v_g                =('v_g')
        self.dT_dt_rad_forc     =('dT_dt_rad_forc')
        self.h_advec_thil       =('h_advec_thil')
        self.h_advec_qt         =('h_advec_qt')
        self.v_advec_thil       =('v_advec_thil')
        self.v_advec_qt         =('v_advec_qt')
        self.T_s                =('T_s')
        self.lhf                =('lhf')
        self.shf                =('shf')
        self.tprcp_inst         =('tprcp_inst')
        self.tprcp_rate_inst    =('tprcp_rate_inst')
        self.t2m                =('t2m')
        self.q2m                =('q2m')
        self.ustar              =('ustar')
        self.tsfc               =('tsfc')
        self.tau_u              =('tau_u')
        self.tau_v              =('tau_v')
        self.upd_mf             =('upd_mf')
        self.dwn_mf             =('dwn_mf')
        self.det_mf             =('det_mf')
        self.sfc_up_lw_land     =('sfc_up_lw_land')
        self.sfc_up_lw_ice      =('sfc_up_lw_ice')
        self.sfc_up_lw_water    =('sfc_up_lw_water')
        self.sfc_up_sw_dir_nir  =('sfc_up_sw_dir_nir')
        self.sfc_up_sw_dif_nir  =('sfc_up_sw_dif_nir')
        self.sfc_up_sw_dir_vis  =('sfc_up_sw_dir_vis')
        self.sfc_up_sw_dif_vis  =('sfc_up_sw_dif_vis')
        self.sfc_dwn_sw_dir_nir =('sfc_dwn_sw_dir_nir')
        self.sfc_dwn_sw_dif_nir =('sfc_dwn_sw_dif_nir')
        self.sfc_dwn_sw_dir_vis =('sfc_dwn_sw_dir_vis')
        self.sfc_dwn_sw_dif_vis =('sfc_dwn_sw_dif_vis')
        self.mp_prcp_inst       =('mp_prcp_inst')
        self.dcnv_prcp_inst     =('dcnv_prcp_inst')
        self.scnv_prcp_inst     =('scnv_prcp_inst')
        self.rad_cloud_fraction =('rad_cloud_fraction')
        self.rad_cloud_lwp      =('rad_cloud_lwp')
        self.rad_eff_rad_ql     =('rad_eff_rad_ql')
        self.rad_cloud_iwp      =('rad_cloud_iwp')
        self.rad_eff_rad_qi     =('rad_eff_rad_qi')
        self.rad_cloud_rwp      =('rad_cloud_rwp')
        self.rad_eff_rad_qr     =('rad_eff_rad_qr')
        self.rad_cloud_swp      =('rad_cloud_swp')
        self.rad_eff_rad_qs     =('rad_eff_rad_qs')
        self.sw_rad_heating_rate=('sw_rad_heating_rate')
        self.lw_rad_heating_rate=('lw_rad_heating_rate')
        self.pwat               =('pwat')
        self.dT_dt_lwrad        =('dT_dt_lwrad')
        self.dT_dt_swrad        =('dT_dt_swrad')
        self.dT_dt_pbl          =('dT_dt_pbl')
        self.dT_dt_deepconv     =('dT_dt_deepconv')
        self.dT_dt_shalconv     =('dT_dt_shalconv')
        self.dT_dt_micro        =('dT_dt_micro')
        self.dT_dt_ogwd         =('dT_dt_ogwd')
        self.dT_dt_cgwd         =('dT_dt_cgwd')
        self.dT_dt_phys         =('dT_dt_phys')
        self.dT_dt_nonphys      =('dT_dt_nonphys')
        self.dq_dt_pbl          =('dq_dt_pbl')
        self.dq_dt_deepconv     =('dq_dt_deepconv')
        self.dq_dt_shalconv     =('dq_dt_shalconv')
        self.dq_dt_micro        =('dq_dt_micro')
        self.dq_dt_phys         =('dq_dt_phys')
        self.dq_dt_nonphys      =('dq_dt_nonphys')
        self.doz_dt_pbl         =('doz_dt_pbl')
        self.doz_dt_prodloss    =('doz_dt_prodloss')
        self.doz_dt_oz          =('doz_dt_oz')
        self.doz_dt_T           =('doz_dt_T')
        self.doz_dt_ovhd        =('doz_dt_ovhd')
        self.doz_dt_phys        =('doz_dt_phys')
        self.doz_dt_nonphys     =('doz_dt_nonphys')
        self.du_dt_pbl          =('du_dt_pbl')
        self.du_dt_ogwd         =('du_dt_ogwd')
        self.du_dt_deepconv     =('du_dt_deepconv')
        self.du_dt_cgwd         =('du_dt_cgwd')
        self.du_dt_shalconv     =('du_dt_shalconv')
        self.du_dt_phys         =('du_dt_phys')
        self.du_dt_nonphys      =('du_dt_nonphys')
        self.dv_dt_pbl          =('dv_dt_pbl')
        self.dv_dt_ogwd         =('dv_dt_ogwd')
        self.dv_dt_deepconv     =('dv_dt_deepconv')
        self.dv_dt_cgwd         =('dv_dt_cgwd')
        self.dv_dt_shalconv     =('dv_dt_shalconv')
        self.dv_dt_phys         =('dv_dt_phys')
        self.dv_dt_nonphys      =('dv_dt_nonphys')
        self.sfc_dwn_sw         =('sfc_dwn_sw')
        self.sfc_up_sw          =('sfc_up_sw')
        self.sfc_net_sw         =('sfc_net_sw')
        self.sfc_dwn_lw         =('sfc_dwn_lw')
        self.gflux              =('gflux')
        self.u10m               =('u10m')
        self.v10m               =('v10m')
        self.hpbl               =('hpbl')
        self.tprcp_accum        =('tprcp_accum')
        self.ice_accum          =('ice_accum')
        self.snow_accum         =('snow_accum')
        self.graupel_accum      =('graupel_accum')
        self.conv_prcp_accum    =('conv_prcp_accum')
        self.tprcp_rate_accum   =('tprcp_rate_accum')
        self.ice_rate_accum     =('ice_rate_accum')
        self.snow_rate_accum    =('snow_rate_accum')
        self.graupel_rate_accum =('graupel_rate_accum')
        self.conv_prcp_rate_accum    =('conv_prcp_rate_accum')
        self.max_cloud_fraction  =('max_cloud_fraction')
        self.toa_total_albedo    =('toa_total_albedo')
        self.vert_int_lwp_mp     =('vert_int_lwp_mp')
        self.vert_int_iwp_mp     =('vert_int_iwp_mp')
        self.vert_int_lwp_cf     =('vert_int_lwp_cf')
        self.vert_int_iwp_cf     =('vert_int_iwp_cf')
        self.init_year           =('init_year')
        self.init_month          =('init_month')
        self.init_day            =('init_day')
        self.init_hour           =('init_hour')
        self.init_minute         =('init_minute')

    def __iter__(self):
        for each in self.__dict__.keys():              
            yield self.__getattribute__(each)

#To assint the label of the family of 
#variables

def ncload(name,dates,file_l,calendar,vars_to_plot,vars2d_to_plot,vars_diurnal,dates_d=0):

    #load class
    label=variables()

    #put the objets in class

    label.datei=dt.datetime(dates[0][0],dates[0][1],dates[0][2],dates[0][3])
    label.datef=dt.datetime(dates[1][0],dates[1][1],dates[1][2],dates[1][3])

    if dates_d==0:
        print('Diurnal dates experiment was no defined')
    else:
        label.datei_diurnal=dt.datetime(dates_d[0][0],dates_d[0][1],dates_d[0][2],dates_d[0][3])
        label.datef_diurnal=dt.datetime(dates_d[1][0],dates_d[1][1],dates_d[1][2],dates_d[1][3])

    label.name=name
    label.var1d=vars_to_plot
    label.var2d=vars2d_to_plot
    label.vars_diurnal=vars_diurnal

    # Your filename
    nc_file    = '%s'%(file_l)


    # Dataset is the class behavior to open the file
    # and create an instance of the ncCDF4 class
    nc_v = Dataset(nc_file, 'r')

    label.nc_f       =nc_v 


    label.time_inst          = nc_v.variables['time_inst']
    label.time_diag          = nc_v.variables['time_diag']
    label.time_swrad         = nc_v.variables['time_swrad']
    label.time_lwrad         = nc_v.variables['time_lwrad']
    label.time_rad           = nc_v.variables['time_rad']
    label.pres               = nc_v.variables['pres']
    label.pres_i             = nc_v.variables['pres_i']
    label.sigma              = nc_v.variables['sigma']
    label.sigma_i            = nc_v.variables['sigma_i']
    label.pres_s             = nc_v.variables['pres_s']
    label.qv                 = nc_v.variables['qv']
    label.T                  = nc_v.variables['T']
    label.u                  = nc_v.variables['u']
    label.v                  = nc_v.variables['v']
    label.ql                 = nc_v.variables['ql']
    label.qi                 = nc_v.variables['qi']
    label.qc                 = nc_v.variables['qc']
    label.qv_force_tend      = nc_v.variables['qv_force_tend']
    label.T_force_tend       = nc_v.variables['T_force_tend']
    label.u_force_tend       = nc_v.variables['u_force_tend']
    label.v_force_tend       = nc_v.variables['v_force_tend']
    label.w_ls               = nc_v.variables['w_ls']
    label.u_g                = nc_v.variables['u_g']
    label.v_g                = nc_v.variables['v_g']
    label.dT_dt_rad_forc     = nc_v.variables['dT_dt_rad_forc']
    label.h_advec_thil       = nc_v.variables['h_advec_thil']
    label.h_advec_qt         = nc_v.variables['h_advec_qt']
    label.v_advec_thil       = nc_v.variables['v_advec_thil']
    label.v_advec_qt         = nc_v.variables['v_advec_qt']
    label.T_s                = nc_v.variables['T_s']
    label.lhf                = nc_v.variables['lhf']
    label.shf                = nc_v.variables['shf']
    label.tprcp_inst         = nc_v.variables['tprcp_inst']
    label.tprcp_rate_inst    = nc_v.variables['tprcp_rate_inst']
    label.t2m                = nc_v.variables['t2m']
    label.q2m                = nc_v.variables['q2m']
    label.ustar              = nc_v.variables['ustar']
    label.tsfc               = nc_v.variables['tsfc']
    label.tau_u              = nc_v.variables['tau_u']
    label.tau_v              = nc_v.variables['tau_v']
    label.upd_mf             = nc_v.variables['upd_mf']
    label.dwn_mf             = nc_v.variables['dwn_mf']
    label.det_mf             = nc_v.variables['det_mf']
    label.sfc_up_lw_land     = nc_v.variables['sfc_up_lw_land']
    label.sfc_up_lw_ice      = nc_v.variables['sfc_up_lw_ice']
    label.sfc_up_lw_water    = nc_v.variables['sfc_up_lw_water']
    label.sfc_up_sw_dir_nir  = nc_v.variables['sfc_up_sw_dir_nir']
    label.sfc_up_sw_dif_nir  = nc_v.variables['sfc_up_sw_dif_nir']
    label.sfc_up_sw_dir_vis  = nc_v.variables['sfc_up_sw_dir_vis']
    label.sfc_up_sw_dif_vis  = nc_v.variables['sfc_up_sw_dif_vis']
    label.sfc_dwn_sw_dir_nir = nc_v.variables['sfc_dwn_sw_dir_nir']
    label.sfc_dwn_sw_dif_nir = nc_v.variables['sfc_dwn_sw_dif_nir']
    label.sfc_dwn_sw_dir_vis = nc_v.variables['sfc_dwn_sw_dir_vis']
    label.sfc_dwn_sw_dif_vis = nc_v.variables['sfc_dwn_sw_dif_vis']
    label.mp_prcp_inst       = nc_v.variables['mp_prcp_inst']
    label.dcnv_prcp_inst     = nc_v.variables['dcnv_prcp_inst']
    label.scnv_prcp_inst     = nc_v.variables['scnv_prcp_inst']
    label.rad_cloud_fraction = nc_v.variables['rad_cloud_fraction']
    label.rad_cloud_lwp      = nc_v.variables['rad_cloud_lwp']
    label.rad_eff_rad_ql     = nc_v.variables['rad_eff_rad_ql']
    label.rad_cloud_iwp      = nc_v.variables['rad_cloud_iwp']
    label.rad_eff_rad_qi     = nc_v.variables['rad_eff_rad_qi']
    label.rad_cloud_rwp      = nc_v.variables['rad_cloud_rwp']
    label.rad_eff_rad_qr     = nc_v.variables['rad_eff_rad_qr']
    label.rad_cloud_swp      = nc_v.variables['rad_cloud_swp']
    label.rad_eff_rad_qs     = nc_v.variables['rad_eff_rad_qs']
    label.sw_rad_heating_rate= nc_v.variables['sw_rad_heating_rate']
    label.lw_rad_heating_rate= nc_v.variables['lw_rad_heating_rate']
    label.pwat               = nc_v.variables['pwat']
    label.dT_dt_lwrad        = nc_v.variables['dT_dt_lwrad']
    label.dT_dt_swrad        = nc_v.variables['dT_dt_swrad']
    label.dT_dt_pbl          = nc_v.variables['dT_dt_pbl']
    label.dT_dt_deepconv     = nc_v.variables['dT_dt_deepconv']
    label.dT_dt_shalconv     = nc_v.variables['dT_dt_shalconv']
    label.dT_dt_micro        = nc_v.variables['dT_dt_micro']
    label.dT_dt_ogwd         = nc_v.variables['dT_dt_ogwd']
    label.dT_dt_cgwd         = nc_v.variables['dT_dt_cgwd']
    label.dT_dt_phys         = nc_v.variables['dT_dt_phys']
    label.dT_dt_nonphys      = nc_v.variables['dT_dt_nonphys']
    label.dq_dt_pbl          = nc_v.variables['dq_dt_pbl']
    label.dq_dt_deepconv     = nc_v.variables['dq_dt_deepconv']
    label.dq_dt_shalconv     = nc_v.variables['dq_dt_shalconv']
    label.dq_dt_micro        = nc_v.variables['dq_dt_micro']
    label.dq_dt_phys         = nc_v.variables['dq_dt_phys']
    label.dq_dt_nonphys      = nc_v.variables['dq_dt_nonphys']
    label.doz_dt_pbl         = nc_v.variables['doz_dt_pbl']
    label.doz_dt_prodloss    = nc_v.variables['doz_dt_prodloss']
    label.doz_dt_oz          = nc_v.variables['doz_dt_oz']
    label.doz_dt_T           = nc_v.variables['doz_dt_T']
    label.doz_dt_ovhd        = nc_v.variables['doz_dt_ovhd']
    label.doz_dt_phys        = nc_v.variables['doz_dt_phys']
    label.doz_dt_nonphys     = nc_v.variables['doz_dt_nonphys']
    label.du_dt_pbl          = nc_v.variables['du_dt_pbl']
    label.du_dt_ogwd         = nc_v.variables['du_dt_ogwd']
    label.du_dt_deepconv     = nc_v.variables['du_dt_deepconv']
    label.du_dt_cgwd         = nc_v.variables['du_dt_cgwd']
    label.du_dt_shalconv     = nc_v.variables['du_dt_shalconv']
    label.du_dt_phys         = nc_v.variables['du_dt_phys']
    label.du_dt_nonphys      = nc_v.variables['du_dt_nonphys']
    label.dv_dt_pbl          = nc_v.variables['dv_dt_pbl']
    label.dv_dt_ogwd         = nc_v.variables['dv_dt_ogwd']
    label.dv_dt_deepconv     = nc_v.variables['dv_dt_deepconv']
    label.dv_dt_cgwd         = nc_v.variables['dv_dt_cgwd']
    label.dv_dt_shalconv     = nc_v.variables['dv_dt_shalconv']
    label.dv_dt_phys         = nc_v.variables['dv_dt_phys']
    label.dv_dt_nonphys      = nc_v.variables['dv_dt_nonphys']
    label.sfc_dwn_sw         = nc_v.variables['sfc_dwn_sw']
    label.sfc_up_sw          = nc_v.variables['sfc_up_sw']
    label.sfc_net_sw         = nc_v.variables['sfc_net_sw']
    label.sfc_dwn_lw         = nc_v.variables['sfc_dwn_lw']
    label.gflux              = nc_v.variables['gflux']
    label.u10m               = nc_v.variables['u10m']
    label.v10m               = nc_v.variables['v10m']
    label.hpbl               = nc_v.variables['hpbl']
    label.tprcp_accum        = nc_v.variables['tprcp_accum']
    label.ice_accum          = nc_v.variables['ice_accum']
    label.snow_accum         = nc_v.variables['snow_accum']
    label.graupel_accum      = nc_v.variables['graupel_accum']
    label.conv_prcp_accum    = nc_v.variables['conv_prcp_accum']
    label.tprcp_rate_accum   = nc_v.variables['tprcp_rate_accum']
    label.ice_rate_accum     = nc_v.variables['ice_rate_accum']
    label.snow_rate_accum    = nc_v.variables['snow_rate_accum']
    label.graupel_rate_accum = nc_v.variables['graupel_rate_accum']
    label.conv_prcp_rate_accum    =nc_v.variables['conv_prcp_rate_accum']
    label.max_cloud_fraction  = nc_v.variables['max_cloud_fraction']
    label.toa_total_albedo    = nc_v.variables['toa_total_albedo']
    label.vert_int_lwp_mp     = nc_v.variables['vert_int_lwp_mp']
    label.vert_int_iwp_mp     = nc_v.variables['vert_int_iwp_mp']
    label.vert_int_lwp_cf     = nc_v.variables['vert_int_lwp_cf']
    label.vert_int_iwp_cf     = nc_v.variables['vert_int_iwp_cf']
    label.init_year           = nc_v.variables['init_year']
    label.init_month          = nc_v.variables['init_month']
    label.init_day            = nc_v.variables['init_day']
    label.init_hour           = nc_v.variables['init_hour']
    label.init_minute         = nc_v.variables['init_minute']

    tu = calendar[0] 
    tc = calendar[1]

    label.date       = num2pydate(label.time_inst[:],units=tu,calendar=tc)


    return label 

#time_inst
#time_diag
#time_swrad
#time_lwrad
#time_rad
#pres
#pres_i
#sigma
#sigma_i
#pres_s
#qv
#T
#u
#v
#ql
#qi
#qc
#qv_force_tend
#T_force_tend
#u_force_tend
#v_force_tend
#w_ls
#u_g
#v_g
#dT_dt_rad_forc
#h_advec_thil
#h_advec_qt
#v_advec_thil
#v_advec_qt
#T_s
#lhf
#shf
#tprcp_inst
#tprcp_rate_inst
#t2m
#q2m
#ustar
#tsfc
#tau_u
#tau_v
#upd_mf
#dwn_mf
#det_mf
#sfc_up_lw_land
#sfc_up_lw_ice
#sfc_up_lw_water
#sfc_up_sw_dir_nir
#sfc_up_sw_dif_nir
#sfc_up_sw_dir_vis
#sfc_up_sw_dif_vis
#sfc_dwn_sw_dir_nir
#sfc_dwn_sw_dif_nir
#sfc_dwn_sw_dir_vis
#sfc_dwn_sw_dif_vis
#mp_prcp_inst
#dcnv_prcp_inst
#scnv_prcp_inst
#rad_cloud_fraction
#rad_cloud_lwp
#rad_eff_rad_ql
#rad_cloud_iwp
#rad_eff_rad_qi
#rad_cloud_rwp
#rad_eff_rad_qr
#rad_cloud_swp
#rad_eff_rad_qs
#sw_rad_heating_rate
#lw_rad_heating_rate
#pwat
#dT_dt_lwrad
#dT_dt_swrad
#dT_dt_pbl
#dT_dt_deepconv
#dT_dt_shalconv
#dT_dt_micro
#dT_dt_ogwd
#dT_dt_cgwd
#dT_dt_phys
#dT_dt_nonphys
#dq_dt_pbl
#dq_dt_deepconv
#dq_dt_shalconv
#dq_dt_micro
#dq_dt_phys
#dq_dt_nonphys
#doz_dt_pbl
#doz_dt_prodloss
#doz_dt_oz
#doz_dt_T
#doz_dt_ovhd
#doz_dt_phys
#doz_dt_nonphys
#du_dt_pbl
#du_dt_ogwd
#du_dt_deepconv
#du_dt_cgwd
#du_dt_shalconv
#du_dt_phys
#du_dt_nonphys
#dv_dt_pbl
#dv_dt_ogwd
#dv_dt_deepconv
#dv_dt_cgwd
#dv_dt_shalconv
#dv_dt_phys
#dv_dt_nonphys
#sfc_dwn_sw
#sfc_up_sw
#sfc_net_sw
#sfc_dwn_lw
#gflux
#u10m
#v10m
#hpbl(time_inst_dim, hor_dim_layer) ;
#tprcp_accum
#ice_accum
#snow_accum
#graupel_accum
#conv_prcp_accum
#tprcp_rate_accum
#ice_rate_accum
#snow_rate_accum
#graupel_rate_accum
#conv_prcp_rate_accum
#max_cloud_fraction
#toa_total_albedo
#vert_int_lwp_mp
#vert_int_iwp_mp
#vert_int_lwp_cf
#vert_int_iwp_cf
#init_year ;
#init_month ;
#init_day ;
#init_hour ;
#init_minute ;
