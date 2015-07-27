import json
import requests

def getDoorstatus():
    resp = requests.get(url="http://realraum.at/status.json")
    data = json.loads(resp.text)
    locked = data['sensors']['door_locked'][0]['value']
    kontakted = data['sensors']['door_locked'][0]['value']
    return (locked, kontakted)

