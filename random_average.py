#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


import random


def main():
    # I calculate the average of randomely generated numbers

    # process
    random_numbers = []
    counter1 = 0
    sum = 0
    # calculate average of random numbers
    while counter1 < 10:
        # generate random numbers
        random_numbers.append(round(random.uniform(1, 100), 2))
        sum += random_numbers[counter1]
        counter1 += 1
    average = sum / len(random_numbers)

    # output
    print("Random numbers are: ", end="")
    counter1 = 0
    while counter1 < 10:
        # print random numbers
        if counter1 < 9:
            print("{}".format(random_numbers[counter1]), end=", ")
        else:
            print("{}".format(random_numbers[counter1]))
        counter1 += 1
    print("The average is {}.".format(average))
    print("\nDone.")


if __name__ == "__main__":
    main()
