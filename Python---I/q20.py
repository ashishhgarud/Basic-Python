# a class with a generator which can iterate the numbers, which are divisible by 7, between a given range 0 and n.
class test:
    def generator(self, n):
        return [i for i in range(n) if i % 7 == 0]


n = int(input())

num = test()
test_object = num.generator(n)

print(test_object)