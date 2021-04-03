#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:28:54 2021

@author: deepak
"""

A0 = dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
A1 = range(10)
A2 = sorted([i for i in A1 if i in A0])
A3 = sorted([A0[s] for s in A0])
A4 = [i for i in A1 if i in A3]
A5 = {i:i*i for i in A1}
A6 = [[i,i*i] for i in A1]
#print(A0,A1,A2,A3,A4,A5,A6)
print(A0)
print()
print(A1)
print()
print(A2)
print()
print(A3)
print()
print(A4)
print()
print(A5)
print()
print(A6)