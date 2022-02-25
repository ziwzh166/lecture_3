# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 14:14:58 2022

@author: zhao
"""
# practice with numpy
import numpy as np
#null vector fifth 1
p1 = np.zeros((10))
p1[5] = 1
#range from 10 to 49
p2 = np.linspace(10, 49)
#reverse p2
p3 = p2[::-1]
#0-9 arrary 3x3
p4 = np.arange(0,9,1).reshape(3,3)
#find non zero value
p5_1 =np.array([1,2,0,0,4,0])
p5_2 = p5_1[p5_1 != 0]
#create 30 random number calculate mean
p6_1 =np.random.rand(30)
p6_2 = np.mean(p6_1)
# create a matrix surrounded by 1
n = (5,4) #define size
p7 = np.zeros(n)
p7[:,(0,-1)] += 1
p7[(0,-1),1:-1] += 1
# chckerboard
p8 = np.zeros((8,8))
p8[::2,::2] =1
p8[1::2,1::2] =1
# checkerboard function
def checkerboard(n):
    #return a nxn checker board
    p9 = np.zeros((n,n))
    p9[::2,::2] =1
    p9[1::2,1::2] =1
    print(p9)
checkerboard(10)
#find value greater than 3 smaller than 8
p10 = np.arange(11)
p10 = p10[(p10>=3) & (p10<=8)]
print(p10)
#sort arrary
p11 = np.random.random(10)
p11 = np.sort(p11)
print(p11)
#check if two arrarys are equal
p12_A = np.random.randint(0,2,5)
p12_B = np.random.randint(0,2,5)
p12_equal = p12_A == p12_B
print(p12_equal)
#change the type of the array
p13_Z = np.arange(10, dtype=np.int32)
print(p13_Z.dtype)
p13_Z = p13_Z.astype('float32')
print(p13_Z.dtype)
# diagonal of matrix
p14_A = np.arange(9).reshape(3,3)
p14_B = p14_A + 1
p14_C = np.dot(p14_A,p14_B)
p14_D = np.diag(p14_C)
print(p14_D)