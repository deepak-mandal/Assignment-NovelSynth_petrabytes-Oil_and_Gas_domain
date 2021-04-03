#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 26 19:42:10 2021

@author: deepak

Data used – map.shp, Boundary_State_NAD27.shp, Boundry_County_NAD27.shp
Now by reading the shape files, we have to plot the .shp data on the
map
"""

#sudo apt install qgis qgis-plugin-grass


import geopandas as gpd

import matplotlib.pyplot as plt

#import gdal
#import shapely
#There's a trap for first time users of shapefiles.
#The actual shapefile (.shp) is useless without the companion files: .dbf, .shx, .prj etc..
gdf=gpd.read_file("file:///home/deepak/Desktop/petrabytes/Solutions/TEST_2/NS_Python_Test/map.shp")



print(gdf.shape)
print(gdf.head())

gdf.plt()
gdf.show()








import numpy as np
import pandas as pd
import shapefile as shp
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid", palette="pastel", color_codes=True)
sns.mpl.rc("figure", figsize=(10,6))

shp_path = "map.shp"
sf = shp.Reader(shp_path)

len(sf.shapes())

#sf.records()[1]

#sf.records()[1][5]
#sf.records()[25]

def read_shapefile(sf):
    """
    Read a shapefile into a Pandas dataframe with a 'coords' 
    column holding the geometry information. This uses the pyshp
    package
    """
    fields = [x[0] for x in sf.fields][1:]
    records = sf.records()
    shps = [s.points for s in sf.shapes()]
    df = pd.DataFrame(columns=fields, data=records)
    df = df.assign(coords=shps)
    return df



df = read_shapefile(sf)
df.shape

import geopandas

gdf = geopandas.read_file("/home/deepak/Desktop/petrabytes/Solutions/TEST_2/NS_Python_Test/map.shp")


import arcpy

import pandas as pd

input = "/home/deepak/Desktop/petrabytes/Solutions/TEST_2/NS_Python_Test/map.shp"

arr = arcpy.da.TableToNumPyArray(input, ("FIRE_ID", "FIRENAME"))

df = pd.DataFrame(arr)
