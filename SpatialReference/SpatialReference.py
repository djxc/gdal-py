# -*- encoding: utf-8 -*-
from osgeo import ogr

ds = ogr.Open(r'F:\GISData\全国·市县级shp文件\安徽省市域shp文件.shp')
print(ds.GetLayer().GetSpatialRef())
