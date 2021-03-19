import pandas as pd
import measurement_functions as mf


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
        motionArray.append(mf.amount_of_motion(i, j))
        stabilityArray.append(mf.stability_of_motion(i, j))
        fatigueArray.append(mf.fatigue(i, j))
        mf.most_used_joints(i, j, used_joints_list)
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
    # mode="a" appends, so we can add new data instead of wiping every time
    # default path, change accordingly
    df.to_csv("backend/crunch/skeleton/data/Skeleton.csv", mode="a", index=False)


def skeleton_main():
    """
    Get data from Tobii eye tracker API
    Preprocess
    Write to csv
    :return: void
    """
    # TODO: Refactor to read data and write pdf here instead of in measurement_functions
    print("skeleton process succesfully started")
    writeCSV(50, 60)


skeleton_main()
