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
#importing the Library
import pandas as pd
import matplotlib.pyplot as plt

#Reading the excel sheet using python code
excel_test_data1=pd.read_excel("/home/deepak/Desktop/petrabytes/Solutions/TEST_2/NS_Python_Test/ExcelTestData1.xlsx")

#excel_test_data1.info()
# To remove first row that consists of units only not any values
excel_test_data1.drop(excel_test_data1.index[:1], inplace=True)

"""
Box plot is also used to see how data for a numerical
value is spread or distributed over the range
"""
#for 2st part: for BOX PLOT
plt.boxplot(excel_test_data1["RHOB1"],patch_artist=True,labels=['excel_test_data1["RHOB1"]'])
#argument "patch_artist=True", fills the boxplot and argument "label" takes label to be plotted.

plt.title("2. Distribution of RHOB1 in g/cc (Box Plot)")    #Providing a title
plt.show()







