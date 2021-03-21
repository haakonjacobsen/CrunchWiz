import numpy as np
import pandas as pd
import sympy as sym

df = pd.read_csv("backend/crunch/skeleton/skeleton-S001.csv")


def get_joint_by_index(t, j):
    """
    Main function which reads rows/columns values
    and puts these into an array
    Parameters:
        t (int): Time in second
        j (int): Joint number ranges from 0 to 24
    Returns:
        skele (list): A list of all skeleton joints
        skele[j] (float): A value for specific joint
    """
    # TODO: Refactor to use array instead of directly referencing pandas dataframes
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
    """ Calculating the L2 norm of two given lists
    Parameters:
        a (list): List 1
        b (list): List 2
    Returns:
        norm (float): L2 norm
    """
    norm_x = (a[0] - b[0]) ** 2
    norm_y = (a[1] - b[1]) ** 2
    norm_z = (a[2] - b[2]) ** 2
    return np.sqrt(norm_x + norm_y + norm_z)


def func(a, b):
    """Takes two point, and makes a direction vector,
    then using said vector to calculate three
    equations responsible for x,y,z.
    Since they are dynamic, we use sympy
    to create the mathematical expressions
    Parameters:
        a (list): List of coordinates for point 1
        b (list): List of coordinates for point 2
    Returns:
        x,y,z (float): Three functions with respect to x,y,z
    """
    t = sym.symbols("t")
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
    """Uses finite difference of the third
    derivate, of second order to estimate jerk
    error coefficient is ommited in this calculation
    h is default set to 0.25, since an interval 1 second
    it will get 4 evenly splits
    Parameters:
        f (expression): A sympy function with respect to t
        tstart (int): Start time
        tend (int):  End time
    Returns:
        diff (float): Estimated jerk
    """
    t = sym.symbols("t")
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
    """ Measures fatigue for every joint
    by finding their functions, and applying
    finite differences
    Parameters:
        t0 (int): Start time
        t1 (int): End time
    Returns:
        totalFatigue (float): Fatigue for all joint for given time interval
    """
    totalFatigue = 0.0
    totalJoint = 24
    for i in range(25):
        jointFatigue = 0
        x, y, z = func(get_joint_by_index(t0, i), get_joint_by_index(t1, i))
        # we apply absolute value since we are interested in positive movement
        jointFatigue += np.abs(finiteDiff(x, t0, t1))
        jointFatigue += np.abs(finiteDiff(y, t0, t1))
        jointFatigue += np.abs(finiteDiff(z, t0, t1))
        totalFatigue += jointFatigue / totalJoint
    return totalFatigue


def amount_of_motion(t0, t1):
    """ Take norm of two points and
    averageing, before summing them up
    Parameters:
        t0 (int): Start time
        t1 (int): End time
    Returns:
        total (float): Total motion for given interval
    """
    total_joints = 24
    total = 0
    for i in range(25):
        jointTotal = norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
        total += jointTotal / total_joints
    return total


def most_used_joints(t0, t1, list):
    """ Putting the norm in a list such that
    list[0] = joint 0, list[1] = joint 1 etc.
    Parameters:
        t0 (int): Start time
        t1 (int): End time
        list (list): List requires a list to append values to i.e [0] * 25
    Returns:
        list (list): The inputted array with used joints appended
    """
    for i in range(25):
        list[i] += norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
    return list


def stability_of_motion(t0, t1):
    """ Take norm of two points before applying
    a formula, and summing them up
    Parameters:
        t0 (int): Start time
        t1 (int): End time
    Returns:
        total_distance (float): Distance for all joints given an interval
    """
    total_distance = 0
    for i in range(25):
        euclid = norm_by_array(get_joint_by_index(t1, i), get_joint_by_index(t0, i))
        total_distance += 1 / (1 + euclid)
    return total_distance
