import os
import fnmatch
import gdal
import subprocess
#from osgeo import gdal

def mosaic(year):
    storage = r"C:\Users\ReSEC2021\Downloads\lab 3"
    rootdir_11 =  fr"C:\Users\ReSEC2021\Downloads\{year}"
    rootdir_12 =  fr"C:\Users\ReSEC2021\Downloads\lab 3\{year}" 

    for dirs in os.listdir(rootdir_11):
        folder = os.path.join(rootdir_11,dirs)
        for files in os.listdir(folder):
            modis_file_11 = os.path.join(folder,files)
            sec = modis_file_11[-12:]
            for dirs1 in os.listdir(rootdir_12):
                folder1 = os.path.join(rootdir_12,dirs1)
                for files1 in os.listdir(folder1):
                    if fnmatch.fnmatch(files1, '*' + str(sec)):
                        h11 =  os.path.join(folder,files)
                        print(h11)
                        h12 =  os.path.join(folder1,files1)
                        print(h12)
                        month = os.path.join(storage,folder)
                        output= os.path.join(month,"MODIS_LST_h12v02_" +sec)
                        gdal.AllRegister()
                        subprocess.call(['gdal_merge.py', '-o' , output, h11, h12])

                        #my_vrt = gdal.BuildVRT(output, [h11, h12])



        
        # store = os.path.join(os.path.dirname(storage),'MYD11_h12')
        # if not os.path.exists(store):
        #     os.mkdir(store)
        # store1 = os.path.join(os.path.join(store),os.path.basename(rootdir_12))
        # if not os.path.exists(store1):
        #     os.mkdir(store1)
        # store2 = os.path.join(os.path.join(store1),os.path.basename(folder))
        # if not os.path.exists(store2):
        #     os.mkdir(store2)
        # for file in os.listdir(folder):
        #     sec = file[-12:]
        #     for dir1 in allSubDirs1:
        #         folder1 = os.path.join(rootdir_13,dir1)
        #         for file1 in os.listdir(folder1):
        #             #print(file2)
        #             if fnmatch.fnmatch(file1, '*' + str(sec)):
        #                 h12 =  os.path.join(folder,file)
        #                 h13 =  os.path.join(folder1,file1)
        #                 #print(h12)
        #                 #print(h13)
        #                 #outfolder= r"C:/Users/ReSEC2021/Downloads/Data/Join"
        #                 my_vrt = gdal.BuildVRT(os.path.join(store2,"MODIS_LST_h12_13v02_" + sec), [h12, h13])

        #     #print(files)
mosaic(2003)


    
