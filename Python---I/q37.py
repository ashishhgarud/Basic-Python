# function which can generate and print a tuple where the value are square of numbers between 1 and 20 (both included).
# Hints:
# Use tuple() to get a tuple from a list.

def sqr_lst():
    list1 = []  # list1 = list()
    for i in range(1, 21):
        list1.append(i**2)
    print(tuple(list1))  # [:5]


sqr_lst()

# =======

def sqr_lst():
    list1 = [i ** 2 for i in range(1, 21)]
    print(tuple(list1))

sqr_lst()