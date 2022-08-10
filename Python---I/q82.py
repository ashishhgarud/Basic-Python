# print the list after removing the 0th, 2nd, 4th, 6th ("index") numbers in [12,24,35,70,88,120,155,189].


li = [12,24,35,70,88,120,155,189]
print ([li[i] for i in range(len(li)) if i % 2 != 0])

# ========================================

def nonEvenIndexEle(n, ele=[]):
    for i in range(len(li)):
              if i % 2 != 0:
                   ele.append(i)
    return print(ele)
          


li = [12,24,35,70,88,120,155,189]
print(nonEvenIndexEle(li))
                   
        
                   
                   
                   
