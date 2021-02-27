import pandas as pd
import numpy as np

df = pd.read_csv("backend/crunch/skeleton/skeleton-S001.csv")

""" skele_container = [] #skele[jointtype][time][x,y,z]

print(skele_container[1][1])
print(skele_container) """


def returnByJoint(t, j):
    # time,jointnr
    skele = []
    for i in range(25):
        temp = []
        temp.append(df.iloc[i + 25 * t][1])
        temp.append(df.iloc[i + 25 * t][2])
        temp.append(df.iloc[i + 25 * t][3])
        skele.append(temp)
    if j == "all":
        # array jointnumber= indexnr i.e. skele[jointnr][x,y,z]
        return skele
    else:
        # array [x,y,z] coordinates
        return skele[j]


def normByArray(a, b):
    normX = (a[0] - b[0]) ** 2
    normY = (a[1] - b[1]) ** 2
    normZ = (a[2] - b[2]) ** 2

    return np.sqrt(normX + normY + normZ)


def amountofMotion(t0, t1):
    totalJoints = 24
    sum = 0
    for i in range(25):
        sum += normByArray(returnByJoint(t1, i), returnByJoint(t0, i))
    return sum / totalJoints


def printAmountOfMotion(t):
    for i in range(t):
        print(amountofMotion(i, i + 1))


# printAmountofMotion(20)


def stabilityOfMotion(t0, t1):
    totalJoints = 24
    sum = 0
    for i in range(25):
        euclid = normByArray(returnByJoint(t1, i), returnByJoint(t0, i))
        sum += 1 / (1 + euclid)
    return sum / totalJoints


def printStabilityOfMotion(t):
    for i in range(t):
        print(stabilityOfMotion(i, i + 1))


# printStabilityOfMotion(20)

def mostUsedJoints(t0, t1, list):
    for i in range(25):
        list[i] += normByArray(returnByJoint(t1, i), returnByJoint(t0, i))
    return list


def printMostUsedJoints(t):
    usedJointsList = [0]*25
    for i in range(t):
        mostUsedJoints(i, i+1, usedJointsList)
    value = max(usedJointsList)
    print(usedJointsList)
    print("Joint nr:", usedJointsList.index(value), "moved:", value)


printMostUsedJoints(50)
