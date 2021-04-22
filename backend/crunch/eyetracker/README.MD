# How to get the eyetracker to work:

### Connect and install eyetracker software
1. Install software and connect the device, watch the video under "learn & support":

    https://www.tobiipro.com/product-listing/tobii-pro-x3-120/
2. Interface with python and this project:
    * python 3.6 is needed. Important, and not mentioned in link below
    * Follow instructions: http://developer.tobiipro.com/python/python-step-by-step-guide.html

When running main and the eyetracker is not connected or appropriate software installed, the eyetracker will just print
 that no eyetracker was found.
 
 If the device is disconnected mid session, the measurements will not be calculated, but the process will continue to
 wait for the callback function. Reconnecting the device should be fine.
