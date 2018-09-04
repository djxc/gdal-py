# -*- encoding: utf-8 -*-
import myTool

# myTool.print_layers(r'G:\arcgis data\AA.gdb')
# myTool.layer_to_feature_dataset(r'F:\GISData\全国·市县级shp文件', r'F:\GISData\dj.mdb', 'test')
# url = 'WFS:http://gis.srh.noaa.gov/arcgis/services/watchWarn/MapServer/WFSServer'
# url = 'https://services.arcgis.com/V6ZHFr6zdgNZuVG0/ArcGIS/rest/services/CensusLaborDemo/FeatureServer'
url = 'https://sampleserver6.arcgisonline.com/arcgis/rest/services/Census/MapServer/'
myTool.print_layers(url)
