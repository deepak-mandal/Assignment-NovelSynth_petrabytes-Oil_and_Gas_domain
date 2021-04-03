#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 4

1. Read the file “Survey_Data.csv”
2. Create a HDF file: Survey.h5
3. Create a float dataset node: DATA
4. Put all the data in the “DATA” node
5. Add the properties to the node like the screenshot
"""
#importing python library
import pandas as pd

#1. Reading the “Survey_Data.csv” file
survey_data=pd.read_csv("/home/deepak/Desktop/petrabytes/Solutions/TEST_1/Survey_Data.csv")

#printing the brief information about data
print(survey_data.info())
print()
print()


#2. Creating a HDF file: Survey.h5
#df_new = pd.DataFrame.from_records(survey_data.values)
"""
df={"MD":survey_data["MD"],
    "Incl": survey_data["Incl"],
    "Azim": survey_data["Azim"],
    "NS": survey_data["NS"],
    "EW": survey_data["EW"],
    "TVD": survey_data["TVD"]
    }
df_new=pd.DataFrame(df)
"""


#creating data frame from the .csv file 
df_new = pd.DataFrame.from_records(survey_data.values)
print(df_new.info())    #printing breif info adout dataframe
print(df_new.iloc[1:,:])    #prining and selecting the columns from 2nd row onwards

df_new2=df_new.iloc[1:,:]   #selecting the columns from 2nd row onwards
df_new2 = df_new2.astype(float, errors = 'raise')   #converting to float datatype from object data type as show in the info of data


#df_new2 = pd.DataFrame.from_records(df_new.values)
#print(df_new2.info())
import h5py


f=h5py.File("Survey.h5", "w")
#3. Creating a float dataset node: DATA, and
#4. Puting all the data in the “DATA” node
dset=f.create_dataset("DATA", data=df_new, dtype="float")
print(dset)
print()
print()
f.close()


filename = "Survey.h5"
#printing all the data of HDF file of "DATA" node
with h5py.File(filename, "r") as f:
    print(list(f["DATA"]))









