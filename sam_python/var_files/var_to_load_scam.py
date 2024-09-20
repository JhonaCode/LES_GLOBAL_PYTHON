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

class variables(object):

    def __init__(self):

        self.lat                =('lat')
        self.lon                =('lon')
        self.ntrk               =('ntrk')
        self.ntrn               =('ntrn')
        self.ntrm               =('ntrm')
        self.gw                 =('gw')
        self.lev                =('lev')
        self.hyam               =('hyam')
        self.hybm               =('hybm')
        self.P0                 =('P0')
        self.ilev               =('ilev')
        self.hyai               =('hyai')
        self.hybi               =('hybi')
        self.time               =('time')
        self.date               =('date')
        self.datesec            =('datesec')
        self.time_bnds          =('time_bnds')
        self.date_written       =('date_written')
        self.time_written       =('time_written')
        self.ndbase             =('ndbase')
        self.nsbase             =('nsbase')
        self.nbdate             =('nbdate')
        self.nbsec              =('nbsec ')
        self.mdt                =('mdt')
        self.ndcur              =('ndcur')
        self.nscur              =('nscur')
        self.co2vmr             =('co2vmr')
        self.ch4vmr             =('ch4vmr')
        self.n2ovmr             =('n2ovmr')
        self.f11vmr             =('f11vmr')
        self.f12vmr             =('f12vmr')
        self.sol_tsi            =('sol_tsi')
        self.nsteph             =('nsteph')
        self.ADRAIN             =('ADRAIN')
        self.ADSNOW             =('ADSNOW')
        self.AEROD_v            =('AEROD_v')
        self.ANRAIN             =('ANRAIN')
        self.ANSNOW             =('ANSNOW')
        self.AODDUST            =('AODDUST')
        self.AODDUST1           =('AODDUST1')
        self.AODDUST3           =('AODDUST3')
        self.AODVIS             =('AODVIS')
        self.AQRAIN             =('AQRAIN')
        self.AQSNOW             =('AQSNOW')
        self.AREI               =('AREI')
        self.AREL               =('AREL')
        self.AWNC               =('AWNC')
        self.AWNI               =('AWNI')
        self.CCN3               =('CCN3')
        self.CDNUMC             =('CDNUMC')
        self.CLDHGH             =('CLDHGH')
        self.CLDICE             =('CLDICE')
        self.CLDLIQ             =('CLDLIQ')
        self.CLDLOW             =('CLDLOW')
        self.CLDMED             =('CLDMED')
        self.CLDTOT             =('CLDTOT')
        self.CLOUD              =('CLOUD')
        self.CLOUDCOVER_CLUBB   =('CLOUDCOVER_CLUBB')
        self.CLOUDFRAC_CLUBB    =('CLOUDFRAC_CLUBB')
        self.CONCLD             =('CONCLD')
        self.DCQ                =('DCQ')
        self.DF_H2O2            =('DF_H2O2')
        self.DF_H2SO4           =('DF_H2SO4')
        self.DF_SO2             =('DF_SO2')
        self.DMS                =('DMS')
        self.DMS_SRF            =('DMS_SRF')
        self.DTCOND             =('DTCOND')
        self.DTH                =('DTH')
        self.DTV                =('DTV')
        self.DTWR_H2O2          =('DTWR_H2O2')
        self.DTWR_H2SO4         =('DTWR_H2SO4')
        self.DTWR_SO2           =('DTWR_SO2')
        self.FICE               =('FICE')
        self.FLDS               =('FLDS')
        self.FLNS               =('FLNS')
        self.FLNSC              =('FLNSC')
        self.FLNT               =('FLNT')
        self.FLNTC              =('FLNTC')
        self.FLUT               =('FLUT')
        self.FLUTC              =('FLUTC')
        self.FREQCLR            =('FREQCLR')
        self.FREQI              =('FREQI')
        self.FREQL              =('FREQL')
        self.FREQR              =('FREQR')
        self.FREQS              =('FREQS')
        self.FREQSL             =('FREQSL')
        self.FSDS               =('FSDS')
        self.FSDSC              =('FSDSC')
        self.FSNS               =('FSNS')
        self.FSNSC              =('FSNSC')
        self.FSNT               =('FSNT')
        self.FSNTC              =('FSNTC')
        self.FSNTOA             =('FSNTOA')
        self.FSNTOAC            =('FSNTOAC')
        self.FSUTOA             =('FSUTOA')
        self.H2O                =('H2O')
        self.H2O2               =('H2O2')
        self.H2O2_SRF           =('H2O2_SRF')
        self.H2O_CMXF           =('H2O_CMXF')
        self.H2O_SRF            =('H2O_SRF')
        self.H2SO4              =('H2SO4')
        self.H2SO4_SRF          =('H2SO4_SRF')
        self.ICEFRAC            =('ICEFRAC')
        self.ICIMR              =('ICIMR')
        self.ICWMR              =('ICWMR')
        self.IWC                =('IWC')
        self.LANDFRAC           =('LANDFRAC')
        self.LHFLX              =('LHFLX')
        self.LS_FLXPRC          =('LS_FLXPRC')
        self.LWCF               =('LWCF')
        self.NUMICE             =('NUMICE')
        self.NUMLIQ             =('NUMLIQ')
        self.NUMRAI             =('NUMRAI')
        self.NUMSNO             =('NUMSNO')
        self.OCNFRAC            =('OCNFRAC')
        self.OMEGA              =('OMEGA')
        self.OMEGAT             =('OMEGAT')
        self.PBLH               =('PBLH')
        self.PHIS               =('PHIS')
        self.PRECC              =('PRECC')
        self.PRECL              =('PRECL')
        self.PRECSC             =('PRECSC')
        self.PRECSL             =('PRECSL')
        self.PS                 =('PS')
        self.PSL                =('PSL')
        self.Q                  =('Q')
        self.QDIFF              =('QDIFF')
        self.QFLX               =('QFLX')
        self.QREFHT             =('QREFHT')
        self.QRL                =('QRL')
        self.QRS                =('QRS')
        self.QT                 =('QT')
        self.RAINQM             =('RAINQM')
        self.RCMINLAYER_CLUBB   =('RCMINLAYER_CLUBB')
        self.RCMTEND_CLUBB      =('RCMTEND_CLUBB')
        self.RCM_CLUBB          =('RCM_CLUBB')
        self.RELHUM             =('RELHUM')
        self.RELVAR             =('RELVAR')
        self.RHO_CLUBB          =('RHO_CLUBB')
        self.RIMTEND_CLUBB      =('RIMTEND_CLUBB')
        self.RTP2_CLUBB         =('RTP2_CLUBB')
        self.RTPTHLP_CLUBB      =('RTPTHLP_CLUBB')
        self.RVMTEND_CLUBB      =('RVMTEND_CLUBB')
        self.SFDMS              =('SFDMS')
        self.SFH2O2             =('SFH2O2')
        self.SFH2SO4            =('SFH2SO4')
        self.SFSO2              =('SFSO2')
        self.SFSOAG             =('SFSOAG')
        self.SFbc_a1            =('SFbc_a1')
        self.SFbc_a4            =('SFbc_a4')
        self.SFdst_a1           =('SFdst_a1')
        self.SFdst_a2           =('SFdst_a2')
        self.SFdst_a3           =('SFdst_a3')
        self.SFncl_a1           =('SFncl_a1')
        self.SFncl_a2           =('SFncl_a2')
        self.SFncl_a3           =('SFncl_a3')
        self.SFnum_a1           =('SFnum_a1')
        self.SFnum_a2           =('SFnum_a2')
        self.SFnum_a3           =('SFnum_a3')
        self.SFnum_a4           =('SFnum_a4')
        self.SFpom_a1           =('SFpom_a1')
        self.SFpom_a4           =('SFpom_a4')
        self.SFso4_a1           =('SFso4_a1')
        self.SFso4_a2           =('SFso4_a2')
        self.SFso4_a3           =('SFso4_a3')
        self.SFsoa_a1           =('SFsoa_a1')
        self.SFsoa_a2           =('SFsoa_a2')
        self.SHFLX              =('SHFLX')
        self.SL                 =('SL')
        self.SNOWHICE           =('SNOWHICE')
        self.SNOWHLND           =('SNOWHLND')
        self.SNOWQM             =('SNOWQM')
        self.SO2                =('SO2')
        self.SO2_CLXF           =('SO2_CLXF')
        self.SO2_CMXF           =('SO2_CMXF')
        self.SO2_SRF            =('SO2_SRF')
        self.SOAG               =('SOAG')
        self.SOAG_SRF           =('SOAG_SRF')
        self.SOLIN              =('SOLIN')
        self.STEND_CLUBB        =('STEND_CLUBB')
        self.SWCF               =('SWCF')
        self.T                  =('T')
        self.TAUBLJX            =('TAUBLJX')
        self.TAUBLJY            =('TAUBLJY')
        self.TAUGWX             =('TAUGWX')
        self.TAUGWY             =('TAUGWY')
        self.TAUX               =('TAUX')
        self.TAUY               =('TAUY')
        self.TDIFF              =('TDIFF')
        self.TGCLDCWP           =('TGCLDCWP')
        self.TGCLDIWP           =('TGCLDIWP')
        self.TGCLDLWP           =('TGCLDLWP')
        self.THLP2_CLUBB        =('THLP2_CLUBB')
        self.TMQ                =('TMQ')
        self.TREFHT             =('TREFHT')
        self.TS                 =('TS')
        self.TSMN               =('TSMN')
        self.TSMX               =('TSMX')
        self.U                  =('U')
        self.U10                =('U10')
        self.UM_CLUBB           =('UM_CLUBB')
        self.UP2_CLUBB          =('UP2_CLUBB')
        self.UPWP_CLUBB         =('UPWP_CLUBB')
        self.UTEND_CLUBB        =('UTEND_CLUBB')
        self.UU                 =('UU')
        self.V                  =('V')
        self.VD01               =('VD01')
        self.VM_CLUBB           =('VM_CLUBB')
        self.VP2_CLUBB          =('VP2_CLUBB')
        self.VPWP_CLUBB         =('VPWP_CLUBB')
        self.VQ                 =('VQ')
        self.VT                 =('VT')
        self.VTEND_CLUBB        =('VTEND_CLUBB')
        self.VU                 =('VU')
        self.VV                 =('VV')
        self.WD_H2O2            =('WD_H2O2')
        self.WD_H2SO4           =('WD_H2SO4')
        self.WD_SO2             =('WD_SO2')
        self.WP2_CLUBB          =('WP2_CLUBB')
        self.WP3_CLUBB          =('WP3_CLUBB')
        self.WPRCP_CLUBB        =('WPRCP_CLUBB')
        self.WPRTP_CLUBB        =('WPRTP_CLUBB')
        self.WPTHLP_CLUBB       =('WPTHLP_CLUBB')
        self.WPTHVP_CLUBB       =('WPTHVP_CLUBB')
        self.WSUB               =('WSUB')
        self.Z3                 =('Z3')
        self.ZM_CLUBB           =('ZM_CLUBB')
        self.ZT_CLUBB           =('ZT_CLUBB')
        self.bc_a1              =('bc_a1')
        self.bc_a1DDF           =('bc_a1DDF')
        self.bc_a1SFWET         =('bc_a1SFWET')
        self.bc_a1_SRF          =('bc_a1_SRF')
        self.bc_a4              =('bc_a4')
        self.bc_a4DDF           =('bc_a4DDF')
        self.bc_a4SFWET         =('bc_a4SFWET')
        self.bc_a4_CLXF         =('bc_a4_CLXF')
        self.bc_a4_CMXF         =('bc_a4_CMXF')
        self.bc_a4_SRF          =('bc_a4_SRF')
        self.bc_c1              =('bc_c1')
        self.bc_c1SFWET         =('bc_c1SFWET')
        self.bc_c4              =('bc_c4')
        self.bc_c4SFWET         =('bc_c4SFWET')
        self.dst_a1             =('dst_a1')
        self.dst_a1DDF          =('dst_a1DDF')
        self.dst_a1SF           =('dst_a1SF')
        self.dst_a1SFWET        =('dst_a1SFWET')
        self.dst_a1_SRF         =('dst_a1_SRF')
        self.dst_a2             =('dst_a2')
        self.dst_a2DDF          =('dst_a2DDF')
        self.dst_a2SF           =('dst_a2SF')
        self.dst_a2SFWET        =('dst_a2SFWET')
        self.dst_a2_SRF         =('dst_a2_SRF')
        self.dst_a3             =('dst_a3')
        self.dst_a3DDF          =('dst_a3DDF')
        self.dst_a3SF           =('dst_a3SF')
        self.dst_a3SFWET        =('dst_a3SFWET')
        self.dst_a3_SRF         =('dst_a3_SRF')
        self.dst_c1             =('dst_c1')
        self.dst_c1SFWET        =('dst_c1SFWET')
        self.dst_c2             =('dst_c2')
        self.dst_c2SFWET        =('dst_c2SFWET')
        self.dst_c3             =('dst_c3')
        self.dst_c3SFWET        =('dst_c3SFWET')
        self.ncl_a1             =('ncl_a1')
        self.ncl_a1DDF          =('ncl_a1DDF')
        self.ncl_a1SF           =('ncl_a1SF')
        self.ncl_a1SFWET        =('ncl_a1SFWET')
        self.ncl_a1_SRF         =('ncl_a1_SRF')
        self.ncl_a2             =('ncl_a2')
        self.ncl_a2DDF          =('ncl_a2DDF')
        self.ncl_a2SF           =('ncl_a2SF')
        self.ncl_a2SFWET        =('ncl_a2SFWET')
        self.ncl_a2_SRF         =('ncl_a2_SRF')
        self.ncl_a3             =('ncl_a3')
        self.ncl_a3DDF          =('ncl_a3DDF')
        self.ncl_a3SF           =('ncl_a3SF')
        self.ncl_a3SFWET        =('ncl_a3SFWET')
        self.ncl_a3_SRF         =('ncl_a3_SRF')
        self.ncl_c1             =('ncl_c1')
        self.ncl_c1SFWET        =('ncl_c1SFWET')
        self.ncl_c2             =('ncl_c2')
        self.ncl_c2SFWET        =('ncl_c2SFWET')
        self.ncl_c3             =('ncl_c3')
        self.ncl_c3SFWET        =('ncl_c3SFWET')
        self.num_a1             =('num_a1')
        self.num_a1DDF          =('num_a1DDF')
        self.num_a1SF           =('num_a1SF')
        self.num_a1SFWET        =('num_a1SFWET')
        self.num_a1_CLXF        =('num_a1_CLXF')
        self.num_a1_CMXF        =('num_a1_CMXF')
        self.num_a1_SRF         =('num_a1_SRF')
        self.num_a2             =('num_a2')
        self.num_a2DDF          =('num_a2DDF')
        self.num_a2SF           =('num_a2SF')
        self.num_a2SFWET        =('num_a2SFWET')
        self.num_a2_CLXF        =('num_a2_CLXF')
        self.num_a2_CMXF        =('num_a2_CMXF')
        self.num_a2_SRF         =('num_a2_SRF')
        self.num_a3             =('num_a3')
        self.num_a3DDF          =('num_a3DDF')
        self.num_a3SF           =('num_a3SF')
        self.num_a3SFWET        =('num_a3SFWET')
        self.num_a3_SRF         =('num_a3_SRF')
        self.num_a4             =('num_a4')
        self.num_a4DDF          =('num_a4DDF')
        self.num_a4SFWET        =('num_a4SFWET')
        self.num_a4_CLXF        =('num_a4_CLXF')
        self.num_a4_CMXF        =('num_a4_CMXF')
        self.num_a4_SRF         =('num_a4_SRF')
        self.num_c1             =('num_c1')
        self.num_c1SFWET        =('num_c1SFWET')
        self.num_c2             =('num_c2')
        self.num_c2SFWET        =('num_c2SFWET')
        self.num_c3             =('num_c3')
        self.num_c3SFWET        =('num_c3SFWET')
        self.num_c4             =('num_c4')
        self.num_c4SFWET        =('num_c4SFWET')
        self.pom_a1             =('pom_a1')
        self.pom_a1DDF          =('pom_a1DDF')
        self.pom_a1SFWET        =('pom_a1SFWET')
        self.pom_a1_SRF         =('pom_a1_SRF')
        self.pom_a4             =('pom_a4')
        self.pom_a4DDF          =('pom_a4DDF')
        self.pom_a4SFWET        =('pom_a4SFWET')
        self.pom_a4_CLXF        =('pom_a4_CLXF')
        self.pom_a4_CMXF        =('pom_a4_CMXF')
        self.pom_a4_SRF         =('pom_a4_SRF')
        self.pom_c1             =('pom_c1')
        self.pom_c1SFWET        =('pom_c1SFWET')
        self.pom_c4             =('pom_c4')
        self.pom_c4SFWET        =('pom_c4SFWET')
        self.so4_a1             =('so4_a1')
        self.so4_a1DDF          =('so4_a1DDF')
        self.so4_a1SFWET        =('so4_a1SFWET')
        self.so4_a1_CLXF        =('so4_a1_CLXF')
        self.so4_a1_CMXF        =('so4_a1_CMXF')
        self.so4_a1_SRF         =('so4_a1_SRF')
        self.so4_a2             =('so4_a2')
        self.so4_a2DDF          =('so4_a2DDF')
        self.so4_a2SFWET        =('so4_a2SFWET')
        self.so4_a2_CLXF        =('so4_a2_CLXF')
        self.so4_a2_CMXF        =('so4_a2_CMXF')
        self.so4_a2_SRF         =('so4_a2_SRF')
        self.so4_a3             =('so4_a3')
        self.so4_a3DDF          =('so4_a3DDF')
        self.so4_a3SFWET        =('so4_a3SFWET')
        self.so4_a3_SRF         =('so4_a3_SRF')
        self.so4_c1             =('so4_c1')
        self.so4_c1SFWET        =('so4_c1SFWET')
        self.so4_c2             =('so4_c2')
        self.so4_c2SFWET        =('so4_c2SFWET')
        self.so4_c3             =('so4_c3')
        self.so4_c3SFWET        =('so4_c3SFWET')
        self.soa_a1             =('soa_a1')
        self.soa_a1DDF          =('soa_a1DDF')
        self.soa_a1SFWET        =('soa_a1SFWET')
        self.soa_a1_SRF         =('soa_a1_SRF')
        self.soa_a2             =('soa_a2')
        self.soa_a2DDF          =('soa_a2DDF')
        self.soa_a2SFWET        =('soa_a2SFWET')
        self.soa_a2_SRF         =('soa_a2_SRF')
        self.soa_c1             =('soa_c1')
        self.soa_c1SFWET        =('soa_c1SFWET')
        self.soa_c2             =('soa_c2')
        self.soa_c2SFWET        =('soa_c2SFWET')
        self.PRECT              =('PRECT')
        self.CMFMCDZM           =('CMFMCDZM')
        self.ZMMU               =('ZMMU')
        self.ZMMD               =('ZMMD')
        self.CMFMC              =('CMFMC')
        #self.CBMF               =('CBMF')
        self.TKEIC              =('TKE&IC')


    def __iter__(self):
        for each in self.__dict__.keys():
            yield self.__getattribute__(each)

#To assint the label of the family of 
#variables

def ncload(file_l,calendar):

    label=variables() 

    # Your filename
    nc_file    = '%s'%(file_l)  

    # Dataset is the class behavior to open the file
    # and create an instance of the ncCDF4 class
    nc_v = Dataset(nc_file, 'r')    

    label.lat                = nc_v.variables['lat']  
    label.lon                = nc_v.variables['lon']
    label.ntrk               = nc_v.variables['ntrk']
    label.ntrn               = nc_v.variables['ntrn']
    label.ntrm               = nc_v.variables['ntrm']
    label.gw                 = nc_v.variables['gw']
    label.lev                = nc_v.variables['lev']
    label.hyam               = nc_v.variables['hyam']
    label.hybm               = nc_v.variables['hybm']
    label.P0                 = nc_v.variables['P0']
    label.ilev               = nc_v.variables['ilev']
    label.hyai               = nc_v.variables['hyai']
    label.hybi               = nc_v.variables['hybi']
    label.time               = nc_v.variables['time']
    label.date               = nc_v.variables['date']
    label.datesec            = nc_v.variables['datesec']
    label.time_bnds          = nc_v.variables['time_bnds']
    label.date_written       = nc_v.variables['date_written']
    label.time_written       = nc_v.variables['time_written']
    label.ndbase             = nc_v.variables['ndbase']
    label.nsbase             = nc_v.variables['nsbase']
    label.nbdate             = nc_v.variables['nbdate']
    label.nbsec              = nc_v.variables['nbsec']
    label.mdt                = nc_v.variables['mdt']
    label.ndcur              = nc_v.variables['ndcur']
    label.nscur              = nc_v.variables['nscur']
    label.co2vmr             = nc_v.variables['co2vmr']
    label.ch4vmr             = nc_v.variables['ch4vmr']
    label.n2ovmr             = nc_v.variables['n2ovmr']
    label.f11vmr             = nc_v.variables['f11vmr']
    label.f12vmr             = nc_v.variables['f12vmr']
    label.sol_tsi            = nc_v.variables['sol_tsi']
    label.nsteph             = nc_v.variables['nsteph']
    label.ADRAIN             = nc_v.variables['ADRAIN']
    label.ADSNOW             = nc_v.variables['ADSNOW']
    label.AEROD_v            = nc_v.variables['AEROD_v']
    label.ANRAIN             = nc_v.variables['ANRAIN']
    label.ANSNOW             = nc_v.variables['ANSNOW']
    label.AODDUST            = nc_v.variables['AODDUST']
    label.AODDUST1           = nc_v.variables['AODDUST1']
    label.AODDUST3           = nc_v.variables['AODDUST3']
    label.AODVIS             = nc_v.variables['AODVIS']
    label.AQRAIN             = nc_v.variables['AQRAIN']
    label.AQSNOW             = nc_v.variables['AQSNOW']
    label.AREI               = nc_v.variables['AREI']
    label.AREL               = nc_v.variables['AREL']
    label.AWNC               = nc_v.variables['AWNC']
    label.AWNI               = nc_v.variables['AWNI']
    label.CCN3               = nc_v.variables['CCN3']
    label.CDNUMC             = nc_v.variables['CDNUMC']
    label.CLDHGH             = nc_v.variables['CLDHGH']
    label.CLDICE             = nc_v.variables['CLDICE']
    label.CLDLIQ             = nc_v.variables['CLDLIQ']
    label.CLDLOW             = nc_v.variables['CLDLOW']
    label.CLDMED             = nc_v.variables['CLDMED']
    label.CLDTOT             = nc_v.variables['CLDTOT']
    label.CLOUD              = nc_v.variables['CLOUD']
    #label.CLOUDCOVER_CLUBB   = nc_v.variables['CLOUDCOVER_CLUBB']
    #label.CLOUDFRAC_CLUBB    = nc_v.variables['CLOUDFRAC_CLUBB']
    #label.CONCLD             = nc_v.variables['CONCLD']
    label.DCQ                = nc_v.variables['DCQ']
    label.DF_H2O2            = nc_v.variables['DF_H2O2']
    label.DF_H2SO4           = nc_v.variables['DF_H2SO4']
    label.DF_SO2             = nc_v.variables['DF_SO2']
    label.DMS                = nc_v.variables['DMS']
    label.DMS_SRF            = nc_v.variables['DMS_SRF']
    label.DTCOND             = nc_v.variables['DTCOND']
    label.DTH                = nc_v.variables['DTH']
    label.DTV                = nc_v.variables['DTV']
    label.DTWR_H2O2          = nc_v.variables['DTWR_H2O2']
    label.DTWR_H2SO4         = nc_v.variables['DTWR_H2SO4']
    label.DTWR_SO2           = nc_v.variables['DTWR_SO2']
    label.FICE               = nc_v.variables['FICE']
    label.FLDS               = nc_v.variables['FLDS']
    label.FLNS               = nc_v.variables['FLNS']
    label.FLNSC              = nc_v.variables['FLNSC']
    label.FLNT               = nc_v.variables['FLNT']
    label.FLNTC              = nc_v.variables['FLNTC']
    label.FLUT               = nc_v.variables['FLUT']
    label.FLUTC              = nc_v.variables['FLUTC']
    label.FREQCLR            = nc_v.variables['FREQCLR']
    label.FREQI              = nc_v.variables['FREQI']
    label.FREQL              = nc_v.variables['FREQL']
    label.FREQR              = nc_v.variables['FREQR']
    label.FREQS              = nc_v.variables['FREQS']
    label.FREQSL             = nc_v.variables['FREQSL']
    label.FSDS               = nc_v.variables['FSDS']
    label.FSDSC              = nc_v.variables['FSDSC']
    label.FSNS               = nc_v.variables['FSNS']
    label.FSNSC              = nc_v.variables['FSNSC']
    label.FSNT               = nc_v.variables['FSNT']
    label.FSNTC              = nc_v.variables['FSNTC']
    label.FSNTOA             = nc_v.variables['FSNTOA']
    label.FSNTOAC            = nc_v.variables['FSNTOAC']
    label.FSUTOA             = nc_v.variables['FSUTOA']
    label.H2O                = nc_v.variables['H2O']
    label.H2O2               = nc_v.variables['H2O2']
    label.H2O2_SRF           = nc_v.variables['H2O2_SRF']
    label.H2O_CMXF           = nc_v.variables['H2O_CMXF']
    label.H2O_SRF            = nc_v.variables['H2O_SRF']
    label.H2SO4              = nc_v.variables['H2SO4']
    label.H2SO4_SRF          = nc_v.variables['H2SO4_SRF']
    label.ICEFRAC            = nc_v.variables['ICEFRAC']
    label.ICIMR              = nc_v.variables['ICIMR']
    label.ICWMR              = nc_v.variables['ICWMR']
    label.IWC                = nc_v.variables['IWC']
    label.LANDFRAC           = nc_v.variables['LANDFRAC']
    label.LHFLX              = nc_v.variables['LHFLX']
    label.LS_FLXPRC          = nc_v.variables['LS_FLXPRC']
    label.LWCF               = nc_v.variables['LWCF']
    label.NUMICE             = nc_v.variables['NUMICE']
    label.NUMLIQ             = nc_v.variables['NUMLIQ']
    label.NUMRAI             = nc_v.variables['NUMRAI']
    label.NUMSNO             = nc_v.variables['NUMSNO']
    label.OCNFRAC            = nc_v.variables['OCNFRAC']
    label.OMEGA              = nc_v.variables['OMEGA']
    label.OMEGAT             = nc_v.variables['OMEGAT']
    label.PBLH               = nc_v.variables['PBLH']
    label.PHIS               = nc_v.variables['PHIS']
    label.PRECC              = nc_v.variables['PRECC']
    label.PRECL              = nc_v.variables['PRECL']
    label.PRECSC             = nc_v.variables['PRECSC']
    label.PRECSL             = nc_v.variables['PRECSL']
    label.PS                 = nc_v.variables['PS']
    label.PSL                = nc_v.variables['PSL']
    label.Q                  = nc_v.variables['Q']
    label.QDIFF              = nc_v.variables['QDIFF']
    label.QFLX               = nc_v.variables['QFLX']
    label.QREFHT             = nc_v.variables['QREFHT']
    label.QRL                = nc_v.variables['QRL']
    label.QRS                = nc_v.variables['QRS']
    #label.QT                 = nc_v.variables['QT']
    label.RAINQM             = nc_v.variables['RAINQM']
    #label.RCMINLAYER_CLUBB   = nc_v.variables['RCMINLAYER_CLUBB']
    #label.RCMTEND_CLUBB      = nc_v.variables['RCMTEND_CLUBB']
    #label.RCM_CLUBB          = nc_v.variables['RCM_CLUBB']
    #label.RELHUM             = nc_v.variables['RELHUM']
    #label.RELVAR             = nc_v.variables['RELVAR']
    #label.RHO_CLUBB          = nc_v.variables['RHO_CLUBB']
    #label.RIMTEND_CLUBB      = nc_v.variables['RIMTEND_CLUBB']
    #label.RTP2_CLUBB         = nc_v.variables['RTP2_CLUBB']
    #label.RTPTHLP_CLUBB      = nc_v.variables['RTPTHLP_CLUBB']
    #label.RVMTEND_CLUBB      = nc_v.variables['RVMTEND_CLUBB']
    label.SFDMS              = nc_v.variables['SFDMS']
    label.SFH2O2             = nc_v.variables['SFH2O2']
    label.SFH2SO4            = nc_v.variables['SFH2SO4']
    label.SFSO2              = nc_v.variables['SFSO2']
    label.SFSOAG             = nc_v.variables['SFSOAG']
    label.SFbc_a1            = nc_v.variables['SFbc_a1']
    label.SFbc_a4            = nc_v.variables['SFbc_a4']
    label.SFdst_a1           = nc_v.variables['SFdst_a1']
    label.SFdst_a2           = nc_v.variables['SFdst_a2']
    label.SFdst_a3           = nc_v.variables['SFdst_a3']
    label.SFncl_a1           = nc_v.variables['SFncl_a1']
    label.SFncl_a2           = nc_v.variables['SFncl_a2']
    label.SFncl_a3           = nc_v.variables['SFncl_a3']
    label.SFnum_a1           = nc_v.variables['SFnum_a1']
    label.SFnum_a2           = nc_v.variables['SFnum_a2']
    label.SFnum_a3           = nc_v.variables['SFnum_a3']
    label.SFnum_a4           = nc_v.variables['SFnum_a4']
    label.SFpom_a1           = nc_v.variables['SFpom_a1']
    label.SFpom_a4           = nc_v.variables['SFpom_a4']
    label.SFso4_a1           = nc_v.variables['SFso4_a1']
    label.SFso4_a2           = nc_v.variables['SFso4_a2']
    label.SFso4_a3           = nc_v.variables['SFso4_a3']
    label.SFsoa_a1           = nc_v.variables['SFsoa_a1']
    label.SFsoa_a2           = nc_v.variables['SFsoa_a2']
    label.SHFLX              = nc_v.variables['SHFLX']
    #label.SL                 = nc_v.variables['SL']
    label.SNOWHICE           = nc_v.variables['SNOWHICE']
    label.SNOWHLND           = nc_v.variables['SNOWHLND']
    label.SNOWQM             = nc_v.variables['SNOWQM']
    label.SO2                = nc_v.variables['SO2']
    label.SO2_CLXF           = nc_v.variables['SO2_CLXF']
    label.SO2_CMXF           = nc_v.variables['SO2_CMXF']
    label.SO2_SRF            = nc_v.variables['SO2_SRF']
    label.SOAG               = nc_v.variables['SOAG']
    label.SOAG_SRF           = nc_v.variables['SOAG_SRF']
    label.SOLIN              = nc_v.variables['SOLIN']
    #label.STEND_CLUBB        = nc_v.variables['STEND_CLUBB']
    label.SWCF               = nc_v.variables['SWCF']
    label.T                  = nc_v.variables['T']
    label.TAUBLJX            = nc_v.variables['TAUBLJX']
    label.TAUBLJY            = nc_v.variables['TAUBLJY']
    label.TAUGWX             = nc_v.variables['TAUGWX']
    label.TAUGWY             = nc_v.variables['TAUGWY']
    label.TAUX               = nc_v.variables['TAUX']
    label.TAUY               = nc_v.variables['TAUY']
    label.TDIFF              = nc_v.variables['TDIFF']
    label.TGCLDCWP           = nc_v.variables['TGCLDCWP']
    label.TGCLDIWP           = nc_v.variables['TGCLDIWP']
    label.TGCLDLWP           = nc_v.variables['TGCLDLWP']
    #label.THLP2_CLUBB        = nc_v.variables['THLP2_CLUBB']
    label.TMQ                = nc_v.variables['TMQ']
    label.TREFHT             = nc_v.variables['TREFHT']
    label.TS                 = nc_v.variables['TS']
    label.TSMN               = nc_v.variables['TSMN']
    label.TSMX               = nc_v.variables['TSMX']
    label.U                  = nc_v.variables['U']
    label.U10                = nc_v.variables['U10']
    #label.UM_CLUBB           = nc_v.variables['UM_CLUBB']
    #label.UP2_CLUBB          = nc_v.variables['UP2_CLUBB']
    #label.UPWP_CLUBB         = nc_v.variables['UPWP_CLUBB']
    #label.UTEND_CLUBB        = nc_v.variables['UTEND_CLUBB']
    label.UU                 = nc_v.variables['UU']
    label.V                  = nc_v.variables['V']
    label.VD01               = nc_v.variables['VD01']
    #label.VM_CLUBB           = nc_v.variables['VM_CLUBB']
    #label.VP2_CLUBB          = nc_v.variables['VP2_CLUBB']
    #label.VPWP_CLUBB         = nc_v.variables['VPWP_CLUBB']
    label.VQ                 = nc_v.variables['VQ']
    label.VT                 = nc_v.variables['VT']
    #label.VTEND_CLUBB        = nc_v.variables['VTEND_CLUBB']
    label.VU                 = nc_v.variables['VU']
    label.VV                 = nc_v.variables['VV']
    label.WD_H2O2            = nc_v.variables['WD_H2O2']
    label.WD_H2SO4           = nc_v.variables['WD_H2SO4']
    label.WD_SO2             = nc_v.variables['WD_SO2']
    #label.WP2_CLUBB          = nc_v.variables['WP2_CLUBB']
    #label.WP3_CLUBB          = nc_v.variables['WP3_CLUBB']
    #label.WPRCP_CLUBB        = nc_v.variables['WPRCP_CLUBB']
    #label.WPRTP_CLUBB        = nc_v.variables['WPRTP_CLUBB']
    #label.WPTHLP_CLUBB       = nc_v.variables['WPTHLP_CLUBB']
    #label.WPTHVP_CLUBB       = nc_v.variables['WPTHVP_CLUBB']
    label.WSUB               = nc_v.variables['WSUB']
    label.Z3                 = nc_v.variables['Z3']
    #label.ZM_CLUBB           = nc_v.variables['ZM_CLUBB']
    #label.ZT_CLUBB           = nc_v.variables['ZT_CLUBB']
    label.bc_a1              = nc_v.variables['bc_a1']
    label.bc_a1DDF           = nc_v.variables['bc_a1DDF']
    label.bc_a1SFWET         = nc_v.variables['bc_a1SFWET']
    label.bc_a1_SRF          = nc_v.variables['bc_a1_SRF']
    label.bc_a4              = nc_v.variables['bc_a4']
    label.bc_a4DDF           = nc_v.variables['bc_a4DDF']
    label.bc_a4SFWET         = nc_v.variables['bc_a4SFWET']
    label.bc_a4_CLXF         = nc_v.variables['bc_a4_CLXF']
    label.bc_a4_CMXF         = nc_v.variables['bc_a4_CMXF']
    label.bc_a4_SRF          = nc_v.variables['bc_a4_SRF']
    label.bc_c1              = nc_v.variables['bc_c1']
    label.bc_c1SFWET         = nc_v.variables['bc_c1SFWET']
    label.bc_c4              = nc_v.variables['bc_c4']
    label.bc_c4SFWET         = nc_v.variables['bc_c4SFWET']
    label.dst_a1             = nc_v.variables['dst_a1']
    label.dst_a1DDF          = nc_v.variables['dst_a1DDF']
    label.dst_a1SF           = nc_v.variables['dst_a1SF']
    label.dst_a1SFWET        = nc_v.variables['dst_a1SFWET']
    label.dst_a1_SRF         = nc_v.variables['dst_a1_SRF']
    label.dst_a2             = nc_v.variables['dst_a2']
    label.dst_a2DDF          = nc_v.variables['dst_a2DDF']
    label.dst_a2SF           = nc_v.variables['dst_a2SF']
    label.dst_a2SFWET        = nc_v.variables['dst_a2SFWET']
    label.dst_a2_SRF         = nc_v.variables['dst_a2_SRF']
    label.dst_a3             = nc_v.variables['dst_a3']
    label.dst_a3DDF          = nc_v.variables['dst_a3DDF']
    label.dst_a3SF           = nc_v.variables['dst_a3SF']
    label.dst_a3SFWET        = nc_v.variables['dst_a3SFWET']
    label.dst_a3_SRF         = nc_v.variables['dst_a3_SRF']
    label.dst_c1             = nc_v.variables['dst_c1']
    label.dst_c1SFWET        = nc_v.variables['dst_c1SFWET']
    label.dst_c2             = nc_v.variables['dst_c2']
    label.dst_c2SFWET        = nc_v.variables['dst_c2SFWET']
    label.dst_c3             = nc_v.variables['dst_c3']
    label.dst_c3SFWET        = nc_v.variables['dst_c3SFWET']
    label.ncl_a1             = nc_v.variables['ncl_a1']
    label.ncl_a1DDF          = nc_v.variables['ncl_a1DDF']
    label.ncl_a1SF           = nc_v.variables['ncl_a1SF']
    label.ncl_a1SFWET        = nc_v.variables['ncl_a1SFWET']
    label.ncl_a1_SRF         = nc_v.variables['ncl_a1_SRF']
    label.ncl_a2             = nc_v.variables['ncl_a2']
    label.ncl_a2DDF          = nc_v.variables['ncl_a2DDF']
    label.ncl_a2SF           = nc_v.variables['ncl_a2SF']
    label.ncl_a2SFWET        = nc_v.variables['ncl_a2SFWET']
    label.ncl_a2_SRF         = nc_v.variables['ncl_a2_SRF']
    label.ncl_a3             = nc_v.variables['ncl_a3']
    label.ncl_a3DDF          = nc_v.variables['ncl_a3DDF']
    label.ncl_a3SF           = nc_v.variables['ncl_a3SF']
    label.ncl_a3SFWET        = nc_v.variables['ncl_a3SFWET']
    label.ncl_a3_SRF         = nc_v.variables['ncl_a3_SRF']
    label.ncl_c1             = nc_v.variables['ncl_c1']
    label.ncl_c1SFWET        = nc_v.variables['ncl_c1SFWET']
    label.ncl_c2             = nc_v.variables['ncl_c2']
    label.ncl_c2SFWET        = nc_v.variables['ncl_c2SFWET']
    label.ncl_c3             = nc_v.variables['ncl_c3']
    label.ncl_c3SFWET        = nc_v.variables['ncl_c3SFWET']
    label.num_a1             = nc_v.variables['num_a1']
    label.num_a1DDF          = nc_v.variables['num_a1DDF']
    label.num_a1SF           = nc_v.variables['num_a1SF']
    label.num_a1SFWET        = nc_v.variables['num_a1SFWET']
    label.num_a1_CLXF        = nc_v.variables['num_a1_CLXF']
    label.num_a1_CMXF        = nc_v.variables['num_a1_CMXF']
    label.num_a1_SRF         = nc_v.variables['num_a1_SRF']
    label.num_a2             = nc_v.variables['num_a2']
    label.num_a2DDF          = nc_v.variables['num_a2DDF']
    label.num_a2SF           = nc_v.variables['num_a2SF']
    label.num_a2SFWET        = nc_v.variables['num_a2SFWET']
    label.num_a2_CLXF        = nc_v.variables['num_a2_CLXF']
    label.num_a2_CMXF        = nc_v.variables['num_a2_CMXF']
    label.num_a2_SRF         = nc_v.variables['num_a2_SRF']
    label.num_a3             = nc_v.variables['num_a3']
    label.num_a3DDF          = nc_v.variables['num_a3DDF']
    label.num_a3SF           = nc_v.variables['num_a3SF']
    label.num_a3SFWET        = nc_v.variables['num_a3SFWET']
    label.num_a3_SRF         = nc_v.variables['num_a3_SRF']
    label.num_a4             = nc_v.variables['num_a4']
    label.num_a4DDF          = nc_v.variables['num_a4DDF']
    label.num_a4SFWET        = nc_v.variables['num_a4SFWET']
    label.num_a4_CLXF        = nc_v.variables['num_a4_CLXF']
    label.num_a4_CMXF        = nc_v.variables['num_a4_CMXF']
    label.num_a4_SRF         = nc_v.variables['num_a4_SRF']
    label.num_c1             = nc_v.variables['num_c1']
    label.num_c1SFWET        = nc_v.variables['num_c1SFWET']
    label.num_c2             = nc_v.variables['num_c2']
    label.num_c2SFWET        = nc_v.variables['num_c2SFWET']
    label.num_c3             = nc_v.variables['num_c3']
    label.num_c3SFWET        = nc_v.variables['num_c3SFWET']
    label.num_c4             = nc_v.variables['num_c4']
    label.num_c4SFWET        = nc_v.variables['num_c4SFWET']
    label.pom_a1             = nc_v.variables['pom_a1']
    label.pom_a1DDF          = nc_v.variables['pom_a1DDF']
    label.pom_a1SFWET        = nc_v.variables['pom_a1SFWET']
    label.pom_a1_SRF         = nc_v.variables['pom_a1_SRF']
    label.pom_a4             = nc_v.variables['pom_a4']
    label.pom_a4DDF          = nc_v.variables['pom_a4DDF']
    label.pom_a4SFWET        = nc_v.variables['pom_a4SFWET']
    label.pom_a4_CLXF        = nc_v.variables['pom_a4_CLXF']
    label.pom_a4_CMXF        = nc_v.variables['pom_a4_CMXF']
    label.pom_a4_SRF         = nc_v.variables['pom_a4_SRF']
    label.pom_c1             = nc_v.variables['pom_c1']
    label.pom_c1SFWET        = nc_v.variables['pom_c1SFWET']
    label.pom_c4             = nc_v.variables['pom_c4']
    label.pom_c4SFWET        = nc_v.variables['pom_c4SFWET']
    label.so4_a1             = nc_v.variables['so4_a1']
    label.so4_a1DDF          = nc_v.variables['so4_a1DDF']
    label.so4_a1SFWET        = nc_v.variables['so4_a1SFWET']
    label.so4_a1_CLXF        = nc_v.variables['so4_a1_CLXF']
    label.so4_a1_CMXF        = nc_v.variables['so4_a1_CMXF']
    label.so4_a1_SRF         = nc_v.variables['so4_a1_SRF']
    label.so4_a2             = nc_v.variables['so4_a2']
    label.so4_a2DDF          = nc_v.variables['so4_a2DDF']
    label.so4_a2SFWET        = nc_v.variables['so4_a2SFWET']
    label.so4_a2_CLXF        = nc_v.variables['so4_a2_CLXF']
    label.so4_a2_CMXF        = nc_v.variables['so4_a2_CMXF']
    label.so4_a2_SRF         = nc_v.variables['so4_a2_SRF']
    label.so4_a3             = nc_v.variables['so4_a3']
    label.so4_a3DDF          = nc_v.variables['so4_a3DDF']
    label.so4_a3SFWET        = nc_v.variables['so4_a3SFWET']
    label.so4_a3_SRF         = nc_v.variables['so4_a3_SRF']
    label.so4_c1             = nc_v.variables['so4_c1']
    label.so4_c1SFWET        = nc_v.variables['so4_c1SFWET']
    label.so4_c2             = nc_v.variables['so4_c2']
    label.so4_c2SFWET        = nc_v.variables['so4_c2SFWET']
    label.so4_c3             = nc_v.variables['so4_c3']
    label.so4_c3SFWET        = nc_v.variables['so4_c3SFWET']
    label.soa_a1             = nc_v.variables['soa_a1']
    label.soa_a1DDF          = nc_v.variables['soa_a1DDF']
    label.soa_a1SFWET        = nc_v.variables['soa_a1SFWET']
    label.soa_a1_SRF         = nc_v.variables['soa_a1_SRF']
    label.soa_a2             = nc_v.variables['soa_a2']
    label.soa_a2DDF          = nc_v.variables['soa_a2DDF']
    label.soa_a2SFWET        = nc_v.variables['soa_a2SFWET']
    label.soa_a2_SRF         = nc_v.variables['soa_a2_SRF']
    label.soa_c1             = nc_v.variables['soa_c1']
    label.soa_c1SFWET        = nc_v.variables['soa_c1SFWET']
    label.soa_c2             = nc_v.variables['soa_c2']
    label.soa_c2SFWET        = nc_v.variables['soa_c2SFWET']
    label.PRECT              = nc_v.variables['PRECT']
    label.CMFMCDZM           = nc_v.variables['CMFMCDZM']
    label.ZMMU               = nc_v.variables['ZMMU']
    label.ZMMD               = nc_v.variables['ZMMD']
    label.CMFMC              = nc_v.variables['CMFMC']
    #label.CBMF               = nc_v.variables['CBMF']
    label.TKE                = nc_v.variables['TKE']

    tu = calendar[0] 
    tc = calendar[1]
    #tu = "days since 2014-02-15T00:00:00 +04:00:00"
    #tc = "gregorian"
    #tc = "noleap"

    print (label.time.units)

    #label.data       = num2date(label.time,units=nc_v.variables['time'].units,calendar=nc_v.variables['time'].calendar)

    #label.data       = num2date(label.time[:],units=tu,calendar=tc)

    label.data       = num2pydate(label.time[:],units=tu,calendar=tc)


    return label 

#	levgrnd 
#	levlak
#	levdcmp
#	time 
#	mcdate 
#	mcsec 
#	mdcur 
#	mscur 
#	nstep 
#	time_bounds
#	date_written
#	time_written
#	lon
#	lat
#	area 
#	landfrac 
#	landmask 
#	pftmask 
#	nbedrock 
#	ZSOI 
#	DZSOI 
#	WATSAT 
#	SUCSAT 
#	BSW 
#	HKSAT 
#	ZLAKE 
#	DZLAKE 
#	ATM_TOPO 
#	BCDEP 
#	BTRAN2 
#	BTRANMN 
#	DSL 
#	DSTDEP 
#	DSTFLXT 
#	EFLXBUILD 
#	EFLX_DYNBAL 
#	EFLX_GRND_LAKE 
#	EFLX_LH_TOT 
#	EFLX_LH_TOT_R 
#	ELAI 
#	ERRH2O 
#	ERRH2OSNO 
#	ERRSEB 
#	ERRSOI 
#	ERRSOL 
#	ESAI 
#	FCEV 
#	FCOV 
#	FCTR 
#	FGEV 
#	FGR 
#	FGR12 
#	FH2OSFC 
#	FIRA 
#	FIRA_R 
#	FIRE 
#	FIRE_R 
#	FLDS 
#	FPSN 
#	FSA 
#	FSAT 
#	FSDS 
#	FSDSND 
#	FSDSNDLN 
#	FSDSNI 
#	FSDSVD 
#	FSDSVDLN 
#	FSDSVI 
#	FSDSVILN 
#	FSH 
#	FSH_G 
#	FSH_PRECIP_CONVERSION 
#	FSH_R 
#	FSH_RUNOFF_ICE_TO_LIQ 
#	FSH_TO_COUPLER 
#	FSH_V 
#	FSM 
#	FSNO 
#	FSNO_EFF 
#	FSR 
#	FSRND 
#	FSRNDLN 
#	FSRNI 
#	FSRVD 
#	FSRVDLN 
#	FSRVI 
#	GSSHA 
#	GSSHALN 
#	GSSUN 
#	GSSUNLN 
#	H2OCAN 
#	H2OSFC 
#	H2OSNO 
#	H2OSNO_TOP 
#	H2OSOI
#	HEAT_CONTENT1 
#	HEAT_FROM_AC 
#	HIA 
#	HIA_R 
#	HIA_U 
#	HUMIDEX 
#	HUMIDEX_R 
#	HUMIDEX_U 
#	ICE_CONTENT1 
#	JMX25T 
#	Jmx25Z 
#	LAISHA 
#	LAISUN 
#	LAKEICEFRAC_SURF 
#	LAKEICETHICK 
#	LIQCAN 
#	LIQUID_CONTENT1 
#	LNC 
#	OCDEP 
#	PARVEGLN 
#	PBOT 
#	PCO2 
#	PCT_CFT
#	PCT_GLC_MEC
#	PCT_LANDUNIT
#	PCT_NAT_PFT
#	Q2M 
#	QBOT 
#	QCHARGE 
#	QDRAI 
#	QDRAI_PERCH 
#	QDRAI_XS 
#	QDRIP 
#	QFLOOD 
#	QFLX_DEW_GRND 
#	QFLX_DEW_SNOW 
#	QFLX_EVAP_TOT 
#	QFLX_ICE_DYNBAL 
#	QFLX_LIQ_DYNBAL 
#	QFLX_SNOW_DRAIN 
#	QFLX_SNOW_DRAIN_ICE 
#	QFLX_SUB_SNOW 
#	QH2OSFC 
#	QICE 
#	QICE_FRZ 
#	QICE_MELT 
#	QINFL 
#	QINTR 
#	QIRRIG 
#	QOVER 
#	QRGWL 
#	QRUNOFF 
#	QRUNOFF_ICE 
#	QRUNOFF_ICE_TO_COUPLER 
#	QRUNOFF_TO_COUPLER 
#	QSNOCPLIQ 
#	QSNOEVAP 
#	QSNOFRZ 
#	QSNOFRZ_ICE 
#	QSNOMELT 
#	QSNOMELT_ICE 
#	QSNO_TEMPUNLOAD 
#	QSNO_WINDUNLOAD 
#	QSNWCPICE 
#	QSOIL 
#	QSOIL_ICE 
#	QVEGE 
#	QVEGT 
#	RAIN 
#	RAIN_FROM_ATM 
#	RH2M 
#	RSSHA 
#	RSSUN 
#	SABG 
#	SABG_PEN 
#	SABV 
#	SMP
#	SNOBCMCL 
#	SNOBCMSL 
#	SNOCAN 
#	SNODSTMCL 
#	SNODSTMSL 
#	SNOFSRND 
#	SNOFSRNI 
#	SNOFSRVD 
#	SNOFSRVI 
#	SNOINTABS 
#	SNOOCMCL 
#	SNOOCMSL 
#	SNOTXMASS 
#	SNOUNLOAD 
#	SNOW 
#	SNOWDP 
#	SNOWICE 
#	SNOWLIQ 
#	SNOW_DEPTH 
#	SNOW_FROM_ATM 
#	SNOW_PERSISTENCE 
#	SNOW_SINKS 
#	SNOW_SOURCES 
#	SOILICE
#	SOILLIQ
#	SOILRESIS 
#	SOILWATER_10CM 
#	SWBGT 
#	SWBGT_R 
#	SWBGT_U 
#	TAUX 
#	TAUY 
#	TBOT 
#	TBUILD 
#	TG 
#	TH2OSFC 
#	THBOT 
#	TKE1 
#	TLAI 
#	TLAKE
#	TOTSOILICE 
#	TOTSOILLIQ 
#	TPU25T 
#	TREFMNAV 
#	TREFMXAV 
#	TSA 
#	TSAI 
#	TSKIN 
#	TSL 
#	TSOI
#	TSOI_10CM 
#	TSOI_ICE
#	TV 
#	TWS 
#	U10 
#	U10_DUST 
#	URBAN_AC 
#	URBAN_HEAT 
#	VCMX25T 
#	VEGWP
#	VOLR 
#	VOLRMCH 
#	Vcmx25Z 
#	WA 
#	WASTEHEAT 
#	WBT 
#	WBT_R 
#	WBT_U 
#	WIND 
#	ZBOT 
#	ZWT 
#	ZWT_PERCH 
