# ----------------------------------------------------------------------------
# -*- coding: utf-8 -*-
# @Author:              Gifty Attiah
# @Date:                2020-12-21
# @Email:               geattiah@gmail.com
# @Last Modified By:    Gifty Attiah
# @Last Modified Time:  Not Tracked
# 
# PROGRAM DESCRIPTION:
# Mosaic Modis Data within a folder
# ----------------------------------------------------------------------------

import os
import fnmatch
from osgeo import gdal

rootdir_12 =  r"C:/Users/ReSEC2021/Downloads/2003"
rootdir_13 =  r"C:/Users/ReSEC2021/Downloads/Data/2003"

allSubDirs = os.listdir(rootdir_12)
allSubDirs1 = os.listdir(rootdir_13)

for dirs in allSubDirs:
    folder = os.path.join(rootdir_12,dirs)
    for file in os.listdir(folder):
        sec = file[-12:]
        for dir1 in allSubDirs1:
            folder1 = os.path.join(rootdir_13,dir1)
            for file1 in os.listdir(folder1):
                #print(file2)
                if fnmatch.fnmatch(file1, '*' + str(sec)):
                    h12 =  os.path.join(folder,file)
                    h13 =  os.path.join(folder1,file1)
                    print(h12)
                    print(h13)
                    outfolder= r"C:/Users/ReSEC2021/Downloads/Data/Join"
                    my_vrt = gdal.BuildVRT(os.path.join(outfolder,"MODIS_LST_h12_13v02_" + sec), [h12, h13])

        #print(files)

