from csv import DictWriter
import os
import time
import pandas as pd
import numpy as np 

df = pd.read_csv("backend/preprocessing/dummy_data/skeleton/skeleton-S001.csv")

""" skele_container = [] #skele[jointtype][time][x,y,z]

print(skele_container[1][1])
print(skele_container) """

def returnByJoint(t,j): #time,jointnr   
    skele = []
    for i in range(25):
        temp = []
        #print(df.iloc[i+25*t][4])
        temp.append(df.iloc[i+25*t][1])
        temp.append(df.iloc[i+25*t][2])
        temp.append(df.iloc[i+25*t][3])
        skele.append(temp)
    if j == "all":
        #array jointnumber= indexnr i.e. skele[jointnr][x,y,z]
        return skele
    else:
        #array [x,y,z] coordinates
        return skele[j]

def normByArray(a,b):
    normX = (a[0]-b[0])**2
    normY = (a[1]-b[1])**2
    normZ = (a[2]-b[2])**2

    return np.sqrt(normX+normY+normZ)

def amountofMotion(t0,t1):
    totalJoints = 24
    sum = 0
    for i in range(25):
        sum += normByArray(returnByJoint(t1,i),returnByJoint(t0,i))
    return sum/24

def run(t):
    for i in range(t):
        print(amountofMotion(i,i+1))


run(20)

""" 
print(returnByJoint(0,"all"))
print(returnByJoint(4,1))
print(returnByJoint(51,2)) 
print(returnByJoint(300,3))

 """
