def compute_stress(temps_list):
    """
    Predicts acute stress based on GSR temperature
    :param temps_list: list of temperatures
    :return: returns the overall change in temperature in the list
    """
    temperature_sum = 0
    for i, temp in enumerate(temps_list[:-1]):
        change = temps_list[i+1] - temp
        temperature_sum += change
    return float(temperature_sum)
