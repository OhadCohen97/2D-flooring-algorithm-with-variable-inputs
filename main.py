import pandas as pd
from ritzuf_room import Room
from Visualize import visualize


def main():
    # reading csv file:
    df = pd.read_csv('rects.csv')

    # insert rectangles to list
    My_Rectangles = [list(row) for row in df.values]
    print('CSV file Rectangles:{}'.format(My_Rectangles))

    rectangles = Room(My_Rectangles)
    visualize(rectangles)

if __name__ == '__main__':
    main()

