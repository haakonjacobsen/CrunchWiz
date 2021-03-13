# import measurement_functions
import pandas as pd
# import numpy as np
from measurement_functions import compute_stress


def empatica_main():
    """
    Collect data from empatica E4 API
    Compute measurements
    Write to CSV
    :return: void
    """
    __compute_stress()
    print("empatica process successfully started")


def __compute_stress():
    """
    Sends 8 temperature values from CSV file to compute_stress function
    :return: void
    """
    df = pd.read_csv("S001/TEMP2.csv")
    temperature_data = df.values.flatten().tolist()
    for i in range(1, len(temperature_data), 8):
        if len(temperature_data[i:]) >= 8:
            stress = compute_stress(temperature_data[i:i+8])
            if stress != 0.5:
                print(i+2, " - ", i+9)  # line nr. in csv file


empatica_main()
