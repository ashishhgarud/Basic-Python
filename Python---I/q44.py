# map() to make a list whose elements are square of numbers between 1 and 20 (both included).

squaredNumbers = list(map(lambda x: x**2, range(1, 21)))
print(squaredNumbers)

# ============

def sqr(x):
    return x*x


squaredNumbers = list(map(sqr, range(1, 21)))
print(squaredNumbers)