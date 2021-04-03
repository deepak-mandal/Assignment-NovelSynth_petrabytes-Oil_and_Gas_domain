#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 6 – Plotting GIS Data on maps

Data used - Latitude_Long_Example_Data.csv


plot the latitude and longitude values from the data.
"""
"""
#using Google Colab

#pip install geopandas

import plotly.graph_objects as go

import pandas as pd

from google.colab import files
uploaded = files.upload()

import io

df=pd.read_csv(io.BytesIO(uploaded['Latitude_Long_Example_Data.csv']))

#df.info()
df['text'] = df['QQQQ'].astype(str)

fig = go.Figure(data=go.Scattergeo(
        lon = df['LONG'],
        lat = df['LAT'],
        text = df['text'],
        mode = 'markers',
        
        ))

fig.update_layout(
        title = 'Assignment 6 – Plotting GIS Data on maps using Latitude_Long_Example_Data.csv file', 
        #geo_scope='north america'
        )

fig.show()


"""
