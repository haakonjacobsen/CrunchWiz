def compute_hrv(list_of_ibi_values):
    """The root mean square of successive differences (RMSSD)
    One of many measures of HRV"""
    window_size = 10
    assert list == type(list_of_ibi_values)
    assert len(list_of_ibi_values) > window_size
    total = 0
    for i in range(1, window_size):
        total += (list_of_ibi_values[i] - list_of_ibi_values[i - 1]) ** 2
    return (total / (window_size - 1)) ** 0.5


def compute_emotional_regulation(list_of_ibi_values):
    """
    mr K: "The root mean square of successive differences (RMSSD)
    ”normal” Inter-Beat Interval (IBI) à remove too short and too large
    intervals.
    Percentage of successive IBI that differ by more than 50 ms."

    I have interpreted this as 3 alternative ways, where I chose the last one. """
    window_size = 10
    assert list == type(list_of_ibi_values)
    assert len(list_of_ibi_values) > window_size
    differs_more = 0
    differs_less = 0
    for i in range(1, window_size):
        if abs(list_of_ibi_values[i] - list_of_ibi_values[i - 1]) > 0.05:
            differs_more += 1
        else:
            differs_less += 1
    return differs_more / (differs_more + differs_less)


def compute_stress(temps_list):
    """
    Predicts acute stress based on GSR temperature
    :param temps_list:
    :return: 1 if acute stress event found, 0.5 otherwise
    """
    temperature_sum = 0
    temperature_threshold = -0.02
    for i, temp in enumerate(temps_list[:-1]):
        change = temps_list[i+1] - temp
        if change > 0:
            temperature_sum = 0
            continue
        temperature_sum += change
        if temperature_sum < temperature_threshold:
            #  return abs(round(temperature_sum, 2))
            return 1
    return 0.5
