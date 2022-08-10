# to print this list after removing all duplicate values with original order reserved
# list [12,24,35,24,88,120,155,88,120,155]


def removeDuplicate(inputList):
    seen = [] # seen = {} # seen = set()
    outputList = []
    for i in inputList:
        if i not in seen:
            seen.append(i)
            outputList.append(i)
    return outputList


print(removeDuplicate([12,24,35,24,88,120,155,88,120,155]))           
