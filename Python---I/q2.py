# the factorial of a given number
# results should be printed in a comma-separated sequence on a single line

"""This is a recursive function that calls
   itself to find the factorial of given number"""


def factorial(num1):
    if num1 == 1:
        return 1
    else:
        return num1 * factorial(num1 - 1)


num = int(input("Enter a number: "))
print("The factorial of", num, "is:", factorial(num))

# for 'Zero' 0:
# for 'Negative number':
