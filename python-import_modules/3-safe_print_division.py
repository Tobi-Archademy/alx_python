#!/usr/bin/python3
def safe_print_division(a, b):
    try:
        result = a / b
        if result == 0:
            print("Inside result: None")
    finally:
        print("Inside result: {}".format(result))
