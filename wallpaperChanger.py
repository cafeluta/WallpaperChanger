from pathlib import Path
import random
import ctypes
import subprocess
import wallpaperDownloader

# Run the script so it downloads a new photo
wallpaperDownloader.download_wallpaper()

# wallpaper folder
folder = Path("./Wallpapers")
wallpapers = list(folder.glob("*.png"))

# random wallpaper from the list
chosen_wallpaper = random.choice(wallpapers)

# Set the walppaer in win11
ctypes.windll.user32.SystemParametersInfoW(20, 0, str(chosen_wallpaper.resolve()), 3)

