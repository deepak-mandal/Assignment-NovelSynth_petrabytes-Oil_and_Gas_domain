#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 16:10:28 2021

@author: deepak
"""
"""
Write the program for :
Given an integer, n , perform the following conditional actions:
• If n is odd, print Weird
• If n is even and in the inclusive range of to , print Not Weird
• If n is even and in the inclusive range of to , print Weird
• If is even and greater than , print Not Weird
Constraints
1<=n<=100
Output Format
Print Weird if the number is weird; otherwise, print Not Weird.

"""

n=int(input("Enter any number: "))


if n%2==1:
    print("Weird")
elif n%2==0 and 10<=n<=30:    #It is not given so, lets consider any range
    print("Not Weird")
elif n%2==0 and 31<=n<=75:
    print("Weird")
elif n%2==0 and n>75:
    print("Not Weird")
else:                       #for rest of the cases(let)
    print("Not Weird")























