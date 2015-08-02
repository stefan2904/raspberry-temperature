def loadTemp():
    tfile = open("/sys/bus/w1/devices/10-000801375be4/w1_slave")
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    temperature = temperature / 1000
    return temperature

def getTemp():
    while True:
        temp = loadTemp()
        if temp < 85:
            break
    return temp
