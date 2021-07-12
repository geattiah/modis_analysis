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



    


# for subdir, dirs, files in os.walk(rootdir_12):
#     for folder in dirs:
#         direc = os.path.join(dirs,folder)
#         for files in os.listdir(direc):
#         #if fnmatch.fnmatch(file_12, '[20031119]'):
#             print(files)
        #print(os.path.join(subdir, file_12))
        # for subdir, dirs, files in os.walk(rootdir_13):
        #     for file_13 in files:  
        #         if fnmatch.fnmatch(file_13, '[20031119]'):
        #             print(file)

                #print(os.path.join(subdir, file_13))

#for i in 
#file_13 = r"C:/Users/ReSEC2021/Downloads/MODIS_LST_h13v02_20030101.hdf"
#file_12 = r"C:/Users/ReSEC2021/Downloads/MODIS_LST_h12v02_20030101.hdf"
#out = r"C:/Users/ReSEC2021/Downloads/out_LST_al.hdf"
#vrt_options = gdal.BuildVRTOptions(resampleAlg='nearest', addAlpha=True)
#my_vrt = gdal.BuildVRT(out, [file_12, file_13]) #options=vrt_options)
#my_vrt = N