# map() to make a list whose elements are square of elements in [1,2,3,4,5,6,7,8,9,10].
# Hints:
# Use map() to generate a list.
# Use lambda to define anonymous functions.

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sqr_lst1 = [i ** 2 for i in list1]
print(sqr_lst1)

# =============
li = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squaredNumbers = map(lambda x: x ** 2, li)  # returns map type object data
print(list(squaredNumbers))  # converting the object into list
