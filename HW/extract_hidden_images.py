#----------------------------------------------------------
# Lab #1: Steganography
# Image processing through bit manipulation.
#
# Date: 25-Aug-2023
# Authors:
#           A01747869 Gustavo Alejandro Gutiérrez Valdes
#           A01746219 Eric Manuel Navarro Martínez
#----------------------------------------------------------

from PIL import Image
import sys

OUTPUT_FILE_NAME_1 = "scarlett_channel_1_red.png"
OUTPUT_FILE_NAME_2 = "scarlett_channel_2_green.png"
OUTPUT_FILE_NAME_3 = "scarlett_channel_3_blue.png"

def process_image_principal() -> None:
    try:
        INPUT_FILE_NAME = sys.argv[1]
        checker = Image.open(INPUT_FILE_NAME)
        if(checker.mode != "RGB"):
            print("This image isnt RGB")
            sys.exit()
        if(INPUT_FILE_NAME.split(".")[-1]!="png"):
            print("Invalid image type")
            sys.exit()
        
        process_image(INPUT_FILE_NAME)
        
    except IndexError:
        print("Please provide an image document as an argument.")
        sys.exit()
    except FileNotFoundError:
        print("The given document was not found.")
        sys.exit()
        

def process_image(INPUT_FILE_NAME) -> None:
    with Image.open(INPUT_FILE_NAME) as input_file:
        pixin = input_file.load()
        width, height = input_file.size
    output_image = Image.new('1',(width, height))
    pixout = output_image.load()

    for y in range (height):
        for x in range(width):
            r,_,_ = pixin[x,y]
            search = r & 1
            if search == 0:
                pixout[x,y] = 0 #Pixel found
            else:
                pixout[x,y] = 1 #Pixel not found
    output_image.save(OUTPUT_FILE_NAME_1) 
    
    for v in range (height):
        for u in range(width):
            _,g,_ = pixin[u,v]
            search = g & 1
            if search == 0:
                pixout[u,v] = 0 #Pixel found
            else:
                pixout[u,v] = 1 #Pixel not found
    output_image.save(OUTPUT_FILE_NAME_2)
  
    for n in range (height):
        for m in range(width):
            _,_,b = pixin[m,n]
            search = b & 1
            if search == 0:
                pixout[m,n] = 0 #Pixel found
            else:
                pixout[m,n] = 1 #Pixel not found
    output_image.save(OUTPUT_FILE_NAME_3)
   
if __name__ == '__main__':
    process_image_principal()
    