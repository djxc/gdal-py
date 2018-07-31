# -*- coding: utf-8 -*-
from osgeo import ogr

"""遍历图层中所有的要素，然后获取要素的几何以及属性信息"""
def IteratorFeature(layer):
    i = 0
    for feat in layer:
#        pt=feat.geometry()
#        x=pt.GetX()
#        y=pt.GetY()
        x = feat.GetField('X')
        y = feat.GetField('Y')
        name = feat.GetField('NAME')
        print(x, y, name)
        i += 1
        if i==10:
            break


"""获取图层指定的属性信息
    1.给定一个图层
    2.给出要获取属性信息的属性名称
"""
def printAttribute(layer, fields):
    attTable = []
    for feat in layer:
        atts = []
        for field in fields:
            att = feat.GetField(field)
            atts.append(att)
        print(atts)
        attTable.append(atts)
#    print(attTable)        
            
        
        
"""获取图层的元数据信息，包括范围、图层类型、空间坐标系"""        
def getLayerMetData(layer):
    extent = layer.GetExtent()
    print(extent)
    geomType = layer.GetGeomType()
    if geomType == ogr.wkbPolygon:
        print('polygon')
    if geomType == ogr.wkbPoint:
        print('point')
    if geomType == ogr.wkbLineString:
        print('line')
    print(layer.GetSpatialRef())