# Setup the empatica E4 wristband

### Download and install software
Download and install the [E4 streaming server](http://get.empatica.com/win/EmpaticaBLEServer.html).

Download and install the bluetooth drivers found [here](https://www.silabs.com/documents/login/software/BLED112-Signed-Win-Drv.zip).
Follow the instructions in the zip file.

### Aquire the API key for the wristband
If you do not have an account at empatica, you can create one [here](https://www.empatica.com/connect/login.php).
After it has been created, click on *become a developer* on the top right of the site. Here you need to input a `purchase key`, 
so that your account can interact with the device. On this page you will also find the `API key`, which we will use later.

### Connect your device
1. Open E4 streaming server, and input your API key in settings.
2. Connect the bluetooth dongle to your USB port.
3. Turn on your wristband
4. The wristband should now show as connected on the E4 streaming server.
