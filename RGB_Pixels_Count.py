import numpy as np
from PIL import Image

print ("e.g: /Path/to/sample.png ")
Path = input("Type image path and file extension (only RGB image): ")
image = np.array(Image.open(Path).convert('RGB'))

Red_color = [255, 0, 0]
Green_color = [0, 255, 0]
Blue_color = [0, 0, 255]

Red_result = np.count_nonzero(np.all(image == Red_color, axis = 2))
Green_result = np.count_nonzero(np.all(image == Green_color, axis = 2))
Blue_result = np.count_nonzero(np.all(image == Blue_color, axis = 2))

print("Counting RGB pixels...")
print("Red  : ", Red_result, "  pixels")
print("Green: ", Green_result, "pixels")
print("Blue : ", Blue_result, "    pixels")
