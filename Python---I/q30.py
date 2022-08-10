# accept two strings as input and print the string with maximum length in console. If two strings have the same length,
# then the function should print all strings line by line.
# Hints:
# Use len() function to get the length of a string.

def max_len(s1, s2):
    len_of_s1 = len(s1)
    len_of_s2 = len(s2)
    if len_of_s1 > len_of_s2:
        print(s1)
    elif len_of_s2 > len_of_s1:
        print(s2)
    else:
        print(s1)
        print(s2)


s1, s2 = input().split()
max_len(s1, s2)