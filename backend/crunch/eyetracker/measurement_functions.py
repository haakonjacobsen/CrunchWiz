#  Define functions that compute measurements here
import pandas as pd

df = pd.read_csv("it2901-crunchwiz/backend/crunch/eyetracker/ET-data-S001.csv")

def getValues(n):
    vals = []
    try:
        for i in range(n):
            vals.append(df.iloc[i])
    except:
        print("Error")
    return vals

def saccade_duration(start_time2, end_time1):
    return start_time2 - end_time1

def saccade_length(x1,y1,x2,y2):
    return ((x2-x1)**2 +(y2-y1)**2)**0.5



def perceived_difficulty(vals):
    count = 0
    sum = 0
    for i in range(1,len(vals)) :
        sacc_dur = saccade_duration(vals[i][1],vals[i-1][2])
        sacc_len = saccade_length(vals[i-1][5],vals[i-1][6],vals[i][5],vals[i][6])
        pd = 1/(1+(sacc_len / sacc_dur))
        count+=1
        sum+=pd
    
    sacc_speed = sacc_len / sacc_dur
    return sum/count
