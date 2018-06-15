#!/usr/bin/env python3
#
# Project 1
# 99 Bottles
#
# UMBC TDQC5
# Bruce Cain
#
# Creation of the 99 Bottles on the wall song


import sys
import time
import random


def bottlePrint(bottle=99, beverage="beer"):
    """
        A function to control how many bottles are sung
        in the bottles on the wall song.
    """
    bottleStr = "{0} bottles of {1} on the wall!\n"  \
                "{0} bottles of {1}!\n" \
                "Take one down\n" \
                "And pass it around\n" \
                "{2}"

    for bottle in range(bottle, 0, -1):
        if bottle > 2:
            print(bottleStr.format(bottle, beverage,
                  str(bottle - 1) + " bottles of " +
                  beverage + " on the wall!\n"))
        elif bottle == 2:
            print(bottleStr.format(bottle, beverage,
                  str(bottle - 1) + " bottle of " +
                  beverage + " on the wall!\n"))
        else:
            singleBottle = "{0} bottle of {1} on the wall!\n" \
                           "{0} bottle of {1}!\n" \
                           "Take one down\n" \
                           "And pass it around\n" \
                           "No more bottles of {1} on the wall!"
            print(singleBottle.format(bottle, beverage))


def main():
    # Start time for performance
    start = time.perf_counter()

    if len(sys.argv) == 3 and 1 <= int(sys.argv[1]) <= 99:
        bottlePrint(int(sys.argv[1]), sys.argv[2])
    elif not(len(sys.argv) == 1):
        print("Too many or too few arguements person.\n" \
              "Enter a single number between 1 and 99.\n" \
              "Followed by a beverage."
             )
    else:
        ans = input("Random # of bottles between 1 - 99 [y]es|[n]o? ")
        if ans.lower() in ["y", "yes"]:
            bottlePrint(random.randint(1, 100))
        elif ans.lower() in ["n", "no"]:
            bottlePrint()
        else:
            print("Invalid input...")

    # End time for performance
    end = time.perf_counter()

    print("\nPerformance: {} seconds".format(end - start))

if __name__ == "__main__":
    main()
