# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 22:49:04 2020

@author: HP
SPATIAL DIAGRAMS

conda install -c scitools cartopy
"""

import xarray as xr
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import cartopy.crs as ccrs
from cartopy import feature as cf
from cartopy.mpl.gridliner import LONGITUDE_FORMATTER, LATITUDE_FORMATTER


in_file='cru_ts4.03.1901.2018.tmp.dat.nc'

Data=xr.open_dataset(in_file)
Data_2_use=Data['tmp']
NHA=Data_2_use.sel(lon=np.arange(-25,50,0.5),lat=np.arange(0,40,0.5),method='nearest')


Seas_NHA=NHA.groupby('time.season').mean('time')

#Seas_NHA.plot.contourf(x='lon',y='lat',col='season', col_wrap=2)

count=0
fig=plt.figure(figsize=(11,7))
for seas in Seas_NHA.season:
    count+=1
    ax=fig.add_subplot(2,2,count,projection=ccrs.PlateCarree())
    Seas_NHA[Seas_NHA.season==seas].plot(vmin=-20, vmax=30)
    
    ax.coastlines(resolution='110m')
    ax.add_feature(cf.BORDERS)
    ax.set_extent([-25.25, 50.25, -0.25, 25.75])
    
    gl=ax.gridlines()
    gl.xlabels_bottom=True; gl.ylabels_left=True
    gl.xformatter=LONGITUDE_FORMATTER
    gl.yformatter=LATITUDE_FORMATTER



    
    