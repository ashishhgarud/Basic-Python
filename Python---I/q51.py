# function to compute 5/0 and use try/except to catch the exceptions.
# Hints
# Use try/except to catch exceptions.


def divideByZero():
    return 5 / 0


try:
    divideByZero()
except ZeroDivisionError as ze:
    print("can't divide by zero")
