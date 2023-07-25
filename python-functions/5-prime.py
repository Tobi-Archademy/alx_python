#!/usr/bin/python3
def is_prime(number):
    for i in range(1, number):
        if (number % i) == 0:
            return False
        return True
