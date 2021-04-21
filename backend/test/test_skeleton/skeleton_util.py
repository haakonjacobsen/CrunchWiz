import pandas as pd
import os

def get_n_skeleton_points(n):
    """
    :param n: number of points to return
    :type n: int
    :return:
    """
    skeleton_data = []

    # Get test data from scuffed CSV
    df = pd.pandas.read_csv(
        os.path.join(os.path.dirname(__file__), "test_data.csv"), header=None
    )
    n = min(n, len(df))
    for i in range(n):
        temp_array = []
        row = df.iloc[i].tolist()
        i = 0
        while i < len(row):
            number = (
                float(row[i].strip().strip("[]()")),
                float(row[i + 1].strip().strip("[]()")),
            )
            i += 2
            temp_array.append(number)
        skeleton_data.append(temp_array)
