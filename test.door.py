import r3temp
import r3door

(locked, kontakted) = r3door.getDoorstatus()
print 'door is', ('locked' if locked else 'unlocked'),
print 'and', ('closed' if kontakted else 'open')
