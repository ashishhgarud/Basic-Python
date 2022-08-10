# accepts a sequence of (comma-separated) numbers from console
# generate a list and a tuple which contains every number

values = input("Enter bunch of numbers: ")
l_for_list = values.split()
t_for_tuple = tuple(l_for_list)
print(l_for_list)
print(t_for_tuple)
