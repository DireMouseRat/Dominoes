from math import pow


def some_calculate(a, b):
    print(abs((a % b) - int(pow(b, a))))
