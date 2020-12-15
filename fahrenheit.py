#!/usr/bin/env python3

# Created by: Jonathan Pasco-Arnone
# Created on: December 2020
# This program converts fahrenheit to celsius


def temperature():
    # This function converts fahrenheit to celsius

    fahrenheit = 0
    print("")
    print("This program calculates the fahrenheit from celsius")
    print("")
    celsius_str = input("Please input the celsius: ")
    print("")

    try:
        celsius = int(celsius_str)
    except Exception:
        print("Please input a number, and have it be positive")
    else:
        if (celsius > 0):
            fahrenheit = (9/5)*celsius+32
            print("The fahrenheit is {}".format(fahrenheit))
        else:
            print("Please input a positive value")


def main():
    # This function calls the the specified functions

    temperature()


if __name__ == "__main__":
    main()
