# -*- coding: utf-8 -*-
import sys
from osgeo import ogr

fn = r'F:\test\point.shp'
ds = ogr.Open(fn, 0)    # 通过打开文件获取datasource
if ds is None:
    sys.exit('Could not open {0}.'.format(fn))
lyr = ds.GetLayer(0)    # 通过datasource获取图层
num_feat = lyr.GetFeatureCount()    # 获取图层中要素个数
print(num_feat)
i = 0
for feat in lyr:    # 遍历图层获取地理要素
    pt = feat.geometry()    # 获取几何对象
    x = pt.GetX()   # 通过几何对象获取x，y坐标
    y = pt.GetY()
    name = feat.GetField('Id')  # 访问属性
    print(name, x, y)
    i += 1
    if i == 10:
        break
del ds  # 删除datasource释放内存
