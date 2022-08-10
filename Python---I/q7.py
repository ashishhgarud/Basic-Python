# 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.

# Hint: In case of input data being supplied to the question, it should be assumed to be a console input in a comma
# separated

input_str = input('Enter comma separated numbers: ')

dimensions = [int(x) for x in input_str.split(',')]
rowNum = dimensions[0]
colNum = dimensions[1]
# in a one-liner by using list comprehension:
two_dim_array = [[0 for col in range(colNum)] for row in range(rowNum)]


for i in range(rowNum):
    for j in range(colNum):
        two_dim_array[i][j] = i * j
print(two_dim_array)



