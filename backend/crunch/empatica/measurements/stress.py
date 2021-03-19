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
