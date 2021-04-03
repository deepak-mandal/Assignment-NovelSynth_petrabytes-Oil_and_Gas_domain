#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Task Goals:
1. Generate random x and y arrays
a. X values range is 0-1000
b. Y Values range is 0-50
2.
Using the above example, generate x-y plot similar to the example plot
"""
#importing library in python
import matplotlib.pyplot as plt
import random

#To generate random x and y value and store it into array
x_arr=[]    #for storing x values
y_arr=[]    #for storing y values
for i in range(10):
    x_arr.append(random.randint(0, 1000))
    y_arr.append(random.randint(0, 50))
  
#To generate x-y plot
plt.figure(dpi=100)
plt.plot(x_arr, y_arr)
plt.xlabel("random x value in between 0 & 1000")    #labeling x axis
plt.ylabel("random y value in between 0 & 50")  #labeling y axis
plt.title("x-y plot (using random number generator function)")  #providing a suitable title
