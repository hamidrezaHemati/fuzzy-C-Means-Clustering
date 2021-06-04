import csv
dataFile = 'data1.csv'
import matplotlib.pyplot as plt
import numpy as np


def get_data():
    points = []
    with open(dataFile) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        col_num = len(next(csv_reader))  # Read first line and count columns
        csv_file.seek(0)  # go back to beginning of file
        for row in csv_reader:
            points.append(row)
            # print(f'{", ".join(row)}')
    print(col_num)
    points = np.array(points)  # convert 2D list to a 2D numpy array
    points = points.astype(np.float64) # cast all the elements to float from string
    return points, col_num


def main():
    points, col_num = get_data()


main()


