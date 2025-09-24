import requests
import random

from pathlib import Path
from secretAPI import id_key

maxNumberOfWallpapers = 1000

# UNSPLASH API
# id_key = your UNSPLASH API KEY
# unsplash_url = "https://api.unsplash.com/search/photos"

# # GET request
# payload = {'query' : 'mountains forest 1920x1080p', 'client_id' : id_key}
# r = requests.get(unsplash_url, params=payload)
# r_dict = r.json()

# print(f"!! INITIAL GET REQUEST: {r.status_code} !!")

# # Chosing a random photo
# numOfResults = len(r_dict['results'])
# chosenResult = random.randint(0, numOfResults - 1)
# print(f"!! CHOSEN RESULT: {chosenResult} !!")

# # Getting image url
# imageUrl = r_dict['results'][chosenResult]['urls']['full']

# print(f"!! CHOSEN PHOTO WITH URL: {imageUrl} !!")

# # Image response
# r_image = requests.get(imageUrl)

# Creating the .png
currentFolder = Path('./Wallpapers')

# creating the Wallpapers folder if it doesn't exists
currentFolder.mkdir(parents=True, exist_ok=True)

try:
    currentWallpapers = 0

    for item in currentFolder.iterdir():
        # saving in separate variables the name and extension of the file
        itemName = item.name
        itemExtension = itemName.rsplit('.')[-1]

        # saving only photos
        if itemExtension == 'png':
            currentWallpapers += 1


    wallpaperFileName = "Wallpaper" + str(currentWallpapers).zfill(3)
    print(wallpaperFileName)


except FileNotFoundError:
    print("== Something went WRONG with the app folder! ==")

