# -*- encoding: utf-8 -*-
from osgeo import ogr
from ospybook.vectorplotter import VectorPlotter


def get_city():
    sd = ogr.Open(r'G:\arcgis data\argis数据\12月16日数据\城市.shp')
    provence = sd.GetLayer(0)
    provence.SetAttributeFilter('area>16000')
    city = provence.GetNextFeature()
    city_geo = city.geometry().Clone()
    print(city.GetField('long'))
    vp.plot(city_geo, 'b')
    vp.draw()
    return city_geo


def get_intersect():
    highway = ogr.Open(r'G:\arcgis data\argis数据\12月16日数据\test_intersect.shp')
    way = highway.GetLayer(0)
    wayfeature = way.GetNextFeature()
    waygeo = wayfeature.geometry().Clone()
    vp.plot(waygeo, 'g')
    vp.draw()
    return waygeo


if __name__ == '__main__':
    """
    1.通过两个图层获取两个要素
    2.通过要素的geometry().Clone()方法获取几何对象
    3.进行相交，获取相交后的几何对象"""
    vp = VectorPlotter(False)
    citygeo = get_city()
    highgeo = get_intersect()
    insect = citygeo.Intersection(highgeo)
    vp.plot(insect, 'yellow')
    vp.draw()