# -*- coding: utf-8 -*-
"""
Created on Sun May 24 23:28:21 2020

@author: HP
"""

import xarray as xr
import numpy as np
import pymannkendall as pmk
in_file='cru_ts4.03.1901.2018.tmp.dat.nc'

Data=xr.open_dataset(in_file)
Data_2_use=Data['tmp']

#Single Line Selection
SLS=Data_2_use.sel(lon=0.5, lat=7.5, method='nearest')
SLS.plot()

#Areal Selection & Averaging
ASA=Data_2_use.sel(lon=np.arange(-1.5,1.5,0.5),lat=np.arange(5,15,0.5),method='nearest')
ASA=ASA.mean(dim=('lon','lat'))
ASA.plot()

#Annual Averaging
Ann_avg=ASA.groupby('time.year').mean('time')
Ann_avg.plot()

### Statistics of Data
stat_result=pmk.original_test(Ann_avg)
print(stat_result)


#Seasonal Climatology
Seas_avg=ASA.groupby('time.season').mean('time')
print(Seas_avg)

#THANK YOU
































#Reading Data from NetCDF File
Data=xr.open_dataset(in_file)
Data_2_use=Data['tmp']

#Selecting location 0.5W, 6.5N
loc_data=Data_2_use.sel(lon=-0.5, lat=6.5, method='nearest')
loc_data.plot()

#Average over an area
spat_avg=Data_2_use.sel(lon=np.arange(-1.5,1.5,0.5),lat=np.arange(5,7.5,0.5), method='nearest')
spat_avg.mean(dim=('lon','lat')).plot()

#Annual Averaging
Ann_avg=spat_avg.groupby('time.year').mean('time')
Ann_avg=Ann_avg.mean(dim=('lon','lat'))
Ann_avg.plot()

#Seasonal Averaging 
Seas_avg=spat_avg.groupby('time.season').mean('time')
Seas_avg.mean(dim=('lon','lat'))

import pymannkendall as pmk
result = pmk.original_test(Ann_avg)