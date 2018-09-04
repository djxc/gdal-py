# -*- encoding: utf-8 -*-
import gdal
import os

os.chdir('F:\GISData')
in_ds = gdal.Open('test1.tif')
num_band = in_ds.RasterCount    # 获取波段数
print(num_band)
in_band = in_ds.GetRasterBand(1)
xSize = in_band.XSize   # 获取行数
ySize = in_band.YSize   # 获取列数
print(xSize, ySize)
print(in_ds.GetProjection())
in_data = in_band.ReadAsArray()     # 将波段数据读取为矩阵
print(in_data)
# gtiff_driver = gdal.GetDriverByName('GTiff')
# ds = gtiff_driver.Create('test.tiff', 100, 100, 3)

