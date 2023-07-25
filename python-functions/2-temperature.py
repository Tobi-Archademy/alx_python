#!/usr/bin/python3
def convert_to_celsius(fahrenheit):
    temp = float(input(fahrenheit))
    cels = (temp - 32) * 5/9
    return cels
