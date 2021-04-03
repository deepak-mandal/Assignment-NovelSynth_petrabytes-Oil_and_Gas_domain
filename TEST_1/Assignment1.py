#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 1

1. Read the “Mud_Weight.csv” file in python.
2. Create a Plot using matplotlib like the sample on right
"""
import pandas as pd
import matplotlib.pyplot as plt

#1. Reading the Mud_Weight.csv file
mud_weight_data=pd.read_csv("/home/deepak/Desktop/petrabytes/Solutions/TEST_1/Mud_Weight.csv")

#Eleminating the irrelevent or unwanted data from Mud_Weight.csv
mud_weight_data.drop(columns=["Unnamed: 2", "Unnamed: 3"], inplace=True)
mud_weight_data.drop(mud_weight_data.index[:1], inplace=True)

#Renaming the column name with their units
mud_weight_data=mud_weight_data.rename(columns={"MD": "MD (m)"})
mud_weight_data=mud_weight_data.rename(columns={"Mud_Weight": "Mud_Weight (lbm/galUS)"})

#mud_weight_data.info()
#for Ploting using line plot in matplotlib library in python
fig, ax = plt.subplots(figsize=(25, 15))
ax.patch.set_facecolor('#6495ED')
plt.plot(mud_weight_data["Mud_Weight (lbm/galUS)"], mud_weight_data["MD (m)"], linewidth=5, color="yellow")
#labeling the x and y axis
plt.xlabel("Mud Weight")
plt.ylabel("Depth (m)")
plt.title("MD (m) Vs Mud_Weight (lbm/galUS) graph")
plt.show()




