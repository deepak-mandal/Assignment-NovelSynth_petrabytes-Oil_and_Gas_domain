#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 18:52:11 2021

@author: deepak
"""


def check_leap(year):
    if year%4==0 and year%100!=0:
        print("{} is a Leap Year".format(year))
    elif year%100==0:
        print("{} is not a Leap Year".format(year))
    elif year%400==0:
        print("{} is a Leap Year".format(year))
    else:
        print("{} is not a Leap Year".format(year))
        
        
    
year=int(input("Enter year: "))
check_leap(year)
        
        
        
