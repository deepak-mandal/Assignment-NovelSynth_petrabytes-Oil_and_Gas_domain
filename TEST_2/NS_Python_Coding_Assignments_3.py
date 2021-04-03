#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Assignment 3 – Flow Chart
1. Using the graphviz module, create a flowchart as per the following
2. Functional Elements A, B, C, D, E
a. Output from A goes to B
b. Output from B goes to D
c. Output from C & D goes to E
d. Output from A goes to E
3. Python script should create the flow chart for the above process.
"""

"""
To install graphviz and use man dot (for dotFiles): 
sudo apt-get install graphviz
"""
#importing the lib.
from graphviz import Digraph

dot = Digraph(comment='The Round Table for creating flow chart')
#dot
#create a flowchart for the function element A, B, C, D, E
dot.node('A', 'A')
dot.node('B', 'B')
dot.node('C', 'C')
dot.node('D', 'D')
dot.node('E', 'E')

"""
AB: Output from A goes to B
BD for Output from B goes to D
CE & DE for Output from C & D goes to E
DE: Output from A goes to E
"""
dot.edges(['AB', 'BD', 'CE', 'DE', 'AE'])

print(dot.source)   #printing the source code which is same to .gv file

#To view image : sudo apt install imagemagick-6.q16
#Result printing the for flow chart
dot.render('NS_Python_Coding_Assignments_3_flow_chart.gv', view=True)





