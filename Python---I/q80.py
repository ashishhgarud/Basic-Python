# the list after removing even ("Elements") numbers in [5,6,77,45,22,12,24].


li = [5, 6, 77, 45, 22, 12, 24, 11]
print([i for i in li if i % 2 != 0])


# ==================================

def isNotEven(n, ele=[]):
    for i in n:  # for i in range(len(n)+1):
        if i % 2 != 0:
            ele.append(i)
    return print(ele)


li = [5, 6, 77, 45, 22, 12, 24, 11]
print(isNotEven(li))
