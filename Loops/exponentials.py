# Write a program using a for loop that calculates exponentials. Your program should ask the user for a base
# (base) and an exponent (exp), and calculate base**exp without using the ** operator.

# These lines ask the user for input
base = eval(input("Base?"))
exp = eval(input("Exponent?"))

# 1. Use a for loop with a range statement to compute the final value. (Hint: think about initializing the
#    final value to 1 before the loop.

# 2. Print the fina value.
result = 1
for i in range (1,(exp+1)):
    result*=(base)
print (result)