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


def numToWord(num):
    """
        A function used to change a number to its word equivalent.
    """

    wordDict = {1: "One", 2: "Two", 3: "Three", 4: "Four",
                5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine",
                10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
                14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
                17: "Seventeen", 18: "Eighteen", 19: "Nineteen",
                20: "Twenty", 30: "Thirty", 40: "Fourty", 50: "Fifty",
                60: "Sixty", 70: "Seventy", 80: "Eighty", 90: "Ninety"
                }

    if num >= 20:
        if num % 10 == 0:
            return wordDict[num - num % 10]
        else:
            return wordDict[num - num % 10] + "-" + wordDict[num % 10].lower()
    elif num < 20:
        return wordDict[num]


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
                   ).format(numToWord(bottle), beverage,
                            numToWord(bottle - 1)))
        elif bottle == 2:
            print((bottleStr["1 sLn"] + bottleStr["1 sLn"] +
                   bottleStr["5 ln"] + bottleStr["6 ln"] + bottleStr["7 ln"]
                   ).format(numToWord(bottle), beverage,
                            numToWord(bottle - 1)))
        else:
            print((bottleStr["1 ln"] + bottleStr["2 ln"] + bottleStr["5 ln"] +
                   bottleStr["6 ln"] + bottleStr["No bottles"]
                   ).format(numToWord(bottle), beverage,
                            numToWord(bottle - 1)))


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
            bottlePrint(random.randint(1, 99), "beer")
        elif ans.lower() in ["n", "no"]:
            bottlePrint(99, "beer")
        else:
            print("Invalid input... Enter yes... or no...")

    # End time for performance
    end = time.perf_counter()

    print("\nPerformance: {} seconds".format(end - start))

if __name__ == "__main__":
    main()
