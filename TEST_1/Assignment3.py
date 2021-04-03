#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 3

Read the “Mud_Weight.csv” file in python.
Multiply the “Mud_Weight” data with ‘10’ value
Create another csv file “Mud_Weight_PI.csv” with the output
Create a HDF (Hierarchical Data Format) file with one float dataset named “DATA”. (search online)
Read the “Mud_Weight_PI.csv” file.
Write the data from the “Mud_Weight_PI.csv” file in the “DATA” node
Add the Attributes on the “DATA” node like the screenshot attached in the next slide with the current units from the “Mud_Weight_PI.csv” file.

"""
import pandas as pd
#import h5py

#1. Reading the “Mud_Weight.csv” file
mud_weight_data=pd.read_csv("/home/deepak/Desktop/petrabytes/Solutions/TEST_1/Mud_Weight.csv")


#Droping the unnecessary data
mud_weight_data.drop(columns=["Unnamed: 2", "Unnamed: 3"], inplace=True)
mud_weight_data.drop(mud_weight_data.index[:1], inplace=True)

#renaming the column data with their units name
mud_weight_data=mud_weight_data.rename(columns={"MD": "MD_in_m"})
mud_weight_data=mud_weight_data.rename(columns={"Mud_Weight": "Mud_Weight_in_lbm_per_galUS"})

#print(mud_weight_data.info())


#2. Multiplying the “Mud_Weight” data with ‘10’ value
arr1=[]	#for 1st column 
for i in mud_weight_data["MD_in_m"]:
    arr1.append(float(i))

x=pd.Series(arr1)    
x=(x*10)

arr2=[]	#for 2nd column
for j in mud_weight_data["Mud_Weight_in_lbm_per_galUS"]:
    arr2.append(float(j))

y=pd.Series(arr2)    
y=(y*10)


#3. Creating another csv file “Mud_Weight_PI.csv” with the output
df={"MD_in_m": x,
    "Mud_Weight_in_lbm_per_galUS": y}
df1=pd.DataFrame(df)    #creating dataframe
df1.to_csv("Mud_Weight_PI.csv")     #writting data into csv file format



#5. Reading the “Mud_Weight_PI.csv” file.
mud_weight_PI_data=pd.read_csv("/home/deepak/Desktop/petrabytes/Solutions/TEST_1/Mud_Weight_PI.csv")

#Just getting an insight of data created
mud_weight_PI_data.info()
print()
print()

#Droping the unnecessary coulmns
mud_weight_PI_data.drop(columns=["Unnamed: 0"], inplace=True)

#4. Creating a HDF (Hierarchical Data Format) file with one float dataset named “DATA”.

df_new = pd.DataFrame.from_records(mud_weight_PI_data.values)

import h5py
import numpy as np

f=h5py.File("Assignment3.hdf5", "w")
#creating dataset
dset=f.create_dataset("DATA", data=df_new, dtype="float")
print(dset)
print()
print()
f.close()


#6. Write the data from the “Mud_Weight_PI.csv” file in the “DATA” node
filename = "Assignment3.hdf5"
#printing all the data of HDF file of "DATA" node
#Hence it confirms that HDF data is created successfully.
with h5py.File(filename, "r") as f:
    print(list(f["DATA"]))









