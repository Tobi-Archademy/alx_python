#!/usr/bin/python3
def safe_print_division(a, b):
    result = a / b
    try:
        if result == 0:
            print("Inside result: None")     
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    finally:
        print("Inside result: {}".format(result))
