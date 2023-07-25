#!/usr/bin/python3
def fibonacci_sequence(n):
    if n < 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        result = [0, 1]
        while len(result) < n:
            next = result[-1] + result[-2]
            result.append(next)
        return result
