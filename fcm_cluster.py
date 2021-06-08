import csv
import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import random
from scipy.spatial import distance

dataFile = 'data5.csv'


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
    points = points.astype(np.float64)  # cast all the elements to float from string
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


def random_centre_maker(points, col_num, cluster_num):
    secure_random = random.SystemRandom()
    random_points = []
    for c in range(cluster_num):
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
    return np.array(random_points)


def sigma(point_k, c_i, centres, power):
    output = 0
    dst1 = distance.euclidean(point_k, c_i)
    for c in centres:
        dst2 = distance.euclidean(point_k, c)
        val = float(dst1 / dst2)
        val = pow(val, power)
        output += val
    return output


# update the belonging value of a point from clusters with distance between point and clusters centre points
def update_belonging_value(points, centres, cluster_num, m):
    u = np.zeros((len(points), cluster_num))
    power = float(2 / (m - 1))
    for k in range(len(points)):
        for i in range(len(centres)):
            # print("k = ", k, " i = ", i, " -->")
            belonging_value_KI = 1 / sigma(points[k], centres[i], centres, power)  # belonging value of k'th data to i'th cluster-centre
            u[k][i] = belonging_value_KI
            # print(f": تعلق داده {k} ام به خوشه {i} ام", end=" ")
            # print(belonging_value_KI)
    return u


# update the centre of each cluster using points belonging value's for each cluster
def update_cluster_centroid(points, u, v, m):
    for i in range(len(v)):
        numerator = 0
        denominator = 0
        for k in range(len(points)):
            numerator += pow(u[k][i], m) * points[k]
            denominator += pow(u[k][i], m)
        v[i] = numerator / denominator
    return v


def clustering(points, col_num):
    c = 2
    steps = 0
    m = 1.2
    while c <= 5:  # TODO: change this statement to satisfy elbow method
        print("debug C: ", c)
        v = random_centre_maker(points, col_num, c)
        while steps != 100:
            u = update_belonging_value(points, v, c, m)
            v = update_cluster_centroid(points, u, v, m)
            # for j in range(c):
            #     print(v[j], end=" ")
            # print()
            steps += 1
        steps = 0
        c += 1


def main():
    points, col_num = get_data()
    # plot(get_axis('x', points), get_axis('y', points))
    clustering(points, col_num)


main()
