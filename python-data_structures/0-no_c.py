#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for ch in my_string:
        if ch != 'c' and ch != 'C':
            new_string = ch + new_string
    return new_string[::-1]
