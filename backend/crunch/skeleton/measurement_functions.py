import pandas as pd
import numpy as np
import sympy as sym
import time

df = pd.read_csv("backend/crunch/skeleton/skeleton-S001.csv")
t = sym.symbols("t")

"""
Main function which reads rows/columns values
and puts these into an array
"""


def get_joint_by_index(t, j):
    skele = []
    for i in range(25):
        temp = [df.iloc[i + 25 * t][1], df.iloc[i + 25 * t][2], df.iloc[i + 25 * t][3]]
        skele.append(temp)
    if j == "all":
        # array jointnumber= indexnr i.e. skele[jointnr][x,y,z]
        return skele
    else:
        # array [x,y,z] coordinates
        return skele[j]


def norm_by_array(a, b):
    """ Calculating the L2 norm  """
    norm_x = (a[0] - b[0]) ** 2
    norm_y = (a[1] - b[1]) ** 2
    norm_z = (a[2] - b[2]) ** 2

    return np.sqrt(norm_x + norm_y + norm_z)


def func(a, b):
    vector = [
        b[0] - a[0],
        b[1] - a[1],
        b[2] - a[2],
    ]
    x = a[0] + (vector[0]) * t
    y = a[1] + (vector[1]) * t
    z = a[2] + (vector[2]) * t
    return x, y, z


def finiteDiff(f, tstart, tend):
    h = 0.25
    t0 = tstart
    t1 = tstart + h
    t2 = t1 + h
    t3 = t2 + h
    t4 = tend
    diff = (
        -0.5 * f.subs(t, t0) + f.subs(t, t1) - f.subs(t, t3) + 0.5 * f.subs(t, t4)
    ) / (h ** 3)
    return diff


def fatigue(t0, t1):
    totalFatigue = 0
    totalJoint = 24
    for i in range(25):
        jointFatigue = 0
        x, y, z = func(get_joint_by_index(t0, i), get_joint_by_index(t1, i))
        jointFatigue += np.abs(finiteDiff(x, t0, t1))
        jointFatigue += np.abs(finiteDiff(y, t0, t1))
        jointFatigue += np.abs(finiteDiff(z, t0, t1))
        totalFatigue += jointFatigue / totalJoint
    return totalFatigue


def amount_of_motion(t0, t1):
    total_joints = 24
    total = 0
    for i in range(25):
        jointTotal = norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
        total += jointTotal / total_joints
    return total


def most_used_joints(t0, t1, list):
    for i in range(25):
        list[i] += norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
    return list


def stability_of_motion(t0, t1):
    total_distance = 0
    for i in range(25):
        euclid = norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
        total_distance += 1 / (1 + euclid)
    return total_distance


def write_stability_of_motion(t):
    timeArray = []
    stabilityArray = []
    for i in range(t):
        j = i + 1
        timeArray.append(j)
        stabilityArray.append(stability_of_motion(i, j))
    dict = {"time": timeArray, "stability": stabilityArray}
    df = pd.DataFrame(dict)
    df.to_csv("backend/crunch/skeleton/data/StabilityOfMotion.csv", index=False)


def write_most_used_joints(t):
    timeArray = []
    jointArray = []
    valueArray = []
    used_joints_list = [0] * 25
    for i in range(t):
        j = i + 1
        most_used_joints(i, i + 1, used_joints_list)
        value = max(used_joints_list)
        timeArray.append(j)
        jointArray.append(used_joints_list.index(value))
        valueArray.append(value)
    dict = {"time": timeArray, "mostUsedJoint": jointArray, "value": valueArray}
    df = pd.DataFrame(dict)
    df.to_csv("backend/crunch/skeleton/data/MostUsedJoints.csv", index=False)


def write_amount_of_motion(t):
    timeArray = []
    motionArray = []
    for i in range(t):
        j = i + 1
        timeArray.append(j)
        motionArray.append(amount_of_motion(i, j))
    dict = {"time": timeArray, "motion": motionArray}
    df = pd.DataFrame(dict)
    df.to_csv("backend/crunch/skeleton/data/AmountOfMotion.csv", index=False)


def write_fatigue(t):
    timeArray = []
    fatigueArray = []
    # totalFatigue = 0
    for i in range(t):
        j = i + 1
        """
        Applies accumulated fatige over time
        totalFatigue += fatigue(i, j)
        timeArray.append(j)
        fatigueArray.append(totalFatigue)
        """
        timeArray.append(j)
        fatigueArray.append(fatigue(i, j))
    dict = {"time": timeArray, "fatigue": fatigueArray}
    df = pd.DataFrame(dict)
    df.to_csv("backend/crunch/skeleton/data/Fatigue.csv", index=False)


def main(n):
    write_stability_of_motion(n)
    write_most_used_joints(n)
    write_amount_of_motion(n)
    write_fatigue(n)


start_time = time.time()
main(120)
print("--- %s seconds ---" % (time.time() - start_time))
