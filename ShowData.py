# -*- encoding: utf-8 -*-
from osgeo import ogr

from CreateGeometry import CreatePoint, CreateLine, CreatePolygon


# os.chdir(r'F:\test')
# vp = VectorPlotter(False)
# vp.plot('point.shp', 'bo')
# vp.draw()
def about_point():
    point = CreatePoint.CreatePoint("point", "point")
    points = point.create_points()
    point.show_point(points)
    point.change_point(points)
    point.show_point(points)
    print(points)

def about_line():
    line = CreateLine.CreateLine()
    li = line.create_line()
    line.show_line(li)
    vertices = li.GetPoints()
    for v in vertices:
        print(v)


def create_line():
    line = ogr.Geometry(ogr.wkbLineString)
    points = [(12, 20), (15, 22), (18, 18)]
    for point in points:
        line.AddPoint(*point)   # *操作符可以将元组展开为独立的参数
    print(line)


def about_polygon():
    polygon = CreatePolygon.CreatePolygon()
    po = polygon.create_polygon()
    polygon.show_polygon(po)


if __name__ == '__main__':
    # about_line()
    # create_line()
    about_polygon()