from .measurement_functions import writeCSV


def calculate_measurements(tstart, tend):
    """
    Write measurement from skeleton data
    from x seconds to y seconds
    """
    writeCSV(tstart, tend)


def skeleton_main():
    """
    Get data from Tobii eye tracker API
    Preprocess
    Write to csv
    :return: void
    """
    # TODO: Refactor to read data and write pdf here instead of in measurement_functions
    print("skeleton process succesfully started")
    calculate_measurements(50, 60)
