#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given
1. Anaconda Python Using Spyder IDE or can use pycharm with anaconda
2. Excel Files - ExcelTestData1.xlsx, ExcelTestData2.xlsx, ExcelTestData3.xlsx


Coding Assignment 2
Task: Reading excel file using Python

Goal:
1. Read excel sheet using python code and print values row by row.
"""
#importing library
import pandas as pd

#Reading the excel sheet using python code
excel_test_data1=pd.read_excel("/home/deepak/Desktop/petrabytes/Solutions/TEST_2/NS_Python_Test/ExcelTestData1.xlsx")

#print(excel_test_data1)
#excel_test_data1.info()

#Assign all the value of a specific column to a specific variable
x=excel_test_data1["MD"]
y=excel_test_data1["DT1"]
z=excel_test_data1["RHOB1"]

#print values row by row
print("Printing the values of ExcelTestData1.xlsx file row by row")
print()
print("MD(in ft)", "DT1(in us/ft)", "RHOB1(in g/cc)")
for i in range(1, len(x)):
    print(x[i], y[i], z[i])


"""
Similarly ExcelTestData2.xlsx, ExcelTestData3.xlsx
"""
#Reading the data from excel file
excel_test_data2=pd.read_excel("/home/deepak/Desktop/petrabytes/Solutions/TEST_2/NS_Python_Test/ExcelTestData2.xlsx")
#excel_test_data2.info()
#print(excel_test_data2.head(5))
#Assign all the value of a specific column to a specific variable

x2=excel_test_data2["MD"]
y2=excel_test_data2["INC."]
z2=excel_test_data2["AZM."]

#print values row by row
print()
print("Printing the values of ExcelTestData2.xlsx file row by row")
print("MD(in ft)", "INC.(in deg)", "AZM.(in deg)")
for i in range(1, len(x2)):
    print("{:4.2f}    {:4.2f}    {:4.2f}".format(x2[i], y2[i], z2[i]))
