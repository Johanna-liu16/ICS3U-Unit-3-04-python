#!/usr/bin/env python3

# Created by: Johanna Liu
# Created on: Oct 2022
# This program identifies an integer


def main():
    # this program identifies an integer

    # input
    print("Integer identifier.")
    user_integer = int(input("Enter an integer: "))

    # process

    if user_integer > 0:
        print("{0} is a positive integer.".format(user_integer))
    elif user_integer < 0:
        print("{0} is a negative integer".format(user_integer))
    else:
        print("{0} is zero.".format(user_integer))

    # output
    print("\nDone.")


if __name__ == "__main__":
    main()
