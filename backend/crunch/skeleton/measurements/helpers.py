import numpy as np
import sympy as sym


def norm_by_array(a, b):
    """ Calculating the L2 norm  """
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


def finite_diff(f, tstart, tend):
    """Uses finite difference of the third
    derivate, of second order to estimate jerk
    error coefficient is ommited in this calculation
    h is default set to 0.25, since an interval 1 second
    it will get 4 evenly splits"""
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

def writeCSV(t0, t1):
    """ Main function to write measurements to csv """
    timeArray = []
    motionArray = []
    fatigueArray = []
    stabilityArray = []
    jointArray = []
    valueArray = []
    used_joints_list = [0] * 25
    i = t0
    while i < t1:
        j = i + 1
        timeArray.append(j)
        motionArray.append(amount_of_motion(i, j))
        stabilityArray.append(stability_of_motion(i, j))
        fatigueArray.append(fatigue(i, j))
        most_used_joints(i, j, used_joints_list)
        value = max(used_joints_list)
        jointArray.append(used_joints_list.index(value))
        valueArray.append(value)
        i += 1
    dict = {
        "time": timeArray,
        "motion": motionArray,
        "stability": stabilityArray,
        "fatigue": fatigueArray,
        "most used joint": jointArray,
        "value for most used joint": valueArray,
    }
    df = pd.DataFrame(dict)
    print(df)
