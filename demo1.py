# -*- coding: utf-8 -*-
import sys
from osgeo import ogr
import myLayer

"""打开矢量数据，打开失败直接退出程序。打开成功，返回一个dataset"""
def openData(path):
    ds = ogr.Open(path, 0)
    if ds is None:
        sys.exit('Could not open {0}'.format(path))
    return ds


def createGeojson():
    dirver = ogr.GetDriverByName('geojson')     # 获取数据格式的驱动
    print(dirver.name)
    fn = 'data/test2.geojson'
    jsonDs = dirver.CreateDataSource(fn)
    if jsonDs is None:
        sys.exit('Could not create {0}.'.format(fn))
    jsonLayer = jsonDs.CreateLayer('dj', lyr.GetSpatialRef(), ogr.wkbPoint)
    
    name_fld = ogr.FieldDefn('Name', ogr.OFTString)
    name_fld.SetWidth(6)
    jsonLayer.CreateField(name_fld)
    
    coord_fld = ogr.FieldDefn('x', ogr.OFTReal)
    coord_fld.SetWidth(6)
    coord_fld.SetPrecision(3)
    jsonLayer.CreateField(coord_fld)
    
    coord_fld.SetName('y')
    jsonLayer.CreateField(coord_fld)
    
    out_feat = ogr.Feature(jsonLayer.GetLayerDefn())
    for i in range(100):
        out_feat.SetField('Name', str(i))
        out_feat.SetField('x', i*10)
        out_feat.SetFiels('y', i*10+2)
        jsonLayer.CreateFeature(out_feat)


def createShp(lyr):
    ds = ogr.Open('data')
    if ds is None:
        sys.exit('Could not open floder')
#    dirver = ogr.GetDriverByName('ESRI ShapeFile')     # 获取数据格式的驱动
#    print(dirver.name)
#    fn = 'data/test1.shp'
#    jsonDs = dirver.CreateDataSource(fn)
#    if jsonDs is None:
#        sys.exit('Could not create {0}.'.format(fn))
    jsonLayer = ds.CreateLayer('dj', lyr.GetSpatialRef(), ogr.wkbPoint)
    
    name_fld = ogr.FieldDefn('Name', ogr.OFTString)
    name_fld.SetWidth(6)
    jsonLayer.CreateField(name_fld)
    
    coord_fld = ogr.FieldDefn('x', ogr.OFTReal)
    coord_fld.SetWidth(6)
    coord_fld.SetPrecision(3)
    jsonLayer.CreateField(coord_fld)
    
    coord_fld.SetName('y')
    jsonLayer.CreateField(coord_fld)
    
    out_feat = ogr.Feature(jsonLayer.GetLayerDefn())
    for i in range(100):
        out_feat.SetField('Name', str(i))
        out_feat.SetField('x', i*10)
        out_feat.SetFiels('y', i*10+2)
        jsonLayer.CreateFeature(out_feat)


if __name__ == "__main__":    
    ds = openData('../Data/region.shp')
    lyr=ds.GetLayer(0)      # 从dataset中获取图层
    featNum = lyr.GetFeatureCount()         # 获得图层要素的个数
    print(featNum)
#    IteratorFeature(lyr)
#    printAttribute(lyr, ['NAME', 'ID'])   
#    myLayer.getLayerMetData(lyr)
    del ds      # 程序运行最后注销dataset
    createShp(lyr)
    
   
    
    