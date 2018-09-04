# -*- encoding: utf-8 -*-
import codecs
import sys

from osgeo import ogr
from ospybook.vectorplotter import VectorPlotter

import myTool

reload(sys)
sys.setdefaultencoding('utf8')
print sys.getdefaultencoding() + "  - sys.getdefaultencoding()"
print sys.stdout.encoding + " - sys.stdout.encoding:"
sys.stdout = codecs.getwriter('utf8')(sys.stdout)    # 影响print
print sys.stdout.encoding + " - sys.stdout.encoding:"


def show_data(lyr):
    """
    显示数据，提供图层参数
    :param lyr: 
    :return: 
    """
    vp = VectorPlotter(False)
    vp.plot(lyr, 'bo')
    vp.draw()


def get_field(lyr):
    for feature in lyr:    # 遍历图层获取地理要素
        name = feature.GetField('FieldName')  # 访问属性
        print(name)


def attribute_filter(lyr, field_name, field_value):
    """
    属性过滤，需要的变量为1.进行过滤的图层 2.进行过滤字段名称 3.过滤条件字段值
    :return: 
    """
    lyr.SetAttributeFilter(field_name + ' = ' + field_value)  # 对图层设置属性过滤器
    print(polygon_lyr.GetFeatureCount())  # 获取图层中要素的个数


def spatial_filter(lyr, feature):
    """空间过滤器，用户需要提供要进行过滤的图层以及过滤需要的几何对象
    可以通过要素获取几何对象
    """
    geometry = feature.geometry().Clone()
    print(lyr.GetFeatureCount())
    lyr.SetSpatialFilter(geometry)
    print(lyr.GetFeatureCount())


def test_sql(datasource, SQL):
    """
    使用sql语句进行查询，通过数据源进行执行语句，返回一个图层
    :param ds: 数据源
    :param sql: 查询语句
    :return: 图层
    """
    lyr = datasource.ExecuteSQL(SQL)
    return lyr


if __name__ == '__main__':
    ds = ogr.Open(r'F:\test')
    sql = '''SELECT FieldID, FieldName FROM "new_lyr" ORDER BY FieldID DESC '''
    lyr = test_sql(ds, sql)
    myTool.print_attributes(lyr, 3)
    polygon_lyr = ds.GetLayer('new_lyr')
    point_lyr = ds.GetLayer('point')
    print(polygon_lyr.GetName())
    # get_field()
    myTool.print_attributes(polygon_lyr, 3, ['FieldName'], False)
    attribute_filter(polygon_lyr, 'FieldID', '5')
    feat = polygon_lyr.GetNextFeature()
    spatial_filter(point_lyr, feat)
    show_data(point_lyr)
    del ds
