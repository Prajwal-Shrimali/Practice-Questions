# Create a list of first 5 even numbers using list comprehension.

print ([(i + 1) * 2 for i in range(5)])

# Write a Python program to Multiply every element of a list by five and assign
# it to a new list using list comprehension.

list = [1, 2, 3, 4, 5]
print ([i * 5 for i in list])

# Write a program using list comprehension to extract and print all the numbers
# from a given string.

print ([i for i in input('Enter a string: ') if i.isdigit()])

# Write a Python program to MAtrix addition and Multiplication using list
# comprehension

A = eval(input('Enter matrix A: '))
B = eval(input('Enter matrix B: '))

# Compute the sum of A and B
sum_matrix = [[A[i][j] + B[i][j] for j in range(len(A[i]))] for i in range(len(A))]

print(sum_matrix)

# Compute the product of A and B
product_matrix = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

print(product_matrix) 

# Write a Python program to create a new list of Numbers that are divisible by
# 7 from all the numbers in the range of 1-1000.

print ([i for i in range(7,1001,7)])