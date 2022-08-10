# list comprehension to square each odd number in a list.
# The list is input by a sequence of comma-separated numbers.

import math

values = input("Enter bunch of numbers: ")
l_for_list = values.split(",")

sq_of_odd = []
for i in l_for_list:
    if int(i) % 2 != 0:
        sq_of_odd.append(str(int(i) ** 2))
    else:
        pass
# sq_of_odd = [str(int(i)**2) for i in input().split(',') if int(i) % 2]
print(",".join(sq_of_odd))

# ===========
# from math import *  # importing all math functions

C, H = 50, 30


def calc(D):
    return sqrt((2 * C * D) / H)


D = input().split(',')  # splits in comma position and set up in list
D = [str(round(calc(int(i)))) for i in D]  # using comprehension method. It works in order of the previous code
print(",".join(D))
# print(",".join([str(int(calc(int(i)))) for i in input().split(',')]))
