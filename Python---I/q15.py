# computes the value of a+aa+aaa+aaaa with a given digit as the value of a.

a = input()
total = int(a) + int(2*a) + int(3*a) + int(4*a)  # N*a=Na, for example  a="23", 2*a="2323",3*a="232323"
print(total)

# ========

a = input()
total,tmp = 0,str()        # initialing an integer and empty string

for i in range(4):
    tmp += a               # concatenating 'a' to 'tmp'
    total += int(tmp)      # converting string type to integer type

print(total)