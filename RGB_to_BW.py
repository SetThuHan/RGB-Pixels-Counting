import numpy as np
import glob
from PIL import Image

print ("e.g: /Path/to/ ")
Path = input("Type image path (path/dir/) : ")
for file in glob.glob(Path+'/*.png'):
	img = Image.open(file)
	img_conv = img.convert("RGBA")
	red_data = np.array(img_conv)
	green_data = np.array(img_conv)
	blue_data = np.array(img_conv)
print ("Processing image...")

red ,green ,blue, alpha =red_data.T
red ,green ,blue, alpha =green_data.T
red ,green ,blue, alpha =blue_data.T

red_areas = (red == 255) & (green == 0) & (blue == 0)
red_data[..., :-1][red_areas.T] = (255,255,255)

blue_areas = (red == 0) & (green ==  0) & (blue == 255)
blue_data[..., :-1][blue_areas.T] = (1,1,1)

green_areas = (red == 0) & (green == 255) & (blue == 0)
green_data[..., :-1][green_areas.T] = (1,1,1)

red_green_blue_data = red_data + (green_data & blue_data)

img_result = Image.fromarray(red_green_blue_data)
img_result.show() 
img_result.save(Path + 'result.png')
