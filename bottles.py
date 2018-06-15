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

# Moved dictionary out of function for performance, was reccomended
# by Ben Miramontes
WORD_DICTIONARY = {0: "Zero", 1: "One", 2: "Two", 3: "Three", 4: "Four",
                   5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                   10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
                   14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                   17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
                   20: "Twenty", 30: "Thirty", 40: "Fourty", 50: "Fifty",
                   60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"}


def toWord(num):
    """
        A function used to change a number to its word equivalent.
    """

    if num >= 20:
        if num % 10 == 0:
            return WORD_DICTIONARY[num - num % 10]
        else:
            return WORD_DICTIONARY[num - num % 10] + "-" \
                + WORD_DICTIONARY[num % 10].lower()
    elif num < 20:
        return WORD_DICTIONARY[num]


def bottlePrint(bottle, beverage):
    """
        A function to control how many bottles are sung
        in the bottles on the wall song.
    """
    bottlePlural = "bottles"
    bottleSingular = "bottles"

    for bottle in range(bottle, 0, -1):
        lastLine = toWord(bottle - 1)

        if bottle == 2:
            bottleSingular = "bottle"
        elif bottle == 1:
            bottlePlural = "bottle"
            bottleSingular = "bottles"
            lastLine = "No more"

        print(("{0} {1} of {3} on the wall!\n"
               "{0} {1} of {3}!\n"
               "Take one down\n"
               "And pass it around\n"
               "{4} {2} of {3} on the wall!\n"
               ).format(toWord(bottle), bottlePlural, bottleSingular, beverage,
                        lastLine))


def main():
    # Start time for performance
    start = time.time()

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
            bottlePrint(random.randint(1, 99), "beer")
        elif ans.lower() in ["n", "no"]:
            bottlePrint(99, "beer")
        else:
            print("Invalid input... Enter yes... or no...")

    # End time for performance
    end = time.time()

    print("\nPerformance: {} seconds".format(end - start))

if __name__ == "__main__":
    main()
