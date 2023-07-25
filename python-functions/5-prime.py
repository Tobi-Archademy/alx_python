#!/usr/bin/python3
def is_prime(number):
    for i in range(number):
        if (number % i) == 0:
            return False
        return True
