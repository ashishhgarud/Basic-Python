# given number range divisible by and multiple of
# result in a comma-separated sequence on a single line
l_list = []
for i in range(2000, 3200):
    if (i % 7 == 0) and (i % 5 != 0):
        l_list.append(str(i))
print(l_list)
print(" ")
