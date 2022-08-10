# function that can receive two integer numbers in string form and compute their sum and then print it in console.
# Hints:
# Use int() to convert a string to integer

def sum_of(s1, s2):
    print(int(s1) + int(s2))


sum_of("3", "4")

# ==========
sum = lambda s1, s2: int(s1) + int(s2)
print(sum("10", "45"))
