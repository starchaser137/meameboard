# PROGRAM TO COPY MEME RESPONSES TO CLIPBOARD
# DEPENDENCIES:
#   xclip program
#   pillow

import os
from PIL import Image
from time import sleep

print("MEAMEBOARD")
print()
print("Please use convertpng script to convert jpg files to png")
sleep(3)

img_list = os.listdir('pics')
filepath = ""

# PRINT LIST IN TERMINAL
def print_list():
    element = 0
    for i in img_list:
        print(str(element) + " " + img_list[element])
        element += 1

# MAINLOOP
running = True
while running:
    print_list()
    print()
    print('type "exit" to exit')
    inp = (input(">> ")).replace(" ", "")

    if inp == "exit":
        exit()

    elif int(inp) > len(img_list) or int(inp) < 0:
        print("Out Of Range")

    else:
        filepath = "pics/" + img_list[int(inp)]
        os.system("xclip -selection clipboard -t image/png -i " + filepath)

    os.system("clear")



