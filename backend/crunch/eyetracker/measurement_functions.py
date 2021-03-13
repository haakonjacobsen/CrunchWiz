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

def fixation_duration(start_time1, end_time1):
    return end_time1 - start_time1


def compute_information_processing_index(list_of_init_times, list_of_end_times):
    """
    ratio global/local
    Take a time window
    Count the number of the long fixations followed by short saccades
    and vice versa à local processing
    Count the number of the short fixations followed by long saccades
    and vice versa à global processing
    Compute the ratio
    """

    # Q: What qualifies as long fixations/saccades?
    # Q: Preferred window size?
    # Q: have I understood "vice versa correctly"
    def is_short(duration):
        return duration > 100

    window_size = 9
    assert type(list_of_init_times) == type(list_of_end_times) == list
    assert len(list_of_init_times) >= window_size and len(list_of_end_times) >= window_size

    local_ipi, global_ipi = (0, 0)
    prev_saccade_is_long = False

    for i in range(window_size - 1):
        fixation_is_long = is_short(fixation_duration(list_of_init_times[i], list_of_end_times[i]))
        saccade_is_long = is_short(saccade_duration(list_of_init_times[i + 1], list_of_end_times[i]))
        if fixation_is_long and not saccade_is_long:
            local_ipi += 1
        elif not prev_saccade_is_long and fixation_is_long:
            local_ipi += 1
        elif not fixation_is_long and saccade_is_long:
            global_ipi += 1
        elif prev_saccade_is_long and not fixation_is_long:
            global_ipi += 1
        prev_saccade_is_long = saccade_is_long

    print(global_ipi / local_ipi)
    return global_ipi / local_ipi
