def square(num):
    return num ** 2

print square(2)
print square(3)

# =====
n=int(input())
print(n**2)

# ======
def power(n):
    return lambda a: a ** n


number = power(2)

print(number(11))

# ===
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))