import pandas as pd
import numpy as np
from sympy import symbols

df = pd.read_csv("backend/crunch/skeleton/skeleton-S001.csv")


def get_joint_by_index(t, j):
    # time,jointnr
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


t = symbols("t")


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


x, y, z = func([1, 3, 2], [-5, 0, 4])
finiteDiff(x, 1, 2)


def amount_of_motion(t0, t1):
    total_joints = 24
    total = 0
    for i in range(25):
        total += norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
    return total / total_joints


def most_used_joints(t0, t1, list):
    for i in range(25):
        list[i] += norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
    return list


def stability_of_motion(t0, t1):
    total_joints = 24
    total_distance = 0
    for i in range(25):
        euclid = norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
        total_distance += 1 / (1 + euclid)
    return total_distance / total_joints


def print_stability_of_motion(t):
    for i in range(t):
        print(stability_of_motion(i, i + 1))


def print_most_used_joints(t):
    used_joints_list = [0] * 25
    for i in range(t):
        most_used_joints(i, i + 1, used_joints_list)
    value = max(used_joints_list)
    print(used_joints_list)
    print("Joint nr:", used_joints_list.index(value), "moved:", value)


def print_amount_of_motion(t):
    for i in range(t):
        print(amount_of_motion(i, i + 1))


# print measurements for first t seconds
# print_stability_of_motion(20)
# print_most_used_joints(20)
# print_amount_of_motion(20)
