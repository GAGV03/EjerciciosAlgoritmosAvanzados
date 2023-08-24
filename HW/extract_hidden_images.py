#----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
#
# Date: 25-Aug-2023
# Authors:
#           A01747869 Gustavo Gutiérrez
#           A01746219 Eric Martínez
#----------------------------------------------------------

from PIL import Image
from delocate.fuse import fuse_wheels
fuse_wheels('Pillow-9.4.0-cp39-cp39-macosx_11_0_arm64.whl')
import sys

INPUT_FILE_NAME = sys.argv[1]
OUPUT_FILE_NAME_1 = "scarlett_channel_1_red.png"
OUPUT_FILE_NAME_2 = "scarlett_channel_2_green.png"
OUPUT_FILE_NAME_3 = "scarlett_channel_3_blue.png"

def process_image() -> None:
    with Image.open(INPUT_FILE_NAME) as input_file:
        pixin = input_file.load()
        width, height = input_file.size()
        output_image = Image.new('RGB',(width,height))
        pixout = output_image.load()
        for z in range (1,3):
            if z == 1:
              for y in range (height):
                for x in range (width):
                    r,_,_ = pixin[x,y]
                    pixout[x,y] = (r,0,0)  
            output_image.save(OUPUT_FILE_NAME_1)

            elif z == 2:
                for y in range (height):
                 for x in range (width):
                    _,g,_ = pixin[x,y]
                    pixout[x,y] = (0,g,0)  
            output_image.save(OUPUT_FILE_NAME_2)

            else:
               for y in range (height):
                for x in range (width):
                    _,_,b = pixin[x,y]
                    pixout[x,y] = (0,0,b) 
            output_image.save(OUPUT_FILE_NAME_3)
                    
#print(f'{x ^ y = :08b}')
__name__ == '__main__':
process_image()
    