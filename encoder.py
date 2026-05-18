from PIL import Image
import numpy as np
from scipy.io.wavfile import write
from morse import MORSE



def convert(val):
    result = []
    for digits in str(val):
        
        result.append(MORSE[digits])
    return ' '.join(result)



img = Image.open("Image/mei.png").convert('RGB')

length, width = img.size

pixel_morse=[]

for i in range(length):
    for j in range(width):
        
        pixel = img.getpixel((j,i))
        r,g,b = pixel
        r_morse = convert(r)
        g_morse = convert(g)
        b_morse = convert(b)
        pixel_morse.append(f"{r_morse}|{g_morse}|{b_morse}")

with open("output.txt", "w") as f:
    f.write('/'.join(pixel_morse))