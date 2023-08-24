#----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
#
# Date: 25-Aug-2023
# Authors:
#           A01747869 Gustavo Gutiérrez
#           A01747 Eric Martínez
#----------------------------------------------------------

from PIL import Image
from delocate.fuse import fuse_wheels
fuse_wheels('Pillow-9.4.0-cp39-cp39-macosx_11_0_arm64.whl')
import sys



INPUT_FILE_NAME = sys.argv[1]
OUPUT_FILE_NAME_1 = "scarlett_channel_1_red.png"
OUPUT_FILE_NAME_2 = "scarlett_channel_2_green.png"
OUPUT_FILE_NAME_3 = "scarlett_channel_3_blue.png"



print(INPUT_FILE_NAME)