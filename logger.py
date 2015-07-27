import time
import r3temp
import r3door
import csv

temp = r3temp.getTemp()
#print 'current temperature:', temp, 'degreeC'

(locked, kontakted) = r3door.getDoorstatus()
#print 'door is', ('locken' if locked else 'unlocked'),
#print 'and', ('closed' if kontakted else 'open')

row = [int(time.time()), temp, locked, kontakted]

with open('temp_log.csv', 'a') as csvfile:
    logwriter = csv.writer(csvfile, delimiter=';',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    logwriter.writerow(row)
