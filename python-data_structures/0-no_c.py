#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for ch in my_string:
        if ch != "c" and ch != "C":
            new_string = new_string.join(my_string)
    return new_string
