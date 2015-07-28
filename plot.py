import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as tkr
import datetime
import numpy as np
import csv

#x = np.array([datetime.datetime(2013, 9, 28, i, 0) for i in range(24)])
#y = np.random.randint(100, size=x.shape)

data = {}

# read data:

with open('temp_log.csv', 'rb') as csvfile:
    logreader = csv.DictReader(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for row in logreader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]

# prepare data:

x = map(lambda x: datetime.datetime.fromtimestamp(int(x)), data['time'])
y = data['temp']

# actual plotting:

def xfmt(x,pos=None):
    ''' custom date formatting '''
    x = mdates.num2date(x)
    label = x.strftime('%m/%d')
    label = label.lstrip('0')
    return label


plt.plot(x,y)

plt.setp(plt.gca().xaxis.get_majorticklabels(),rotation=90)
plt.gca().xaxis.set_major_formatter(tkr.FuncFormatter(xfmt))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=4))
plt.gca().xaxis.set_minor_locator(mdates.DayLocator())

plt.show()

plt.savefig('temp_plot.png')
