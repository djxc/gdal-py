# -*- encoding: utf-8 -*-
from osgeo import ogr
from ospybook.vectorplotter import VectorPlotter


class CreateLine(object):

    def create_line(self):
        """
        创建线要素，并返回改要素
        :return: 
        """
        line = ogr.Geometry(ogr.wkbLineString)
        line.AddPoint(59.5, 11.5)
        line.AddPoint(69.5, 11.5)
        line.AddPoint(69.5, 21.5)
        line.AddPoint(75.5, 18.5)
        line.AddPoint(78.5, 15.5)
        return line

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

    def show_line(self, line):
        vp = VectorPlotter(False)
        vp.plot(line, 'b-')
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