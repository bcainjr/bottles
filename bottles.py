#!/usr/bin/env python3
#
# Project 1
# 99 Bottles
#
# UMBC TDQC5
# Bruce Cain
#
# Creation of the 99 Bottles on the wall song


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
                           "No more bottles of beer on the wall!"
            print(singleBottle.format(bottle, beverage))


def main():
    bottlePrint()


if __name__ == "__main__":
    main()
