# accepts a sequence of words separated by whitespace as input to print the words composed of digits only.
#


userInput = input("Enter sequence of words separated by whitespace: ").split()
printOutput = []
for i in userInput:
    if i.isdigit():
        printOutput.append(i)
# printOutput = [i for i in userInput if i.isdigit()]
print(printOutput)


