import numpy as np
import sympy as sym
import pandas as df


def norm_by_array(a, b):
    """ Calculating the L2 norm of two given lists
    :param :
        a (list): List 1
        b (list): List 2
    Returns:
        norm (float): L2 norm
    """
    norm_x = (a[0] - b[0]) ** 2
    norm_y = (a[1] - b[1]) ** 2
    norm_z = (a[2] - b[2]) ** 2
    return np.sqrt(norm_x + norm_y + norm_z)


def test_function(a):
    return 1


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
