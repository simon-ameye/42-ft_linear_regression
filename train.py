#!/usr/bin/python3
import os.path
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def dMeanQuadErr(X, Y, a, b):
    length = len(X)

    DMeanQuadErr_a = X * (a * X + b - Y) / length
    DMeanQuadErr_b = (a * X + b - Y) / length

    dMeanQuadErr_a = DMeanQuadErr_a.sum()
    dMeanQuadErr_b = DMeanQuadErr_b.sum()
    return [dMeanQuadErr_a, dMeanQuadErr_b]


def meanQuadErr(X, Y, a, b):
    length = len(X)
    meanQuadErr = 0

    MeanQuadErr = np.power((Y - (a * X + b)), 2)
    meanQuadErr = MeanQuadErr.sum() / float(length) / 2
    return meanQuadErr


def gradient_descent(X, Y, alpha, max_iterations):
    a = 0
    b = 0

    for i in range(0, max_iterations):
        [dMeanQuadErr_a, dMeanQuadErr_b] = dMeanQuadErr(X, Y, a, b)
        a = a - alpha * dMeanQuadErr_a
        b = b - alpha * dMeanQuadErr_b
        print("a = {0}, b = {1}, meanQuadErr = {2}".format(
            a, b, meanQuadErr(X, Y, a, b)))

    return [a, b]


def main():
    # get data
    if os.path.exists('data.csv'):
        raw_data = pd.read_csv("data.csv")
    else:
        print("data.csv not found")
        sys.exit()

    # normalize data and set matrix
    min_km = min(raw_data.km)
    max_km = max(raw_data.km)
    min_price = min(raw_data.price)
    max_price = max(raw_data.price)

    X = raw_data.km.values
    X = (X - min_km)/(max_km-min_km)

    Y = raw_data.price.values
    Y = (Y - min_price)/(max_price-min_price)

    # set gradient descent settings
    max_iterations = 1000
    alpha = 0.1

    # gradient descend
    print("dataset size = {0}".format(len(X)))
    print("Training...")
    [a, b] = gradient_descent(X, Y, alpha, max_iterations)
    print("Done !")

    # write data
    with open('values.txt', 'w') as f:
        f.write(str(a))
        f.write("\n")
        f.write(str(b))
        f.write("\n")
        f.write(str(min_km))
        f.write("\n")
        f.write(str(max_km))
        f.write("\n")
        f.write(str(min_price))
        f.write("\n")
        f.write(str(max_price))

    # plot
    fig = plt.figure("Results")
    norm_fitting = fig.add_subplot()
    norm_fitting.set_title("norm_fitting")
    norm_fitting.scatter(X, Y, color='tab:blue')
    norm_fitting.set_xlabel("norm_mileage")
    norm_fitting.set_ylabel("norm_price")
    norm_fitting.plot([0, 1], [b, a + b])
    plt.show()


if __name__ == "__main__":
    main()
