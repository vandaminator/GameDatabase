import json

apiKey = 'bae170ef64114272811713ac03aac058'
payload = {}
headers = {}


with open("data.json", 'r') as datafile:
    data = json.load(datafile)

with open("games-data.json", 'r') as datafile:
    gamesData = json.load(datafile)

games = []

results = data['results']

# { id, name, background-img, rating, price, genres, tags }
for x in results:
    gameId = x['id']
    gameName = x['name']
    gameBg = x['background_image']
    gameRating = x['rating']
    gamePrice = x['price']
    gameGenres = x['genres']
    gameTags = x['tags']
    gameItem = {
        'id':  gameId,
        'name':  gameName,
        'background_image':  gameBg,
        'rating':  gameRating,
        'price':  gamePrice,
        'genres':  gameGenres,
        'tags':  gameTags,
    }
    games.append(gameItem)

gamesInfo = {'results': games}

keys = list(gamesData.keys())


with open('data.json', 'w') as gamesFile:
    json.dump(gamesInfo, gamesFile, indent=4)

print('operation complete')
