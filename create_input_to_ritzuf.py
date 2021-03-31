import sys
import os
import csv
import numpy as np
import random
import argparse


#creates list of rectangles based on room size and min and max rect sizes
def makeRects(room_size, min_rect_dim, max_rect_dim, rect_quant):

    #take the min rect width or height to calculate the maximum number of possible blocks
    max_possible_blocs = int(room_size / ( min_rect_dim * min_rect_dim))
    #create bank of random rects , quantized to 10 units jumps
    possible_rects = np.random.randint(min_rect_dim, max_rect_dim, size=(2, max_possible_blocs))

    #quntize the width and height of rects
    possible_rects = (( possible_rects / rect_quant ). astype(int))* rect_quant


    #sum till total rects size reaches the room size
    #take the required rects equals to room size
    total_size = 0
    possible_rects = np.transpose(possible_rects)
    for idx, rect in enumerate(possible_rects):
        total_size += rect[0]*rect[1]
        if total_size > room_size:
            break

    rects = possible_rects[:idx+1, :]


    return rects

#creates list of rectagles to csv file
def writeRectsToCsv(files_dir, csv_name, rects):

    csv_full_path = os.path.join(files_dir, csv_name)

    try:
        with open(csv_full_path, 'w', newline='') as f_csv:
            writer = csv.writer(f_csv)

            #loop over the rectangles and write them to csv file
            writer.writerow('W' 'H') # added by Ohad
            for rect in rects:
                writer.writerow(rect)

        f_csv.close()
    except:
        print(" #########################################################################")
        print(" ERROR !! : writing to csv check if your csv file is opened or path exists")
        print(" #########################################################################")
        return -1

    return 0

def main():

    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--files_dir', type=str, default=os.getcwd(),
                        help='directory to the working folder')
    parser.add_argument('--room_width', type=int, default=1000,
    help = 'room width in cm')
    parser.add_argument('--room_height', type=int, default=1000,
    help = 'room height in cm')
    parser.add_argument('--max_rect_width_height', type=int, default=109, # changed default to 109 instead 119 by Ohad
                        help='max rect width or height in cm')
    parser.add_argument('--min_rect_width_height', type=int, default=20,
                        help='min rect width or height in cm')
    parser.add_argument('--rect_jump', type=int, default=10,
                        help='rect width or height quantization in cm')



    args = parser.parse_args()


    room_size = args.room_width * args.room_height
    min_rect_dim = args.min_rect_width_height
    max_rect_dim = args.max_rect_width_height
    rect_quant = args.rect_jump
    files_dir = args.files_dir
    csv_name = "rects.csv"

    #make the rects with width and height
    rects = makeRects(room_size, min_rect_dim, max_rect_dim, rect_quant)

    #write them to csv file choose the dir set files_dir in command line
    #else file will be saved in cur dir
    ret = writeRectsToCsv(files_dir, csv_name, rects)

    if ret == 0:
        csv_full_path = os.path.join(files_dir, csv_name)
        print(" #########################################################################")
        print(" o.k.  csv file at : {}".format(csv_full_path))
        print(" #########################################################################")


if __name__ == '__main__':
    main()
