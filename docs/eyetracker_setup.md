# How to get the eyetracker to work:

### Connect and install eyetracker software
1. Install software and connect the device, watch the video under "learn & support":

    https://www.tobiipro.com/product-listing/tobii-pro-x3-120/

    At this point you should have installed "Installation and Configuration Tool for Tobii Pro X2 and X3 eye trackers", which can be found below the video that is linked above.


    I also would recommend to install the eyetracker manager:

    https://www.tobiipro.com/product-listing/eye-tracker-manager/

    Use the manager to calibrate the eyetracker

2. Interface with python and this project:
    * python 3.6 is needed. Important, and not mentioned in link below
    * Follow instructions: http://developer.tobiipro.com/python/python-getting-started.html
    * The sdk should be in backend/crunch/eyetracker

When running main and the eyetracker is not connected or appropriate software installed, the eyetracker will just print
 that no eyetracker was found.
 
 If the device is disconnected mid session, the measurements will not be calculated, but the process will continue to
 wait for the callback function. Reconnecting the device should be fine.
