# raspberry-temperature
measure (DS18S20P), log (python) &amp; plot (matlibplot/javascript) using raspberry pi

### WTF?

This scripts read and log the temperature and door status of [realraum Graz](http://realraum.at/).

### Setup

##### Setup Temperature Sensor

Connect the temperature sensor to your RPI [as described here](https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/#step-two):

![](https://www.cl.cam.ac.uk/projects/raspberrypi/tutorials/temperature/sensor-connection.png)

##### Setup Device Tree Overlay

Load the one-wire kernel module, setup the required pullup and define to which gpio pin your sensor is connected.
You need to find [the right pin id](http://wiringpi.com/pins/). (For example the id of GPIO6 is 25.)

The pullup is needed since the *DS18S20P* is being used in parasite power mode (See [Datasheet](http://pdfserv.maximintegrated.com/en/ds/DS18B20.pdf)).

Add to your */boot/config.txt* (and reboot):
```
dtoverlay=w1-gpio,gpiopin=25,pullup=1
```

([More infos on Device Tree Overlays](https://www.raspberrypi.org/documentation/configuration/device-tree.md).)

##### Load Kernel Modules

```
sudo modprobe w1-gpio
sudo modprobe w1-therm
```

### Usage

* **test.py** provides a short demo
* **logger.py** provides the actual logging
* **plot.py** creates a static plot of the logged data
* **index.html** displays interactive web-version of the data
* **sync.sh** synchronise (send) the newest measurement to a webserver (via ssh)

* **r3door.py** provides a function to access the door-status of realraum
* **r3temp.py** provides funcitonality to read the temperature maseured by the *DS18S20P*
