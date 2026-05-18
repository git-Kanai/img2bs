from PIL import Image

from morse import MORSE
channel = {v: k for k, v in MORSE.items()}

with open("output.txt", "r") as f:
    data = f.read()

pixel_morse = data.split('/')

pixel=[]

for i in pixel_morse:
    r_morse, g_morse, b_morse = i.split('|')
    r = int(''.join(channel[code] for code in r_morse.split(' ')))
    g = int(''.join(channel[code] for code in g_morse.split(' ')))
    b = int(''.join(channel[code] for code in b_morse.split(' ')))
    pixel.append((r,g,b))

width, height = 256,256

img = Image.new("RGB", (width, height))
img.putdata(pixel)

img.save("decoded.png")

    

