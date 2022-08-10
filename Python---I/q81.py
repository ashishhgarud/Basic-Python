# print the list after removing ("Elements") numbers which are divisible by 5 and 7 in [12,24,35,70,88,120,155].


li = [12,24,35,70,88,120,2]
print([i for i in li if i % 5 != 0 and i % 7 != 0])

# ===========================================

def isNotDiv(n, ele=[]):
    for i in n:  # for i in range(len(n)+1):
        if i % 5 != 0 and i % 7 != 0:
            ele.append(i)
    return print(ele)


li = [12,24,35,70,88,120,2]
print(isNotDiv(li))


# issue in last element 155?
