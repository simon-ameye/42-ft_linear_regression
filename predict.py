#!/usr/bin/python3
import os.path
import sys


def main():
    # get thetas
    if os.path.exists('values.txt'):
        with open('values.txt') as f:
            theta1 = float(f.readline())
            theta0 = float(f.readline())
            min_km = float(f.readline())
            max_km = float(f.readline())
            min_price = float(f.readline())
            max_price = float(f.readline())
    else:
        print("thetas.csv not found, default values are used")
        theta0 = 0
        theta1 = 0
        min_km = 0
        max_km = 1
        min_price = 0
        max_price = 1

    # get input
    km = input("Input mileage: ")

    try:
        km = float(km)
    except ValueError:
        print("Wrong input : float conversion impossible")
        sys.exit()

    if km < 0:
        print("Wrong input : negative input")
        sys.exit()

    # predict
    km_norm = (km - min_km) / (max_km - min_km)
    price_norm = theta0 + theta1 * km_norm
    price = price_norm * (max_price - min_price) + min_price
    print("Estimated price : " + str(price) + "$")

if __name__ == "__main__":
    main()
