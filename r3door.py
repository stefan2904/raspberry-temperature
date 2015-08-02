import json
import requests


def getStatusByName(data, name):
    for node in data['sensors']['door_locked']:
        if node['name'] == name:
            return node['value']


def getDoorstatus():
    resp = requests.get(url="http://realraum.at/status.json")
    data = resp.json()
    locked = getStatusByName(data, 'TorwaechterLock')
    kontakted = getStatusByName(data, 'TorwaechterAjarSensor')
    return (locked, kontakted)
