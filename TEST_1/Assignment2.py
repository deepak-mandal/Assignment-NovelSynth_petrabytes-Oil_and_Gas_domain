#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 2

Read the “Mud_Weight.csv” file in python.
Create another csv file “Mud_Weight_Converted.csv” with converted log from “lbm/galUS” to “kg/m3” for the second column data.
"""
import pandas as pd


#1. Reading the Mud_Weight.csv file
mud_weight_data=pd.read_csv("/home/deepak/Desktop/petrabytes/Solutions/TEST_1/Mud_Weight.csv")
#info() method gives a brief idea about the data
mud_weight_data.info()
#to print the first 5 row
mud_weight_data.head()
#Since In the second row we have the unit of the data column.
#Hence it is str() datatype so, it can't be converted into float datatype
#Therefore, we need to eleminate it 
arr1=[]
for j in mud_weight_data["MD"]:
    arr1.append(j)

x=pd.Series(arr1[1:])

arr2=[]
for k in mud_weight_data["Mud_Weight"]:
    arr2.append(k)
    
y=pd.Series(arr2[1:])

#droping the row consists of str() datatype() i.e.;units
mud_weight_data.drop(mud_weight_data.index[:1], inplace=True)
#Renaming the data with their units for simplicity
mud_weight_data=mud_weight_data.rename(columns={"MD": "MD (m)"})
mud_weight_data=mud_weight_data.rename(columns={"Mud_Weight": "Mud_Weight (lbm/galUS)"})
#Here I am converting the datatype to float such that it can be multiplied withh float data type
#for unit conversion purpose
arr3=[]
for i in mud_weight_data["Mud_Weight (lbm/galUS)"]:
    arr3.append(float(i))

#converting it from “lbm/galUS” to “kg/m3” for the second column data.
z=pd.Series(arr3)    
z=(z*119.826428)

df={"MD (m)": x,
    "Mud_Weight (lbm/galUS)": y,
    "Mud_Weight (kg/m^3)": z
    }

#creating the dataframe for writting the data into another .csv file
df1=pd.DataFrame(df)
# Writing
df1.to_csv('Mud_Weight_Converted.csv')
