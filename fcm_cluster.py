import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random
dataFile = 'data1.csv'


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
    if col_num > 4 or col_num <= 1:
        raise Exception("Wrong number of dimensions, CHECK DATA INPUT it shoud be between 2 and 4")
    return points, col_num


def plot(x, y, z=0):
    if z == 0:
        print("debug, col size = 2")
        plt.plot(x, y, 'rs')
    else:
        print("debug, col size = 3")
        fig = plt.figure()
        ax = fig.add_subplot(111, projection='3d')
        Axes3D.scatter(ax, x, y, z, zdir='z', s=10, c=None, depthshade=True)
    plt.show()


# input: points: nested list, requested_axis: witch axis you want its data, can be x or y or z or t
# output: return the data of the requested axis
def get_axis(requested_axis, points):
    if requested_axis == 'x':
        axis = [point[0] for point in points]
    elif requested_axis == 'y':
        axis = [point[1] for point in points]
    elif requested_axis == 'z':
        axis = [point[2] for point in points]
    elif requested_axis == 't':
        axis = [point[3] for point in points]
    else:
        raise Exception("WRONG INPUT, requested input must be one of these: x,y,z,t")
    return np.array(axis)


def random_centre_maker(points, col_num, c):
    secure_random = random.SystemRandom()
    random_points = []
    for i in range(c):
        generated_point = []
        # print("x: ", get_axis('x', points).min(), get_axis('x', points).max())
        # print("y: ", get_axis('y', points).min(), get_axis('y', points).max())
        x = secure_random.uniform(get_axis('x', points).min(), get_axis('x', points).max())
        y = secure_random.uniform(get_axis('y', points).min(), get_axis('y', points).max())
        generated_point.append(x)
        generated_point.append(y)
        if col_num >= 3:
            z = secure_random.uniform(get_axis('z', points).min(), get_axis('z', points).max())
            generated_point.append(y)
        if col_num == 4:
            t = secure_random.uniform(get_axis('t', points).min(), get_axis('t', points).max())
            generated_point.append(y)
        # print(i, " point: ", x, y, z, t)
        random_points.append(generated_point)
    return random_points


def main():
    points, col_num = get_data()
    centre_points = random_centre_maker(points, col_num, 3)
    print(type(centre_points), type(centre_points[0]))
    for i in centre_points:
        print(i)


main()


