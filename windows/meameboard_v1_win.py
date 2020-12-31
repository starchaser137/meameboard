# PROGRAM TO COPY MEME RESPONSES TO CLIPBOARD
# DEPENDENCIES:
#   pywin32
#   pillow

import os
from io import BytesIO
import win32clipboard
from PIL import Image

img_list = os.listdir('pics')
filepath = ""

def send_to_clipboard(clip_type, data):
    win32clipboard.OpenClipboard()
    win32clipboard.EmptyClipboard()
    win32clipboard.SetClipboardData(clip_type, data)
    win32clipboard.CloseClipboard()

def sendimg():
    filepath = "pics/" + img_list[int(inp)]
    image = Image.open(filepath)
    
    output = BytesIO()
    image.convert("RGB").save(output, "BMP")
    data = output.getvalue()[14:]
    output.close()

    send_to_clipboard(win32clipboard.CF_DIB, data)

def gen_list():
    element = 0
    for i in img_list:
        print(str(element) + " " + img_list[element])
        element += 1

while True:
    gen_list()
    print()
    print('type "exit" to exit')
    inp = (input(">> ")).replace(" ", "")

    if inp == "exit":
        exit()

    if int(inp) > len(img_list) or int(inp) < 0:
        print("Out Of Range")

    sendimg()

    os.system("cls")



