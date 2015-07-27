import r3temp
import r3door

temp = r3temp.getTemp()
print 'current temperature:', temp, 'degreeC'

(locked, kontakted) = r3door.getDoorstatus()
print 'door is', ('locken' if locked else 'unlocked'),
print 'and', ('closed' if kontakted else 'open')
