import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

dataFile = 'data4.csv'


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


def plot(points, col_num):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    if col_num == 2:
        print("debug, col size = 2")
        plt.plot(x, y, 'bs')
        plt.show()
    elif col_num == 3:
        print("debug, col size = 3")
        z = [point[2] for point in points]
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        Axes3D.scatter(ax, x, y, z, zdir='z', s=10, c=None, depthshade=True)
        plt.show()


def main():
    points, col_num = get_data()
    plot(points, col_num)




main()


