from collections import namedtuple
import numpy as np

# creating a subclass of rectangle object Named Tuple with different fields
Rectangle = namedtuple('Rectangle', ['x', 'y', 'w', 'h'])

def Room(rectangles):
    # Rotate rectangles:
    for idx, r in enumerate(rectangles):
        if r[0] < r[1]:  # if height > width
            # Rotate between height and width
            rectangles[idx][0], rectangles[idx][1] = rectangles[idx][1], rectangles[idx][0]
    print('Rectangles after rotations:{}'.format(rectangles))

    # sorting the indices by width ,in descending order
    sorted_indices = sorted(range(len(rectangles)), key=lambda x: -rectangles[x][0])
    print('Rectangles after sorted indices:{}'.format(sorted_indices))

    # sorting the rectangles
    sorted_rect = [rectangles[idx] for idx in sorted_indices]
    # getting the sorted list rects by their width and index
    print('Rectangles after sorted width:{}'.format(sorted_rect))

    # room size 10mx10m:
    width = 1000
    height = 1000
    room_map = np.full((width, height), 1)  # Matrix demonstrating the room filled with 1
    x, y = 0, 0
    move_right = 0
    while sorted_indices:
        idx = sorted_indices.pop(0)
        rec_wid, rec_hig = rectangles[idx]  # rec_wid[0] , rec_hig[1]
        rectangles[idx] = Rectangle(x, y, rec_wid, rec_hig)  # defining a whole new Rectangle based Named Tuple
        matrix = np.full((rec_hig, rec_wid),0)  # creating a matrix that demonstrating the rectangle[idx], filled with 0

        # [low_y : high_y, low_x : high_x]
        room_map[y: y + rec_hig, x: x + rec_wid] *= matrix  # covering a new area in the room with 0
        if y + rec_hig <= height - rec_wid and room_map[y + rec_hig][x] == 1:  # check if we got empty area to fill up
            y = y + rec_hig  # moving up
        else:
            if x + rec_wid <= width - rec_wid and room_map[y][x + rec_wid] == 1:
                flag = False
                find = 0
                while not flag:
                    for i in sorted_rect:  # finding matched rectangle to fill the top
                        if i[0] == rec_wid and i[1] == height - find:  # if we at the top and found matched rectangle
                            rectangles[idx] = Rectangle(x, y, i[0], i[1])  # setting a new rectangle
                            matrix = np.full((i[1], i[0]), 0)  # setting a new rectangle area
                            room_map[y: y + i[1], x: x + i[0]] *= matrix  # covering a specific area
                            flag = True
                            break
                    if not flag:  # if not found a specific rectangle
                        find += 10  # adding more 10cm in order to find the matched rectangle
                x += move_right  # moving right
                move_right = rec_wid
                y = 0  # setting y to zero in order to start a new column
    print('Rectangles parameters after algorithm:{}'.format(rectangles))
    print('The remaining room area after floor flooring:{}cm'.format(room_map.sum()))
    return rectangles
