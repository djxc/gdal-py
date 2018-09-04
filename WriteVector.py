# -*- coding: utf-8 -*-
import sys
from osgeo import ogr

ds = ogr.Open(r'F:\test', 1)    # 打开数据源，以文件夹为数据源
if ds is None:
    sys.exit('Could not open folder')
in_lyr = ds.GetLayer(r'myshp')
if ds.GetLayer('new_lyr'):
    ds.DeleteLayer('new_lyr')
out_layr = ds.CreateLayer('new_lyr', in_lyr.GetSpatialRef(), ogr.wkbPolygon)    # 创建新图层指定空间参考与几何数据类型
out_layr.CreateFields(in_lyr.schema)    # 给图层配置属性表的结构

out_defn = out_layr.GetLayerDefn()
out_feat = ogr.Feature(out_defn)    # 创建空间要素
for in_feat in in_lyr:  # 将就图层中的空间要素赋值给新的空间要素
    geom = in_feat.geometry()
    out_feat.SetGeometry(geom)
    for i in range(in_feat.GetFieldCount()):
        value = in_feat.GetField(i)
        out_feat.SetField(i, value)
    out_layr.CreateFeature(out_feat)
del ds
