import json

with open('games-data.json', 'r') as datafile:
    data = json.load(datafile)

keys = data.keys()

for x in keys:
    print(data[x]['price'])
