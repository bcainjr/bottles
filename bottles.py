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


def bottlePrint(bottle, beverage):
    """
        A function to control how many bottles are sung
        in the bottles on the wall song.
    """

    # BottleStr is a dictionary to help declutter prints
    # ln = singular Line and sLn = plural Line
    # 1, 2, 7 sLn contains "bottles" vs 1, 2, 7 ln contains "bottle"
    bottleStr = {"1 sLn": "{0} bottles of {1} on the wall!\n",
                 "1 ln": "{0} bottle of {1} on the wall!\n",
                 "2 sLn": "{0} bottles of {1}!\n",
                 "2 ln": "{0} bottle of {1}!\n",
                 "5 ln": "Take one down\n",
                 "6 ln": "And pass it around\n",
                 "7 sLn": "{2} bottles of {1} on the wall!\n",
                 "7 ln": "{2} bottle of {1} on the wall!\n",
                 "No bottles": "No more bottles of {1} on the wall!"
                 }

    for bottle in range(bottle, 0, -1):
        if bottle > 2:
            print((bottleStr["1 sLn"] + bottleStr["2 sLn"] +
                   bottleStr["5 ln"] + bottleStr["6 ln"] + bottleStr["7 sLn"]
                   ).format(bottle, beverage, bottle - 1))
        elif bottle == 2:
            print((bottleStr["1 sLn"] + bottleStr["1 sLn"] +
                   bottleStr["5 ln"] + bottleStr["6 ln"] + bottleStr["7 ln"]
                   ).format(bottle, beverage, bottle - 1))
        else:
            print((bottleStr["1 ln"] + bottleStr["2 ln"] + bottleStr["5 ln"] +
                   bottleStr["6 ln"] + bottleStr["No bottles"]
                   ).format(bottle, beverage, bottle - 1))


def main():
    # Start time for performance
    start = time.perf_counter()

    if len(sys.argv) == 3 and sys.argv[1].isdigit() \
       and 1 <= int(sys.argv[1]) <= 99:
        bottlePrint(int(sys.argv[1]), sys.argv[2])
    elif not(len(sys.argv) == 1):
        print("Too many or too few arguements person.\n"
              "Enter a integer between 1 and 99.\n"
              "Followed by a beverage.")
    else:
        try:
            ans = input("Random # of bottles between 1 - 99 [y]es|[n]o? ")
        except (KeyboardInterrupt, EOFError):
            print("\nYou shouldn't have done that...")
            exit()
        if ans.lower() in ["y", "yes"]:
            bottlePrint(random.randint(1, 100), "beer")
        elif ans.lower() in ["n", "no"]:
            bottlePrint(99, "beer")
        else:
            print("Invalid input...")

    # End time for performance
    end = time.perf_counter()

    print("\nPerformance: {} seconds".format(end - start))

if __name__ == "__main__":
    main()
