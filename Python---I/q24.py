# print some Python built-in functions documents
# document for your own function

import math
# print(abs.__doc__)
print(sorted.__doc__)


# print(input.__doc__)

def log_fun(n, b):
    """
    n: This is any integer number
    b: This is base of log
    return:  Logarithm base b of n = math.log(n, b)
    """

    return math.log(n, b)


print(log_fun(10, 10))
print(log_fun.__doc__)
