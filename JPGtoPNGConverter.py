import sys
import os
from PIL import Image

# Example to run: # python3 JOGtoPNGconverter.py folder newFolder

# get first and second argument
from_folder = sys.argv[1]
to_folder = sys.argv[2]

# check if newFolder exists, if not create it
if not os.path.isdir(to_folder):
    os.mkdir(to_folder)

# converts each image to png and saves to new folder
for filename in os.listdir(from_folder):
    image = Image.open(f"{from_folder}/{filename}")
    name = filename.split(".")[0]
    image.save(f"{to_folder}/{name}.png", "png")
