#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 4 – Plotting
Generate the following plots – create separate script for each plot type.
1. Histogram for the data
a. Input Data – Column B (DT1)
2. Box Plot
a. Input Data – Column C (Rhob1) – see example
"""
import pandas as pd
import matplotlib.pyplot as plt

#Reading the excel sheet using python code
excel_test_data1=pd.read_excel("/home/deepak/Desktop/petrabytes/Solutions/TEST_2/NS_Python_Test/ExcelTestData1.xlsx")

#excel_test_data1.info()
# To remove first row that consists of units only not any values
excel_test_data1.drop(excel_test_data1.index[:1], inplace=True)

"""
To create a Histogram, divide the data in bins.
bins divides the entire range of values in "n" equal parts, where "n" is
specified by us and count the number of records present in each of those parts
"""
#for 1st part: HISTOGRAM PLOT
plt.hist(excel_test_data1["DT1"], bins=10)
plt.xlabel("DT1")   #labeling x axis
plt.ylabel("No. of Records")    #labeling y axis
plt.title("1. Distribution of DT1 (Histogram Plot for frequency count or simply count of records over a range of values)")
plt.show()