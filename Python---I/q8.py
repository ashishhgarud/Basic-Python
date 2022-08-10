# accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting
# them alphabetically.

raw = input('Enter words: ')
items = [x for x in raw.split()]

items.sort()

print(items)