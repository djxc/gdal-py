# -*- coding: utf-8 -*-
from django.contrib.gis.gdal import DataSource

def DsInfo():
    print(ds.name)
    print(ds.layer_count)                  # This file only contains one layer
     
     
"""获取图层的要素个数、属性个数、空间范围、空间参考"""     
def layerInfo():
    print(layer.num_feat)       # 获取图层的要素的数量
    print(layer.num_fields)     # 获取图层属性个数
    print(layer.fields)
    
    envelope = layer.extent     # 获取图层范围，最小外包矩形
    print(envelope)
    
    print(layer.srs)            # 获取图层的空间参考信息

    name = layer.get_fields('NAME')
    print(name)

#    for f in layer.get_geoms():
#        print(f)
        

"""获取要素的信息：图层由要素组成的。直接从图层获取要素，然后可以根据要素获取属性，几何等等"""    
def featInfo():
    feat = layer[1]   
    name = feat.get('NAME')
    print(name)
    print(feat.geom_type)
    

def fieldInfo():
    field = layer[1]['NAME']    
    print(field.name)
    print(field.value)
    print(field.type_name)
    
    
if __name__ == "__main__":    
    ds = DataSource('../Data/region.shp')
    layer = ds[0]           # 获取数据源里的第一个图层
#    featInfo()
    fieldInfo()