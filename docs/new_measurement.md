# How to add a new measurement to the backend pipeline
One of the most important non-functional requirement we had is modularity.
We wanted to make it easy for the customers of this project to change parameters (window size etc.) of
measurements, and add/remove measurements. Below is a simple two step guide to add a new measurement.

### Create the measurement function
The measurement function should take in raw data from either the wristband, eyetracker or openpose.
In this example we will take in raw data from the wristband.

Create in the `backend/crunch/empatica/measurements/` folder. The function should take as input
one of the raw data available from the wristband (EDA, temperature, BVP, acceleration, IBI or HR). 
In this example we take in the heart rate signal, and calculate the mean.

```python
def average_hr(HR):
    """
    Finds the average heart rate of a heart rate signal
    
    :param HR: List of heart rate values
    :return: Average heart rate
    """
    
    average = sum(HR)/len(HR)
    return average
```

### Add the measurement function to the pipeline
Now that we have created our measurement function, all we need to do is add it to the pipeline.
Navigate to the file `backend/crunch/empatica/main.py`.

Import the measurement function we just created. 
```python
from crunch.empatica.measurements.average_hr import average_hr
```

In the `start_empatica()` function, create the datahandler, and subscribe it to the correct raw data,
in the same way as the rest of the measurements.

```python
def start_empatica(api):
    .
    .  
    .
    # Create the data handler
    average_hr_handler = DataHandler(
        measurement_func=average_hr,                    # The measurement function we created
        measurement_path="average_hr.csv",              # The path to save the result
        window_length=20,                               # how many data points in window
        window_step=20,                                 # How many data points between windows
        baseline_length=36,                             # How many data points for baseline
    )
    # Subscribe the data handler to the correct raw data
    api.add_subscriber(average_hr_handler, "HR")
    .
    .
    .
```

Great job! The average heart rate measurement is now added to the pipeline,
and it will be shown in the frontend dashboard when you run the program. You
can also easily change parameters like the window size of all measurements we have added.
