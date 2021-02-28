#  Define functions that compute measurements here
def saccade_length(start_x1, end_y1, start_x2, end_y2):
    return ((end_y2 - end_y1) ** 2 + (start_x2 - start_x1) ** 2) ** 0.5


def saccade_duration(start_time2, end_time1):
    return start_time2 - end_time1


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
