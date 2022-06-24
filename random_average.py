#!/usr/bin/env python3

# Created by Samuel Webster
# Created on March 2022
# This program calculates the circumference of a circle
#     with inputted radius


import random


def main():
    # I calculate the average of randomely generated numbers

    # input
    str_repeat_number = input("How many random numbers do you want: ")

    # process & output
    try:
        int_repeat_number = int(str_repeat_number)
        random_numbers = []
        counter1 = 0
        sum = 0

        # calculate average of random numbers
        while counter1 < int_repeat_number:
            # generate random numbers
            random_numbers.append(round(random.uniform(1, 100), 2))
            sum += random_numbers[counter1]
            counter1 += 1
        average = sum / len(random_numbers)

        # output
        print("\nRandom numbers are: ", random_numbers)
        print("\nThe average is {}.".format(average))
    except Exception:
        print("\nInvalid Input")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
