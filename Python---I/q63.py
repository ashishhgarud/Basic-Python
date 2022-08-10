# print the even numbers between 0 and n in comma separated form while n is input by console.


def evenGenerator(n):
    i = 0
    while i <= n:
        if i%2 == 0:
            yield i
        i += 1


n = int(input("Enter positive integer: "))
printEven = [i for i in evenGenerator(n)]
print(printEven)
