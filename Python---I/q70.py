# output a random even number between 0 and 10 inclusive
# using random module and list comprehension.


import random
print(random.choice([i for i in range(0,11,2)]))
# print(random.choice([i for i in range(11) if i%2 == 0]))
