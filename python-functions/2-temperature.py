#!/usr/bin/python3
def convert_to_celsius(fahrenheit):
    try:
        temp = float(input(fahrenheit))
        cels = (temp - 32) * 5/9
    except EOFError as e:
        print(e)
    return cels
