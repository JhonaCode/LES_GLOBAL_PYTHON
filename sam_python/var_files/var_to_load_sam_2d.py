################################################# 
# Program to read variable of a nc file 
# using python with NetCdf
# Create by: Jhonatan Aguirre 
# Date:06/02/2020
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

        self.time        ='time'   
        self.x           ='x'   
        self.y           ='y'   
        self.Prec        ='Prec'   
        self.LWNS        ='LWNS'      
        self.LWNSC       ='LWNS'      
        self.LWNT        ='LWNT'      
        self.LWNTC       ='LWNT'      
        self.SOLIN       ='SOLI'      
        self.SWNS        ='SWNS'      
        self.SWNSC       ='SWNS'      
        self.SWNT        ='SWNT'      
        self.SWNTC       ='SWNT'      
        self.CWP         ='CWP'      
        self.IWP         ='IWP'      
        self.CLD         ='CLD'      
        self.PW          ='PW'       
        self.USFC        ='USFC'      
        self.U200        ='U200'      
        self.VSFC        ='VSFC'      
        self.V200        ='V200'      
        self.W500        ='W500'      
        self.PSFC        ='PSFC'      
        self.SWVP        ='SWVP'      
        self.U850        ='U850'      
        self.V850        ='V850'      
        self.ZC          ='ZC'       
        self.TB          ='TB'       
        self.ZE          ='ZE'       
        self.CLDC        ='CLDC'      

    def __iter__(self):
        for each in self.__dict__.keys():
            yield self.__getattribute__(each)

#To assint the label of the family of 
#variables

def ncload(name,dates,file_l,calendar,vars_1d=[],vars_2d=[],vars_diurnal=[],dates_d=[]):

    #load class
    label=variables()

    #put the objets in class

    label.datei=dt.datetime(dates[0][0],dates[0][1],dates[0][2],dates[0][3])
    label.datef=dt.datetime(dates[1][0],dates[1][1],dates[1][2],dates[1][3])

    if len(dates_d)>0:
        label.datei_diurnal=dt.datetime(dates_d[0][0],dates_d[0][1],dates_d[0][2],dates_d[0][3])
        label.datef_diurnal=dt.datetime(dates_d[1][0],dates_d[1][1],dates_d[1][2],dates_d[1][3])
    else:
        print('Diurnal dates experiment was no defined')

    label.name=name
    label.var1d=vars_1d
    label.var2d=vars_2d
    label.vars_diurnal=vars_diurnal

    # Your filename
    nc_file    = '%s'%(file_l)


    # Dataset is the class behavior to open the file
    # and create an instance of the ncCDF4 class
    nc_v = Dataset(nc_file, 'r')

    label.nc_f       =nc_v 

    ########################################3
    #Define the variables to load
    label.time        =nc_v.variables['time']   
    label.x           =nc_v.variables['x']   
    label.y           =nc_v.variables['y']   

    label.Prec        =nc_v.variables['Prec']   
    label.LWNS        =nc_v.variables['LWNS']      
    label.LWNSC       =nc_v.variables['LWNS']      
    label.LWNT        =nc_v.variables['LWNT']      
    label.LWNTC       =nc_v.variables['LWNT']      
    label.SOLIN       =nc_v.variables['SOLIN']      
    label.SWNS        =nc_v.variables['SWNS']      
    label.SWNSC       =nc_v.variables['SWNS']      
    label.SWNT        =nc_v.variables['SWNT']      
    label.SWNTC       =nc_v.variables['SWNT']      
    label.CWP         =nc_v.variables['CWP']       
    label.IWP         =nc_v.variables['IWP']       
    label.CLD         =nc_v.variables['CLD']       
    label.PW          =nc_v.variables['PW']        
    label.USFC        =nc_v.variables['USFC']      
    label.U200        =nc_v.variables['U200']      
    label.VSFC        =nc_v.variables['VSFC']      
    label.V200        =nc_v.variables['V200']      
    label.W500        =nc_v.variables['W500']      
    label.PSFC        =nc_v.variables['PSFC']      
    label.SWVP        =nc_v.variables['SWVP']      
    label.U850        =nc_v.variables['U850']      
    label.V850        =nc_v.variables['V850']      
    label.ZC          =nc_v.variables['ZC']        
    label.TB          =nc_v.variables['TB']        
    label.ZE          =nc_v.variables['ZE']        
    label.CLDC        =nc_v.variables['CLDC']      

    ########################################3
    
    tu = calendar[0] 
    tc = calendar[1]

    label.date       = num2pydate(label.time[:],units=tu,calendar=tc)

    return label 

##Prec               20 Surface Precip. Rate    255.32426   0.00000
## LWNS              21 Net LW at the surface    39.224770 11.300159
## LWNSC             31 Net clear-sky LW at the surface    39.436462 24.257160
## LWNT              13 Net LW at TOA    346.76587 326.86862
## LWNTC             23 Clear-Sky Net LW at TOA    176.36771 168.51413
## SOLIN             20 Solar TOA insolation    0.0000000 0.0000000
## SWNS              21 Net SW at the surface    0.0000000 0.0000000
## SWNSC             31 Net Clear-sky SW at the surface    0.0000000 0.0000000
## SWNT              13 Net SW at TOA    0.0000000 0.0000000
## SWNTC             23 Net Clear-Sky SW at TOA    0.0000000 0.0000000
## CWP               16 Cloud Water Path    0.7809817 0.0000000
## IWP                8 Ice Path    0.0060257 0.0000000
## CLD               15 Cloud Frequency    57.361115  0.000000
## PW                18 Precipitable Water    57.507172 53.500282
## USFC              16 U at the surface    0.6862376-5.1848230
## U200              11 U at 200 mb   -7.7026172-7.7806983
## VSFC              16 V at the surface    3.3196933-4.1342850
## V200              11 V at 200 mb   -0.1940548-0.2601828
## W500              11 W at 500 mb    0.1766707-0.1972506
## PSFC              16 P at the surface    1037.2216 1037.0914
## SWVP              26 Saturated Water Vapor Path    77.896080 76.993217
## U850              23 850 mbar zonal velocity   -5.4774113-7.0074725
## V850              28 850 mbar meridional velocity   -1.1510472-2.6474226
## ZC                32 Cloud top height (Instantaneous)    5.1750002 0.0000000
## TB                37 Cloud top temperature (Instantaneous)    297.89810 270.47180
## ZE                31 Echo top height (Instantaneous)    4.6750002 0.0000000
## CLDC              27 Cloud cover (Instantaneous)    1.0000000 0.0000000

