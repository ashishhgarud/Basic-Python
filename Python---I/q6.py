# calculates and prints the value according to the given formula:
#   Q = Square root of [(2 * c1 * v)/c2]
#       c1 = 50, c2 = 30
# 'v' is the variable whose values should be input in a (comma-separated) sequence
import math

con1 = 50
con2 = 30

d_values = input("Enter bunch of numbers: ")
d_list = d_values.split(",")

fun_values = []
for d in d_list:
    fun_values.append(str(round(math.sqrt((2*con1*int(d) / con2)))))

# fun_values = [str(round(math.sqrt((2*con1*int(i) / con2)))) for i in input().split(",")]
print(",".join(fun_values))


