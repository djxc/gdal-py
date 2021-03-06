# -*- encoding: utf-8 -*-
from osgeo import ogr
from ospybook.vectorplotter import VectorPlotter


class CreatePolygon(object):

    def create_polygon(self):
        """
        创建多边形要素，并返回改要素
        :return: 
        """
        ring = ogr.Geometry(ogr.wkbLinearRing)
        ring.AddPoint(59.5, 11.5)
        ring.AddPoint(69.5, 11.5)
        ring.AddPoint(69.5, 21.5)
        ring.AddPoint(59.5, 11.5)
        polygon = ogr.Geometry(ogr.wkbPolygon)
        polygon.AddGeometry(ring)
        polygon.CloseRings()
        return polygon

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

    def show_polygon(self, polygon):
        vp = VectorPlotter(False)
        vp.plot(polygon, fill=False, edgecolor='blue')
        vp.draw()

