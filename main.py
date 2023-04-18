import json

APIKEY = 'bae170ef64114272811713ac03aac058'
payload = {}
headers = {}


with open("data.json", 'r') as datafile:
    data = json.load(datafile)

with open("games-data.json", 'r') as datafile:
    gamesData = json.load(datafile)

games = []

keys = list(gamesData.keys())
results = data['results']
newGameData = {}

# { id, name, background-img, background-img-additional, rating, price, genres, tags }
for x in keys:
    game = gamesData[x]
    gameId = game['id']
    gameName = game['name']
    gameBg = game['background_image']
    gameBgAd = game['background_image_additional']
    gameRating = game['rating']
    gameRatings = game['ratings']
    gamePrice = game['price']
    gameGenres = game['genres']
    gameTags = game['tags']
    gameDescription = game['description']
    gameDescriptionRaw = game['description_raw']
    gameItem = {
        'id':  gameId,
        'name':  gameName,
        'background_image':  gameBg,
        'background_image_additional': gameBgAd,
        'rating':  gameRating,
        'ratings':  gameRatings,
        'price':  gamePrice,
        'genres':  gameGenres,
        'tags':  gameTags,
        'description':  gameDescription,
        'description_raw':  gameDescriptionRaw,
    }
    newGameData[x] = gameItem

gamesInfo = {'results': games}


with open('games-data.json', 'w') as gamesFile:
    json.dump(newGameData, gamesFile, indent=4)

print('operation complete')
