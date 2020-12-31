from time import sleep
import os
from PIL import Image

img_list = os.listdir('pics')

# FUNCTION TO CONVERT ALL FILES IN pics TO .png
def convert():
    print("CONVERTING IMAGES...")
    sleep(1)
    el = 0
    for a in img_list:
        print(img_list[el])
        im1 = Image.open(r'pics/' + img_list[el])
        nwname = (img_list[el]).replace(".jpg", ".png")
        im1.save(r'pics/' + nwname)
        print(nwname)
        el += 1

convert()
os.system("clear")