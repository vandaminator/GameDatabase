import requests
import json
import time


apiKey = 'bae170ef64114272811713ac03aac058'
payload = {}
headers = {}

with open("data.json", 'r') as datafile:
    data = json.load(datafile)

results = data['results']

gamesInfo = {}

for x in results:
    gameId = x['id']
    print(gameId)
    url = f"https://api.rawg.io/api/games/{gameId}/screenshots?key=bae170ef64114272811713ac03aac058"
    response = requests.request("GET", url, headers=headers, data=payload)
    time.sleep(2)
    data = response.json()
    gamesInfo[gameId] = data


with open('games-screenshots.json', 'w') as gamesFile:
    json.dump(gamesInfo, gamesFile, indent=4)
