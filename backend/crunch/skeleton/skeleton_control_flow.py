import measurement_functions as mf


def main(tstart, tend):
    """ Write measurement from skeleton data
    from x seconds to y seconds """
    mf.writeCSV(tstart, tend)


main(50, 120)
