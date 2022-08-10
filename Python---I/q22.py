# compute the frequency of the words from the input. The output should output after sorting the key alphanumerically.

word_freq = {}
user_input = input().split()

for q in user_input:
    word_freq[q] = word_freq.get(q, 0) + 1

word_freq = sorted(word_freq.items())

for i in word_freq:
    print("%s:%d" % (i[0], i[1]))

# =============
ss = input().split()
dict = {i: ss.count(i) for i in ss}  # sets dictionary as i-> split word & ss.count(i) -> total occurrence of i in ss
dict = sorted(dict.items())  # items() function returns both key & value of dictionary as a list
# and then sorted. The sort by default occurs in order of 1st -> 2nd key
for i in dict:
    print("%s:%d" % (i[0], i[1]))

# ==============
ss = input().split()
word = sorted(set(ss))  # split words are stored and sorted as a set

for i in word:
    print("{0}:{1}".format(i, ss.count(i)))

# ==============
from collections import Counter

ss = input().split()
ss = Counter(ss)  # returns key & frequency as a dictionary
ss = sorted(ss.items())  # returns as a tuple list

for i in ss:
    print("%s:%d" % (i[0], i[1]))
