from PIL import Image, ImageOps
from dotenv import load_dotenv
import os

#file_path = input("File path of image: ")
#region for testing:
load_dotenv() 
file_path = os.getenv("IMG_PATH")
#endregion
img = Image.open(file_path) 
greyscale = ImageOps.grayscale(img) 

width, height = greyscale.size
for y in range(greyscale.height):
    for x in range(greyscale.width):
        depth = img.getpixel((x, y))
