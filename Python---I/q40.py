# program which accepts a string as input to print "Yes" if the string is "yes" or "YES" or "Yes", otherwise print "No".
s = input()
if s == "yes" or s == "YES" or s == "Yes":
    print("Yes")
else:
    print("No")

# ===========

s = input()
if s.lower() == 'yes':   # lower function returns all lowercase letters in the string
    print('Yes')
else:
    print("No")
