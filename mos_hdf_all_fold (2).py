# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# @Author:              Gifty Attiah
# @Date:                2021-06-07
# @Email:               geattiah@gmail.com
# @Last Modified By:    Gifty Attiah
# @Last Modified Time:  Not Tracked
# 
# PROGRAM DESCRIPTION:
# Run through MODIS folders and merge those of similar dates
# ----------------------------------------------------------------------------

import os
import fnmatch
from osgeo import gdal
#import gdal

rootdir_12 =  "/home/kheyro/rootdir/data/satellite/daily/MYD11/2003"
rootdir_13 =  "/home/kheyro/rootdir/data/satellite/daily/MYD11_13/2003"
storage = "/home/kheyro/rootdir/data/satellite/daily/MYD11"


allSubDirs = os.listdir(rootdir_12)
allSubDirs1 = os.listdir(rootdir_13)

for dirs in allSubDirs:
    folder = os.path.join(rootdir_12,dirs)
    store = os.path.join(os.path.dirname(storage),'MYD11_h12_13')
    if not os.path.exists(store):
        os.mkdir(store)
    store1 = os.path.join(os.path.join(store),os.path.basename(rootdir_12))
    if not os.path.exists(store1):
        os.mkdir(store1)
    store2 = os.path.join(os.path.join(store1),os.path.basename(folder))
    if not os.path.exists(store2):
        os.mkdir(store2)
    for file in os.listdir(folder):
        sec = file[-12:]
        for dir1 in allSubDirs1:
            folder1 = os.path.join(rootdir_13,dir1)
            for file1 in os.listdir(folder1):
                #print(file2)
                if fnmatch.fnmatch(file1, '*' + str(sec)):
                    h12 =  os.path.join(folder,file)
                    h13 =  os.path.join(folder1,file1)
                    #print(h12)
                    #print(h13)
                    #outfolder= r"C:/Users/ReSEC2021/Downloads/Data/Join"
                    my_vrt = gdal.BuildVRT(os.path.join(store2,"MODIS_LST_h12_13v02_" + sec), [h12, h13])

        #print(files)



    
