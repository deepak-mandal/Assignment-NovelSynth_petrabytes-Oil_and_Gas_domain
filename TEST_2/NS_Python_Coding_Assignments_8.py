#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 8 – Reading and plotting data from HDF
Data used: Test.petrabytes

1. Read the petrabytes file (which is the HDF format).
2. Read data from Well 1 and well 2 and plot on the matplot using matplotlib
"""
import h5py
import pandas as pd
import matplotlib.pyplot as plt

print("For well_1 from Test.petrabytes HDF data")
#Reading the petrabytes file (which is the HDF format).
filename = "Test.petrabytes"

with h5py.File(filename, "r") as f:
    # List all groups
    # print("Keys: %s" % f)
    a_group_key = list(f.keys())[0]
    # print(a_group_key)
    # Get the data
    data = list(f[a_group_key]["well_1"])   
    print(data)    ##To get the dataset name/ID
    data = list(f[a_group_key]["well_1"]["1234"])
    print(type(data))

    df = pd.DataFrame(data)     #creating dataframe of well_1/1234 data
    print(df)
    
#Ploting well 2 data on the matplot using matplotlib
plt.plot(df)
plt.title('Graph for Well_1 from Test.petrabytes HDF file format data, using matplotlib')
plt.xlabel('Well_1 data')   #labeling x axis
plt.ylabel('Number of records') #labeling y axis
plt.legend(['0', '1', '2', '3', '4'], loc=4)
plt.show()


##################################################
print()
#################################################
print("For Well_2 data from Test.petrabytes HDF file")
#Reading the petrabytes file (which is the HDF format).
filename = "Test.petrabytes"

with h5py.File(filename, "r") as f:
    # List all groups
    # print("Keys: %s" % f)
    a_group_key = list(f.keys())[0]
    # print(a_group_key)
    # Get the data
    data = list(f[a_group_key]["well_2"])   #To get the dataset name/ID
    print(data)
    data = list(f[a_group_key]["well_2"]["2222"])
    print(type(data))

    df1 = pd.DataFrame(data)    #creating dataframe of well_2/2222 dataset
    print(df1)
    
    
#Now,Ploting well 2 data on the matplot using matplotlib
fig, ax = plt.subplots(figsize=(15, 8))
plt.plot(df1, linewidth=5)
plt.title('Plot for Well_2 data from Test.petrabytes HDF file using matplotlib')
plt.xlabel('Well_2 data')   #labeling x axis
plt.ylabel('Number of records') #labeling y axis
plt.legend(['0', '1', '2', '3', '4'], loc=1)
plt.show()