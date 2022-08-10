# a list whose elements are intersection of the above given lists.
# two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]


list1 = [1,3,6,78,35,55]
list2 = [12,24,35,24,88,120,155]
set1= set(list1)
set2= set(list2)

intersection = set1 & set2
# intersection = set.intersection(set1,set2)
print(intersection)
