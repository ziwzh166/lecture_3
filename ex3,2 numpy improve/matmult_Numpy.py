#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 09:11:59 2022

@author: zhao
"""

# Update for the preformance 
# Program to multiply two matrices using nested loops
import numpy as np

N = 250

# NxN matrix
X = []
X = np.random.randint(0,100,size =(N,N))

# Nx(N+1) matrix
Y = []
Y = np.random.randint(0,100,size =(N,N+1))
   
# result is Nx(N+1)
result = np.zeros((N,N+1))

# perform the Matrix mutiplacation
result = X@Y

#print results
print(result)