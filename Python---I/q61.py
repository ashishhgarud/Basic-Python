# Compute Fibonacci Sequence: f(n) = f(n-1) + f(n-2) if n > 1, f(n) = 0 if n = 0 and f(n) = 1 if n = 1


def f(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return f(n-1) + f(n-2)


n = int(input("Enter positive integer: "))
print(f(n))
