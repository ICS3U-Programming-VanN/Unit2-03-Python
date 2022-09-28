#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: September 27, 2022
# This program calculates and displays the circumference of a circle
# based on the input using tau (in cm).


import constants


def main():

    # Gets the radius from the user
    radius = float(input("Enter the radius of the circle (cm): "))

    # Calculates the circumference
    circumference = round(constants.TAU * radius, 2)

    # Displays the Circumference
    print(f"\nThe circumference is {circumference}cm.")


if __name__ == "__main__":
    main()
