#!/usr/bin/env python3
# Created by: Abdul
# Created on: December 10th, 2025
# This program calculates the mark for a given level using functions


def calculate(sign, first_number, second_number):
    if sign == "+":
        return first_number + second_number
    elif sign == "-":
        return first_number - second_number
    elif sign == "*":
        return first_number * second_number
    elif sign == "/":
        return first_number / second_number


def main():
    # Get and validate operation
    sign = input("Enter operation (+, -, *, /): ")
    while sign != "+" and sign != "-" and sign != "*" and sign != "/":
        print("Invalid operation.")
        sign = input("Enter operation (+, -, *, /): ")

    # Get and validate first number
    while True:
        try:
            first_number = float(input("Enter first number: "))
            break
        except ValueError:
            print("Invalid number. Try again.")

    # Get and validate second number
    while True:
        try:
            second_number = float(input("Enter second number: "))
            if sign == "/" and second_number == 0:
                print("Cannot divide by zero.")
            else:
                break
        except ValueError:
            print("Invalid number. Try again.")

    result = calculate(sign, first_number, second_number)
    print("Result:", result)


main()
