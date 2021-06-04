import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

dataFile = 'data2.csv'


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


def plot(x, y, z=0):

    if z == 0:
        print("debug, col size = 2")
        plt.plot(x, y, 'rs')
        plt.show()
    else:
        print("debug, col size = 3")
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        Axes3D.scatter(ax, x, y, z, zdir='z', s=10, c=None, depthshade=True)
        plt.show()


# input: points: nested list, col_num: number of column of input data or number of dimensions
# output: return separated axis data in below form:
# if col_num is 2: return x and y axises
# if col_num is 3: return xy in zipped form and z axises
# if col_num is 4: return xy and zt axises in zipped format
def get_axis(points, col_num):
    x = [point[0] for point in points]
    y = [point[1] for point in points]
    if col_num == 2:
        return x, y
    elif col_num >= 3:
        xy = zip(x, y)
        z = [point[2] for point in points]
        if col_num == 4:
            t = [point[3] for point in points]
            zt = zip(z, t)
            return xy, zt
        return xy, z
    else:
        raise Exception("Wrong number of dimensions, CHECK DATA INPUT it shoud be between 2 and 4")


def main():
    points, col_num = get_data()
    x, y, z = get_axis(points, col_num)
    plot(x, y, z)




main()


