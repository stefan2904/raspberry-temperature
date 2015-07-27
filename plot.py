import matplotlib.pyplot as plt
import datetime
import numpy as np
import csv

#x = np.array([datetime.datetime(2013, 9, 28, i, 0) for i in range(24)])
#y = np.random.randint(100, size=x.shape)

data = {}

with open('temp_log.csv', 'rb') as csvfile:
    logreader = csv.DictReader(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in logreader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]


x = map(lambda x: datetime.datetime.fromtimestamp(int(x)), data['time'])
y = data['temp']


plt.plot(x,y)
#plt.show()

plt.savefig('temp_plot.png')
