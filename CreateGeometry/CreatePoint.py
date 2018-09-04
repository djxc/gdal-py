# -*- encoding: utf-8 -*-
from osgeo import ogr
from ospybook.vectorplotter import VectorPlotter


class CreatePoint(object):
    def __init__(self, name, type):
        self.name = name    # 名称
        self.type = type  # 几何类型如：POLYLINE, POINT, MULTIPOINT, POLYGON
        self.geo_type = None

    def create_point(self):
        """
        创建单点要素，并返回改要素
        :return: 
        """
        self.get_type()
        firepit = ogr.Geometry(self.geo_type)
        firepit.AddPoint(59.5, 11.5)
        print(firepit)
        print(firepit.GetX())   # 获取点的x坐标值
        return firepit

    def create_points(self):
        """
        创建多点要素，返回改要素
        :return: 
        """
        firepit = ogr.Geometry(ogr.wkbMultiPoint)
        pit = ogr.Geometry(ogr.wkbPoint)
        pit.AddPoint(59.5, 11.5)
        firepit.AddGeometry(pit)
        pit.AddPoint(60, 13.5)
        firepit.AddGeometry(pit)
        pit.AddPoint(59.5, 13.5)
        firepit.AddGeometry(pit)
        return firepit

    def get_type(self):
        """
        转换几何数据类型
        :return: 
        """
        if self.type == "point":
            self.geo_type = ogr.wkbPoint
        elif self.type == "points":
            self.geo_type = ogr.wkbMultiPoint
        elif self.type == "line":
            self.geo_type = ogr.wkbLineString
        elif self.type == "lines":
            self.geo_type = ogr.wkbMultiLineString
        elif self.type == "polygon":
            self.geo_type = ogr.wkbPolygon
        elif self.type == "ring":
            self.geo_type = ogr.wkbLinearRing

    def show_point(self, point):
        vp = VectorPlotter(False)
        vp.plot(point, 'bo')
        vp.draw()

    def change_point(self, points):
        """
        传入一个点要素，修改点要素的坐标值
        :param points: 
        :return: 
        """
        for i in range(points.GetGeometryCount()):
            p = points.GetGeometryRef(i)
            p.AddPoint(p.GetX() + 10, p.GetY())

