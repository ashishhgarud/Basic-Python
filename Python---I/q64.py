# print the numbers which can be divisible by 5 and 7 between 0 and n in comma separated form while n is input by console.


def divisibleBy(n):
    i = 0
    while i <= n:
        if i % 5 == 0 and i % 7 == 0:
            yield i
        i += 1


n = int(input("Enter positive integer: "))
printOutput = [i for i in divisibleBy(n)]
print(printOutput)
       
