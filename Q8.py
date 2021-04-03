#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:19:30 2021

@author: deepak
"""
def bubble_sort(a):
    for x in range(len(a)-1, -1, -1):
        for j in range(x):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                
list1=["1", "4", "0", "6", "9"]
print(list1)
bubble_sort(list1)
print(list1)
    