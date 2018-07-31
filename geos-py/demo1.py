# -*- coding: utf-8 -*-
from django.contrib.gis.geos import GEOSGeometry, Point, LineString, fromfile, Polygon


"""生成数据，点、线、面"""
def createData():
    pnt = GEOSGeometry('POINT(5 23)') 
    pnt2 = GEOSGeometry('{ "type": "Point", "coordinates": [ 5.000000, 23.000000 ] }') # GeoJSON
    pnt3 = Point(-2, 5)
    poly = Polygon( ((0.0, 0.0), (0.0, 50.0), (50.0, 50.0), (50.0, 0.0), (0.0, 0.0)) )   
    print(pnt2.geojson)
    line = LineString((-1, 0), (1, 1), srid=4326)        # 创建了线类型并定义了坐标系
    return pnt, pnt3, line, poly
#layer = fromfile('Data/region.shp')    
#print(layer)


"""空间关系分析，包含、相离、相交等等"""    
def GeoRelat():      
   
    print(poly.geom_type)       # 输出要素的类型
    
    contain = poly.contains(pnt3)       # 判断是否包含其他要素
    print(contain)
    
    disjoin = line.disjoint(pnt)        # 判断两个要素是否相离
    print(disjoin)
    
    cross = poly.crosses(line)
    print(cross)

"""获取要素的信息：线段长度、多边形的面积以及两个要素的距离"""
def GeomInfo():
    print(line.length)
    print(poly.area)
    print(line.distance(pnt))


"""空间分析：缓冲区分析、相交分析等等"""
def GeoProcess():    
    pointBuffer = pnt.buffer(10)
    print(pointBuffer)



if __name__ == "__main__":       
    pnt, pnt3, line, poly = createData()
    # 输出点的坐标
    for coord in pnt:
        print(coord)
    
    GeoProcess()        
    
