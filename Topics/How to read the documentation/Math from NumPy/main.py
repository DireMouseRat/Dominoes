# import the required library
from math import cos
from math import radians


def calculate_cosine(angle_in_degrees):
    # do not forget to round the result and print it
    print(round(cos(radians(angle_in_degrees)), 2))
