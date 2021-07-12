from osgeo import gdal

file_13 = r"C:/Users/ReSEC2021/Downloads/MODIS_LST_h13v02_20030101.hdf"
file_12 = r"C:/Users/ReSEC2021/Downloads/MODIS_LST_h12v02_20030101.hdf"
out = r"C:/Users/ReSEC2021/Downloads/out_LST_al.hdf"
#vrt_options = gdal.BuildVRTOptions(resampleAlg='nearest', addAlpha=True)
my_vrt = gdal.BuildVRT(out, [file_12, file_13]) #options=vrt_options)
#my_vrt = None