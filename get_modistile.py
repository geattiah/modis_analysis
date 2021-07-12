# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# @Author:              Gifty Attiah
# @Date:                2021-05-24
# @Email:               geattiah@gmail.com
# @Last Modified By:    Gifty Attiah
# @Last Modified Time:  Not Tracked
# 
# PROGRAM DESCRIPTION:
# Get modis tile based on location
# ----------------------------------------------------------------------------

import numpy as np

filename = r"C:\Users\ReSEC2021\Dropbox\Python\array\sn_bound_10deg.txt"
#wget --no-check-certificate "https://modis-land.gsfc.nasa.gov/pdf/sn_bound_10deg.txt"

# first seven rows contain header information
# bottom 3 rows are not data
data = np.genfromtxt(filename, 
                     skip_header = 7, 
                     skip_footer = 3)
lat = 70.87
lon = 29.27



in_tile = False
i = 0
while(not in_tile):
    in_tile = lat >= data[i, 4] and lat <= data[i, 5] and lon >= data[i, 2] and lon <= data[i, 3]
    i += 1

vert = data[i-1, 0]
horiz = data[i-1, 1]
print('Vertical Tile:', vert, 'Horizontal Tile:', horiz)