from PIL import Image, ImageOps
from dotenv import load_dotenv
import os
import numpy as np
from stl import mesh

def make_mesh(greyscale):
    vertices = np.array()
    width, height = greyscale.size
    for y in range(height):
        for x in range(width):
            depth = img.getpixel((x, y))
            np.append(vertices, [x, y, depth])

    faces = np.array()
    for y in range(1, height-1):
        for x in range(width):
            np.append(faces, [])

    cube_mesh = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube_mesh.vectors[i][j] = vertices[f[j], :]
    

#file_path = input("File path of image: ")
#region for testing:
load_dotenv() 
file_path = os.getenv("IMG_PATH")
#endregion
img = Image.open(file_path) 
greyscale = ImageOps.grayscale(img) 
make_mesh(greyscale).save('cube.stl')
