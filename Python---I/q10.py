# accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and
# sorting them alphanumerically.

input_words = input("type whitespace words: ")
words = input_words.split(" , ")
# words = [x for x in input("type whitespace words: ").split(" , ")]

print(words)
words.sort()
# words = sorted(list(set(input("type whitespace words: ").split(" , "))))

print('_'.join(words))


