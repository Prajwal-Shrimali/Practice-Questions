# Find the transpose of a given matrix using list comprehension.

l = eval(input('Enter a matrix: '))
lt = [[] for i in range(len(l))]
[lt[j].append(l[i][j]) for i in range(len(l)) for j in range(len(l[i]))]
print(lt)

# Write a Python program to find the repeated items of a tuple.

tup = eval(input('Enter a tuple: '))
sv = []
ssv = set([])
for i in tup:
    if i not in sv:
        sv.append(i)
    else:
        ssv.add(i)
print(ssv)

# Given a Python list. Turn every item of a list into its square
# input: aList = [1, 2, 3, 4, 5, 6, 7]
# output: [1, 4, 9, 16, 25, 36, 49]

print([i ** 2 for i in eval(input('Enter a list: '))])

# Write a program that reads a string and prints the letters in decreasing
# order of frequency.

string = input('Enter a string: ')
dict = {}
for i in string:
    dict[i] = string.count(i)
sl = (sorted(dict.items(), reverse = True ,key = lambda x : x[1]))
print(''.join([i[0] * i[1] for i in sl]))

# Write a program to perform row wise sum and column wise sum of a matrix and
# store the results in two separate matrices namely row_sum and column_sum

matrix = eval(input('Enter a matrix: '))

row_sum = [sum(i) for i in matrix]
column_sum = [sum([matrix[j][i] for j in range(len(matrix))]) for i in range(len(matrix))]

print(row_sum, column_sum)

# Write a program to arrange all the elements in the matrix in descending
# order.

matrix = [[1,2,3],[4,5,6],[7,8,9]]
ll = []
[ll.extend(sorted(i, reverse=True)) for i in matrix]
ll.sort(reverse=True)
sortedMatrix = []
row, column = len(matrix),len(matrix[0])
k = 0
for i in range(row):
    addRow = []
    for j in range(column):
        addRow.append(ll[k])
        k += 1
    sortedMatrix.append(addRow)
print(sortedMatrix)

# Write a program to check whether two matrices are identical.

A = eval(input('Enter the first matrix: '))
B = eval(input('Enter the second matrix: '))
if A == B:
    print('The two matrices are identical')
else:
    print('The two matrices are not identical')

# Write a Python script to generate and print a dictionary that contains a
# number (between 1 and n) in the form (x, x*x).
# Sample Dictionary ( n = 5) : Expected Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print ({i : i ** 2 for i in range(1, int(input('Enter the value of n: ')) + 1)})

# Create a dictionary with the names as keys and marks as values by user input.
# Write a Python program to sum all the marks in a dictionary and display it. 

print (sum([i for i in {input('Enter Student\'s Name: ') : int(input('Enter Student\'s Mark: ')) for k in range(int(input('Enter a number of students: ')))}.values()]))