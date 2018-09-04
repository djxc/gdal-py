# -*- coding: utf-8 -*-
from osgeo import ogr
import os
import sys
import codecs


# 输出数据源中所有的图层名称
def print_layers(fn):
    ds = ogr.Open(fn)
    if ds is None:
        raise OSError('Could not open {0}.'.format(fn))
    for i in range(ds.GetLayerCount()):
        lyr = ds.GetLayer(i)
        print('{0}:{1}'.format(i, lyr.GetName()))
    del ds


def layer_to_feature_dataset(ds_name, gdb_fn, dataset_name):
    """
    将图层复制到地理数据库中，提供参数为：要导入数据库名称，地理数据库，地理数据集名称
    1.获取要输入的图层的数据源
    2.使用驱动创建打开或者创建地理数据库
    3.遍历输入图层，使用CopyLayer方法进行导入
    :param ds_name: 
    :param gdb_fn: 
    :param dataset_name: 
    :return: 
    """
    in_ds = ogr.Open(ds_name)
    if in_ds is None:
        raise OSError('Could not open {0}.'.format(ds_name))

    gdb_driver = ogr.GetDriverByName('OpenFileGDB')
    if gdb_driver is None:
        raise OSError('Could not get driver')
    if os.path.exists(gdb_fn):
        gdb_ds = gdb_driver.Open(gdb_fn)
    else:
        gdb_ds = gdb_driver.CreateDataSource(gdb_fn)
    if gdb_ds is None:
        raise OSError('Could not open geodatabase')

    options = ['FEATURE_DATASET=', dataset_name]
    for i in range(in_ds.GetLayerCount()):
        lyr = in_ds.GetLayer(i)
        lyr_name = lyr.GetName()
        print('Copy '+ lyr_name+'...')
        gdb_ds.CopyLayer(lyr, lyr_name, options)


def print_attributes(lyr_or_fn, n=None, fields=None, geom=True, reset=True):
    """Print attribute values in a layer.

    lyr_or_fn - OGR layer object or filename to datasource (will use 1st layer)
    n         - optional number of features to print; default is all
    fields    - optional list of case-sensitive field names to print; default
                is all
    geom      - optional boolean flag denoting whether geometry type is printed;
                default is True
    reset     - optional boolean flag denoting whether the layer should be reset
              - to the first record before printing; default is True
    """
    lyr, ds = _get_layer(lyr_or_fn)
    if reset:
        lyr.ResetReading()

    n = n or lyr.GetFeatureCount()
    geom = geom and lyr.GetGeomType() != ogr.wkbNone
    fields = fields or [field.name for field in lyr.schema]
    data = [['FID'] + fields]
    if geom:
        data[0].insert(1, 'Geometry')
    feat = lyr.GetNextFeature()
    while feat and len(data) <= n:
        data.append(_get_atts(feat, fields, geom))
        feat = lyr.GetNextFeature()
    lens = map(lambda i: max(map(lambda j: len(str(j)), i)), zip(*data))
    format_str = ''.join(map(lambda x: '{{:<{}}}'.format(x + 4), lens))
    for row in data:
        try:
            print(format_str.format(*row))
        except UnicodeEncodeError:
            e = sys.stdout.encoding
            print(codecs.decode(format_str.format(*row).encode(e, 'replace'), e))
    print('{0} of {1} features'.format(min(n, lyr.GetFeatureCount()), lyr.GetFeatureCount()))
    if reset:
        lyr.ResetReading()


def _get_layer(lyr_or_fn):
    """Get the datasource and layer from a filename."""
    if type(lyr_or_fn) is str:
        ds = ogr.Open(lyr_or_fn)
        if ds is None:
            raise OSError('Could not open {0}.'.format(lyr_or_fn))
        return ds.GetLayer(), ds
    else:
        return lyr_or_fn, None


def _get_atts(feature, fields, geom):
    """Get attribute values from a feature."""
    data = [feature.GetFID()]
    geometry = feature.geometry()
    if geom and geometry:
        data.append(_geom_str(geometry))
    values = feature.items()
    data += [values[field] for field in fields]
    return data


def _geom_str(geom):
    """Get a geometry string for printing attributes."""
    if geom.GetGeometryType() == ogr.wkbPoint:
        return 'POINT ({:.3f}, {:.3f})'.format(geom.GetX(), geom.GetY())
    else:
        return geom.GetGeometryName()