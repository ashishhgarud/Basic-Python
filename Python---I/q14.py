# accepts a sentence and calculate the number of upper case letters and lower case letters.

string = input("Enter the sentense")
upper = 0
lower = 0
for x in string:
    if x.isupper() == True:
        upper += 1
    # upper+=i.isupper()
    if x.islower() == True:
        lower += 1
    # lower+=i.islower()

print("UPPER CASE: ", upper)
print("LOWER CASE: ", lower)

# ================

word = input()
upper = sum(1 for i in word if i.isupper())           # sum function cumulatively sum up 1's if the condition is True
lower = sum(1 for i in word if i.islower())

print("UPPER CASE {0}\nLOWER CASE {1}".format(upper,lower))