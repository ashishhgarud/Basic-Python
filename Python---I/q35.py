# function which can generate a list where the values are square of numbers between 1 and 20 (both included).
# Then the function needs to print the last 5 elements in the list.
# Hints:

def sqr_lst():
    list1 = []  # list1 = list()
    for i in range(1, 21):
        list1.append(i**2)
    print(list1[-5:])  # [-5:]


sqr_lst()