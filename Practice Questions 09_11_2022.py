# Part A
# WAP to add two number and print the result
num1 = int(input('Enter the first number to add: '))
num2 = int(input('Enter the second number to add: '))
print('Sum:', num1 + num2)

# WAP to find the area of the triangle
side1 = int(input('Enter the length of the first side: '))
side2 = int(input('Enter the length of the second side: '))
side3 = int(input('Enter the length of the third side: '))
semiPerimeter = (side1 + side2 + side3) / 2
areaOfTriangle = pow((semiPerimeter * (semiPerimeter - side1)
                     * (semiPerimeter - side2) * (semiPerimeter - side3)), 0.5)
print('Area of Triangle', areaOfTriangle)

# WAP to find the square root of a number
number = int(input('Enter the number whose square root to be found: '))
print('Square Root', number ** 0.5)

# WAP to solve the square root of a equation
print('ax^2 + bx + c')
a, b, c = int(input('Enter value of a: ')), int(
    input('Enter value of b: ')), int(input('Enter the value of c: '))
print('Factors of the equation {}x^2 + {}x + {} are'.format(a, b, c), (-b + ((b **
      2) - 4 * a * c) ** 0.5) / (2 * a), (-b - ((b ** 2) - 4 * a * c) ** 0.5) / (2 * a))

# WAP to convert Farhenheit and Celsius
farhenheit = int(input('Enter temperature in farhenheit: '))
print((farhenheit - 32) * 5 / 9)

# WAP to print the quotient and reminder after division
dividend, divisor = int(input('Enter the dividend: ')
                        ), int(input('Enter the divisor: '))
print('The quotient and remainder for the numbers {} and {} is {} and {} respectivly'.format(
    dividend, divisor, dividend // divisor, dividend % divisor))

# WAP to swap two numbers using tuple assignment
tupleOriginal = eval(input('Enter a tuple of length 2: '))
swapedTuple = (tupleOriginal[1], tupleOriginal[0])
print('Original Values {} \nSwaped Values: {}'.format(tupleOriginal, swapedTuple))

# WAP to find the average of three marks
mark1, mark2, mark3 = int(input('Enter 1st mark: ')), int(
    input('Enter 2nd mark: ')), int(input('Enter 3ed mark:'))
print((mark1 + mark2 + mark3) / 3)

# WAP to print Simple Interest
principleAmount, interestRate, timePeriod = int(input('Enter Principle Amount: ')), int(
    input('Enter interest rate: ')), int(input('Enter time period: '))
print('Interest Amount:', principleAmount * interestRate * timePeriod / 100)

# Write a program in python to calculate the net pay given basic pay, hra, da and deductions. 
basicPay, hra, da, deductions = int(input('Enter Basic Pay: ')), int(input('Enter HRA: ')), int(input('Enter DA: ')), int(input('Enter Deductions: '))
print('Net Pay:', basicPay + hra + da - deductions)

# Part B
# Given age determine whether a person is eligible to vote or not. (if else) 
ageOfPerson = int(input('Enter the age of the person to check eligiblity: '))
if ageOfPerson >= 18:
    print(True)
else:
    print(False)

# Check whether a number is odd or even. (if else)
enteredNumber = int(input('Enter the number to check if even ot odd: '))
if enteredNumber % 2 == 0:
    print('Even')
else:
    print('Odd')

# Write a program to find largest of two numbers. (if else)
num1, num2 = int(input('Enter first number: ')), int(input('Enter second number: '))
if num1 > num2 :
    print('the first number entred {} is greater then the second number entered {}'.format(num1, num2))
else:
        print('the first number entred {} is lesser then the second number entered {}'.format(num1, num2))

# Obtain a character convert lower case to uppercase and vice versa. (if else)
print(input('Enter a charcater to toggle case: ').swapcase())

# Find the input year is leap year or not. (if else)
yearEntered = int(input('Enter the year to check if it\'s a leap year: '))
if yearEntered % 100 == 0:
    if yearEntered % 400 == 0:
        print('Leap Year')
    else:
        print('Not a Leap Year')
elif yearEntered % 4 == 0:
    print('Leap Year')
else: 
    print('Not a Leap Year')

# Read a number, check if it is positive, negative or zero. Increment the number if it is positive, decrement if it is negative. (elif statement)
numEntered = int(input('Enter a number: '))
if numEntered == 0:
    print('The number entered is ZERO')
elif numEntered > 0:
    print('The number entered is positive and its value after increment is',numEntered + 1)
else:
        print('The number entered is negative and its value after decrement is',numEntered - 1)

# Create a simple calculator. (elif statement)
while(True):
    print('---------------- Welcome User ---------------')
    print('''1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
0. Exit
Please Select A Option to Perform An Operation''')
    ch = int(input('Enter Your Choice: '))
    if ch == 1:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '+' ,y , '=', x + y)
        print()
    elif ch == 2:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '-' ,y , '=', x - y)
        print()
    elif ch == 3:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '*' ,y , '=', x * y)
        print()
    elif ch == 4:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '/' ,y , '=', x / y)
        print()
    elif ch == 0:
        print('Exiting.....')
        print()
        break
    else:
        print('Wrong Option! Option Doesn\'t Exist. Please Select A Suitable Option.')
        print()

# Estimate the Grade based on the marks obtained by a student. (elif statement)
markEntered = int(input('Enter Marks: '))
if 91 <= markEntered <= 100:
    print('A Grade')
elif 81 <= markEntered < 91:
    print('B Grade')
elif 71 <= markEntered < 81:
    print('C Grade')
elif 61 <= markEntered < 71:
    print('D Grade')
elif 51 <= markEntered < 61:
    print('E Grade')
else:
    print('F Fail')

# Find the largest of 3 numbers. (elif statement)
num1, num2, num3 = int(input('Enter first number: ')), int(input('Enter second number: ')), int(input('Enter third number: '))
if num1 > num2 and num1 > num3:
    print(num1, 'is the greatest')
elif num2 > num1 and num2 > num3:
    print(num2, 'is the greatest')
else:
    print(num3, 'is the greatest')

# Obtain a character, check if it is lower case, uppercase or digit. (elif statement)
character = input('Enter a charaacter: ')
if character.isalpha():
    if character.islower():
        print('The entered character is an alphabet and in lower case')
    elif character.isupper():
        print('The entered charecter is an alphabet and in upper case')
elif character.isdigit():
    print('The entered number is numeric')
else:
    print('The entered number is neither an alphabet nor number')


# Part C
# Write a program to check whether a number is odd or even.
enteredNumber = int(input('Enter the number to check if even ot odd: '))
if enteredNumber % 2 == 0:
    print('Even')
else:
    print('Odd')

# Write a program in python to find the biggest of two numbers.
num1, num2 = int(input('Enter first number: ')), int(input('Enter second number: '))
if num1 > num2 :
    print('the first number entred {} is greater then the second number entered {}'.format(num1, num2))
else:
        print('the first number entred {} is lesser then the second number entered {}'.format(num1, num2))

# Write a program to convert a character from lower case to uppercase and vice versa.
print(input('Enter a charcater to toggle case: ').swapcase())

# Write a program in python to find whether a number is divisible by both 5 and 7.
num = int(input('Enter a number: '))
if num % 5 == 0 and num % 7 != 0:
    print(num, 'Divisible by 5')
elif num % 7 == 0 and num % 5 != 0:
    print(num, 'Divisible by 7')
elif num % 35 == 0:
    print(num, 'Divisible by 5 and 7')

# Write a program to find the input year is leap year or not.
yearEntered = int(input('Enter the year to check if it\'s a leap year: '))
if yearEntered % 100 == 0:
    if yearEntered % 400 == 0:
        print('Leap Year')
    else:
        print('Not a Leap Year')
elif yearEntered % 4 == 0:
    print('Leap Year')
else: 
    print('Not a Leap Year')

# Write a program in python to input three sides of a triangle and check whether the triangle is equilateral, isosceles or scalene
side1 = int(input('Enter the length of the first side: '))
side2 = int(input('Enter the length of the second side: '))
side3 = int(input('Enter the length of the third side: '))
if side1 == side2 and side2 == side3:
    print('Equilateral Triangle')
elif (side1 == side2) or (side1 == side3) or (side3 == side2):
    print('Isosceles Triangle')
else:
    print('Scalene Triangle')

# Write a program in python to input three sides of a triangle and check whether it is right angled one.
side1 = int(input('Enter the length of the first side: '))
side2 = int(input('Enter the length of the second side: '))
side3 = int(input('Enter the length of the third side: '))
if side1 ** 2 == side2 ** 2 + side3 ** 2 or side2 ** 2 == side1 ** 2 + side3 ** 2 or side3 ** 2 == side1 ** 2 + side2 ** 2:
    print('The triangle is a right angle triangle')
else:
    print('The triangle isn\'t a right angle triangle')

# Read a number, check if it is positive, negative or zero. Increment the number if it is positive, decrement if it is negative.
numEntered = int(input('Enter a number: '))
if numEntered == 0:
    print('The number entered is ZERO')
elif numEntered > 0:
    print('The number entered is positive and its value after increment is',numEntered + 1)
else:
        print('The number entered is negative and its value after decrement is',numEntered - 1)

# Create a simple calculator.
while(True):
    print('---------------- Welcome User ---------------')
    print('''1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
0. Exit
Please Select A Option to Perform An Operation''')
    ch = int(input('Enter Your Choice: '))
    if ch == 1:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '+' ,y , '=', x + y)
        print()
    elif ch == 2:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '-' ,y , '=', x - y)
        print()
    elif ch == 3:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '*' ,y , '=', x * y)
        print()
    elif ch == 4:
        x = int(input('Enter a Number: '))
        y = int(input('Enter a Number: '))
        print(x, '/' ,y , '=', x / y)
        print()
    elif ch == 0:
        print('Exiting.....')
        print()
        break
    else:
        print('Wrong Option! Option Doesn\'t Exist. Please Select A Suitable Option.')
        print()

# Estimate the Grade based on the marks obtained by a student.
markEntered = int(input('Enter Marks: '))
if 91 <= markEntered <= 100:
    print('A Grade')
elif 81 <= markEntered < 91:
    print('B Grade')
elif 71 <= markEntered < 81:
    print('C Grade')
elif 61 <= markEntered < 71:
    print('D Grade')
elif 51 <= markEntered < 61:
    print('E Grade')
else:
    print('F Fail')

# Obtain a character, check if it is lower case, uppercase or digit.
character = input('Enter a charaacter: ')
if character.isalpha():
    if character.islower():
        print('The entered character is an alphabet and in lower case')
    elif character.isupper():
        print('The entered charecter is an alphabet and in upper case')
elif character.isdigit():
    print('The entered number is numeric')
else:
    print('The entered number is neither an alphabet nor number')

# Find the largest of 3 numbers.
num1, num2, num3 = int(input('Enter first number: ')), int(input('Enter second number: ')), int(input('Enter third number: '))
if num1 > num2 and num1 > num3:
    print(num1, 'is the greatest')
elif num2 > num1 and num2 > num3:
    print(num2, 'is the greatest')
else:
    print(num3, 'is the greatest')

# Obtain a input from the user and display the corresponding data types (primitive and compound data type)


# Part D
# Compute Exponentiation (power of a number) without using ** operator.
number = int(input('Enter a number: '))
square = 1
i = 1
while i <= 2:
    square *= number
    i += 1
print(square)

# Write a program in python to print all the two digit numbers which are either divisible by 3 or by 4.
num = 10
while 10 <= num <= 99:
    if num % 3 == 0 and num % 4 != 0:
        print(num, 'Divisible by 3')
    elif num % 4 == 0 and num % 3 != 0:
        print(num, 'Divisible by 4')
    elif num % 12 == 0:
        print(num, 'Divisible by 3 and 4')
    num += 1

# Write a program in python to print the sum of all the digits of a number.
number = input('Enter a number: ')
rangeOfLoop = 0
sum  = 0
while rangeOfLoop < len(number):
    sum += int(number[rangeOfLoop])
    rangeOfLoop += 1
print(sum)

# Perform the division operation and find the quotient and remainder values. (without using /, // % operators)
dividend, divisor = int(input('Enter dividend: ')), int(input('Enter divisor: '))
remainder, quotient = 0, 0
while True:
    remainder = dividend - divisor 
    quotient += 1
    dividend = remainder
    if remainder < divisor:
        break
print('The quotient is: {}\nThe remainder is: {}'.format(quotient, remainder))

# Check whether the given number is palindrome or not
number = int(input('Enter a number: '))
if number == int(str(number)[::-1]):
    print('Pallendrome')
else:
    print('Not a Pallendrome')

# Check whether the given number is Armstrong number or not
x = int(input('Enter a number to check if its an armstrong number: '))
y = list(str(x))
c = 0
i = 0
while i < len(y):
    c += int(y[i])**len(y)
    i += 1
if x == c:
    print('The Entered Number is an Armstrong Number')
else:
    print('The Entered Number is Not an Armstrong Number')

# Compute the GCD of two numbers.(Euclidean Method and using common factors)
num1, num2 = int(input('Entter first number: ')), int(input('Entter second number: '))
while True:
    remainder = num1 % num2
    if remainder == 0:
        print('The GCD is',num2)
        break
    else:
        num1 = num2
        num2 = remainder

# Take integer inputs from user until he/she presses q (Ask to press q to quit after every integer input ). Print average and product of all numbers.
prodOfVal, listOfVal = 1, []
while True:
    num = int(input('Enter the number: '))
    listOfVal.append(num)
    prodOfVal *= num
    ch = input('Do you want to quit: ')
    if ch.lower() == 'q':
        break
print('The product of the values entered is', prodOfVal)
print('The average of the values entered is', sum(listOfVal) / len(listOfVal))

# Find the square root of a number. (Newton’s method) 
num = int(input('Enter the number whose square root to be found: '))
precision = 10 ** (-10)
r = num
while abs(num - r * r) > precision:
        r = (r + num / r) / 2
print(r)


# Part E
# Write a Python program to construct the following pattern, using a nested for loop.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * * 
# *
# a)
numberOfRows = int(input('Enter the maximum number of elemets in a row: '))
topHalf = ['* ' * i for i in range(1, numberOfRows + 1)]
for i in topHalf:
    print(i)
for j in topHalf[:len(topHalf) - 1][::-1]:
    print(j)

# 1
# 2 1
# 3 2 1
# 4 3 2 1
# 5 4 3 2 1
# b)
numberOfRows = int(input('Enter the number of rows: '))
for i in range(1, numberOfRows + 1):
    for j in range(i , 0, -1):
        print(j, end = ' ')
    print()

#     1 
#    1 1
#   1 2 1
#  1 3 3 1
# 1 4 6 4 1
#1 5 10 10 5 1
# c)
from math import factorial
n = int(input('Enter the number of rows: '))
for i in range(n):
    for j in range(n-i+1):
        print(end=" ")
    for j in range(i+1):
        print(factorial(i)//(factorial(j)*factorial(i-j)), end=" ")
    print()

# 2. Write a Python program that accepts a word from the user and reverse it.
word = input('Enter a word: ')
print('Reversed Word:', word[::-1])

# 3. Write a Python program to count the number of even and odd numbers from a series of numbers.
listEntered = eval(input('Enter a list: '))
print('Even Values:', [i for i in listEntered if i % 2 == 0])
print('Odd Values:', [i for i in listEntered if i % 2 != 0])

# 4. Write a Python program that prints each item and its corresponding type from the following list.
listEntered = eval(input('Enter a list: '))
for i in listEntered:
    print('{:<20}{:<20}'.format(str(i),str(type(i))))

# 5. Write a Python program that prints all the numbers from 0 to 6 except 3 and
for i in range(0,6):
    if i != 3:
        print(i)

# 6. Write a Python program which iterates the integers from 1 to 50. For multiples of three print "Fizz" instead of the number and for the multiples of five print "Buzz". For numbers which are multiples of both three and five print "FizzBuzz".
for i in range(1,51):
    if i % 15 == 0:
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 7. Write a Python program to find numbers between 100 and 400 (both included) where each digit of a number is an even number. The numbers obtained should be printed in a comma-separated sequence.
listWithEvenNumbers = []
for i in range(1,401):
    if [0 for j in str(i) if int(j) % 2 == 0] == [0] * len(str(i)): listWithEvenNumbers.append(i)
print('Values:', ' '.join([str(i) for i in listWithEvenNumbers]))

# 8. Write a Python program to create the multiplication table (from 1 to 10) of number.
numberWhoseMultiplication = int(input('Enter the number of the multiplication: '))
for i in range(1,11):
    print(numberWhoseMultiplication, 'x', i, '=', numberWhoseMultiplication * i)

# 9. Find the sum of series:
# a. 1 + 1/2 + 1/3 + ….. + 1/N
# b. 1 + x^2/2 + x^3/3 + … x^n/n
# a)
numberOfTerms = int(input('Enter the number of the terms: '))
sumOfTerms = 0
for i in range(1,numberOfTerms + 1):
    sumOfTerms += 1 / i
print(sumOfTerms)

# b)
numberOfTerms = int(input('Enter the number of the terms: '))
x = int(input('Enter value of x: '))
sumOfTerms = 1
for i in range(2,numberOfTerms + 1):
    sumOfTerms += (x ** i) / i
print(sumOfTerms)

# 10. Classify the given number is prime or composite number. 
import math
number = int(input('Enter a number: '))
count = 0
for i in range(2, math.floor(number / 2)):
    if number % i == 0:
        count += 1
if count == 0:
    print('Prime')
else:
    print('Composite')

# Part G
# Write a user-defined function to read the marks of 5 subjects, compute the total marks scored,
# average, and grade of the student. The function should take the name and ID of the student as
# arguments and print student name, ID, total, average, and grade. Write a Python program to print
# the mark details for N students using the function.
 
import prettytable
x  = prettytable.PrettyTable()
x.field_names = ['Name', 'ID', 'Total', 'Average', 'Grade']

def gradeCalculator(marks):
    if 91 <= marks <= 100:
        return 'A'
    elif 81 <= marks < 91:
        return 'B'
    elif 71 <= marks < 81:
        return 'C'
    elif 61 <= marks < 71:
        return 'D'
    elif 51 <= marks < 61:
        return 'E'
    else:
        return 'F'

def markCalculation (name, id):
    listOfMarks = []
    for i in range(5):
        listOfMarks.append(int(input(f'Enter the marks of subject no. {i + 1}: ')))
        print()
    return [name, id, sum(listOfMarks), sum(listOfMarks) / 5, gradeCalculator(sum(listOfMarks) / 5)]

def main(n):
    for i in range(n):
        x.add_row(markCalculation(input('Enter the name of the student: '), input('Enter the id of the student: ')))
    print(x)

main(int(input('Enter the total number of students: ')))


# Write a function power(X,N) that will allow a floating-point number to be raised to an integer
# power and return the result. i.e. Y = X^N. Write a Python program to invoke the function.

def power(X,N):
    return X ** N

print(power(float(input('Enter a number: ')), int(input('Enter the integer power: '))))

# Define a function CheckOddEven(num) that checks if the num is odd or even; the function sets
# a flag accordingly and returns it. Use this function to find the sum of even and odd numbers
# separately, from a given input of N numbers.

def CheckOddEven(num):
    flag = True
    if num % 2 == 0:
        return flag
    else:
        return False

N = input('Enter a set of numbers by space seprated values: ').split()
sumOdd, sumEven = 0, 0
for i in N:
    if CheckOddEven(int(i)):
        sumEven += i
    else:
        sumOdd += i

print('Sum of odd numbers: ', sumOdd, ' and even numbers: ', sumEven)

# Define a function to find the factors of the given number as an argument. If the number is not
# given, then display the factors of the default argument.

def factors(num = 10):
    factor = [1]
    for i in range(2, num + 1):
        if num % i == 0:
            factor.append(i)
    return factor

print (factors(20))
print (factors())

# Modify the function in Qn. (1) so that it returns total marks, average and grade of a student. 

import prettytable
x  = prettytable.PrettyTable()
x.field_names = ['Total', 'Average', 'Grade']

def gradeCalculator(marks):
    if 91 <= marks <= 100:
        return 'A'
    elif 81 <= marks < 91:
        return 'B'
    elif 71 <= marks < 81:
        return 'C'
    elif 61 <= marks < 71:
        return 'D'
    elif 51 <= marks < 61:
        return 'E'
    else:
        return 'F'

def markCalculation ():
    listOfMarks = []
    for i in range(5):
        listOfMarks.append(int(input(f'Enter the marks of subject no. {i + 1}: ')))
        print()
    return [sum(listOfMarks), sum(listOfMarks) / 5, gradeCalculator(sum(listOfMarks) / 5)]

def main(n):
    for i in range(n):
        x.add_row(markCalculation())
    print(x)

main(int(input('Enter the total number of students: ')))

# # Part H
# # Calculate factorial of a given number using recursive function. The base case should handle the
# # negative integers by printing an error message and returns none to indicate that something went
# # wrong.

def factorial(n):
  if n < 0:
    print("Error: factorial is not defined for negative integers")
    return None
  elif n == 0:
    return 1
  else:
    return n * factorial(n-1)

print(factorial(int(input('Enter the number of which factorial is to be found: '))))

# Compute the sum of the digits of a given number using recursion.

def sum_digits(n):
  if n < 10:
    return n
  else:
    last_digit = n % 10  
    rest_of_number = n // 10  
    return last_digit + sum_digits(rest_of_number)

print (sum_digits(int(input('Enter the numbe whose sum of digits is to be computed: '))))

# Check whether a given number is prime or not using recursive function.

def is_prime(n, divisor=2):
  if n < 2:
    return False
  elif n == 2:
    return True
  elif n % divisor == 0:
    return False
  elif divisor ** 2 > n:
    return True
  else:
    return is_prime(n, divisor + 1)

print(is_prime(int(input('Enter the number to check for prime: '))))

# The greatest common divisor (GCD) of a and b is the largest number that divides both of them
# with no remainder. One way to find the GCD of two numbers is based on the observation that if r is
# the remainder when a is divided by b, then gcd(a, b) = gcd(b, r). As a base case, we can use
# gcd(a, 0) = a. Write a recursive function called gcd that takes parameters a and b and returns their
# greatest common divisor.

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a % b)

print(gcd(int(input('Enter first number:'))), int(input('Enter second number:')))

# The Ackermann function, A(m, n) is defined as follows:
# Solve the above problem recursively for different values of m and n. 

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m-1, 1)
    elif m > 0 and n > 0:
        return ackermann(m-1, ackermann(m, n-1))

print(ackermann(int(input('Enter the value of m in ackermann function: ')), int(input('Enter the value of n in ackermann function: '))))

# Part I
# Define a function to count the number of occurrences of a substring in a given string
# and print the starting index of the substring for each occurrence.

import re
string = input('Enter the string: ')
subString = input('Enter the substring: ')
countSubstring = string.count(subString)
if countSubstring != 0:
    print ('The number of occurance of the given substring is: ', countSubstring)
    print('The substring is present in the string at position ', end= '\n')
    for i in range(len(string)):
        if string[i] == subString: print(i, end = ' ')
    print()
else:
    print('Substring not found')

# Encrypt a given message by “rotating” each letter by a fixed number of places. To
# rotate a letter means to shift it through the alphabet, wrapping around to the beginning if
# necessary, so 'A' rotated by 3 is 'D' and 'Z' rotated by 1 is 'A'. Write a function called
# rotate_word that takes a string and an integer as parameters, and returns a new string that
# contains the letters from the original string rotated by the given amount. E.g Given
# String: HAL Encrypted String: JCN (Rotated by 2)

string = input('Enter a string to rotate: ')
rotation = int(input('Enter a rotation integer: '))
print(''.join([chr(ord(i) + rotation) for i in string]))


# Write a user-defined function to check whether a given text is palindrome or not using
# string slice method.

def checkPalindrome(s):
    if s[::-1] == s:
        return True
    else:
        return False

print(checkPalindrome(input('Enter a string to check the palindrome: ')))

# Write a function strip_characters(str,chars) which removes the characters mentioned
# in chars from the string str. E.g strip_characters('The quick brown fox jumps over the
# lazy dog','aeiou') output 'Th qck brwn fx jmps' 

def strip_characters(str, chars):
    l = []
    for i in str:
        if i in chars:
            pass
        else:
            l.append(i)
    return ''.join(l)

print(strip_characters(input('Enter a string: '), input('Enter the characters to strip: ')))

# Part J
# Read a list of elements from the user and perform the following operations using functions:
# search(key): to find the given key in the list and display the position of the key if found, otherwise
# display appropriate message, maximum(Lst) and minimum(Lst) to find the maximum and minimum
# number respectively from the list.

mainList = eval(input('Enter a list of characters: '))
keyValue = eval(input('Enter the key to search: '))
def search(list, key):
    if key in list:
        return 'The key is present in the list at position' + str(list.index(key))
    else:
        return 'Key not in list'

def maximum(list):
    max  = list[0]
    for i in list:
        if i > max:
            max = i
    return max

def minimum(list):
    min = list[0]
    for i in list:
        if i < min:
            min = i
    return min

print (search(mainList, keyValue))
print(maximum(mainList))
print(minimum(mainList))

# Two words are anagrams if you can rearrange the letters from one word to spell the other. Write a
# function called is_anagram that takes two strings and returns True if they are anagrams.

from collections import Counter
def is_anagram(s1,s2):
    s1Counter = Counter(s1.lower())
    s2Counter = Counter(s2.lower())

    for key in s2Counter:
        if key not in s1Counter:
            return False
        if s1Counter[key] > s2Counter[key]:
            return False
    return True

print(is_anagram(input('Enter main string: '), input('Enter string to check for anagrams: ')))

# Write a function sorted that takes a list as a parameter and sort the elements in lexicographical
# order. Test the function for a list of names and print the sorted list.

def sortInLexicographicalOrder(list):
    list.sort()
    return list

list = eval(input('Enter a list to sort in lexicographical order: '))
print(sortInLexicographicalOrder(list))

# A list of students registered for Python course. Perform the following operations (use inbuilt
# functions) and print the output:
# i. A new student registered for the course.
# ii. Count the number of students registered for the course.
# iii. Modify a name in the list.
# iv. Sort the name list.
# v. Insert a new student name in a given position.
# vi. Search for a student.
# vii. Remove a given name from the list.

listOfStudents = []
def addNewStudent(student):
    listOfStudents.append(student)

def numberOfStudentRegistered():
    return len(listOfStudents)

def alterValue(student, alteredName):
    listOfStudent[listOfStudents.index(student)] = alteredName

def sortAlphabetically():
    return sorted(listOfStudent)

def addNewStudentAtPosition(student, position):
    listOfStudents.insert(position - 1 , student)

def searchForStudent(student):
    try:
        return listOfStudents.index(student) + 1
    except IndexError:
        return 'The student does not exist'

def removeStudent(student):
    listOfStudents.remove(student)

while True:
    print('''-----------------Welcome to the Portal-----------------
    1 - Add new student name
    2 - Count the number of students
    3 - Alter a name in the registered students
    4 - Display the name of the student alphabetically
    5 - Add a new student name at a specific position
    6 - Search for a student
    7 - Remove a student
    0 - Exit the portal''')
    ch = input('Enter your choice: ')
    if ch == '1':
        addNewStudent(input('Enter new student\'s name: '))
    elif ch == '2':
        print(numberOfStudentRegistered())
    elif ch == '3':
        alterValue(input('Enter the original name of the student: '), input('Enter the altered name of the student: '))
    elif ch == '4':
        print(sortAlphabetically())
    elif ch == '5':
        addNewStudentAtPosition(input('Enter new student name: '), int(input('Enter position at which to add the student name: ')))
    elif ch == '6':
        print(searchForStudent(input('Enter the name of the student to search for: ')))
    elif ch == '7':
        removeStudent(input('Enter the name of the student to remove: '))
    elif ch == '0':
        print('Exiting...')
        break
    else:
        print('Wrong option selected')

# Consider a tuple as T = (1, 3, 2, 4, 6, 5). Write a program to store numbers present at odd index
# into a new tuple.

T = (1, 3, 2, 4, 6, 5)
oddTuple = ()
for i in range(len(T)):
    if i % 2 != 0:
        oddTuple += T[i],

print(oddTuple)

# Consider a list containing food items. Another list contains its corresponding price. Create
# these two lists by getting the input from user. Now get the items ordered by the customer in a
# tuple. Display the total cost of the ordered food.
# Example:
# Available Fruits: Oranges, Mangoes, Apple, Grapes,
# Papaya Price per Kg: 60, 80, 220, 80, 90
# Your order (in Kgs): 2, 0, 1, 0, 0.500 
# Total Amount: Rs. 385

availableFruits =  [input(f'Enter fruit no. {i+1}: ') for i in range(int(input('Enter the total no. of available fruits: ')))]
pricePerKg = [int(input(f'Enter the price per kg for {availableFruits[i]}: ')) for i in range(len(availableFruits))]
itemWeight = [float(input(f'Enter the item weight for {availableFruits[i]}: ')) for i in range(len(availableFruits))]
print (sum([(pricePerKg[i] * itemWeight[i]) for i in range(len(availableFruits))]))

# Part K
# Matrix is a rectangular array of data or numbers. The horizontal entries in a matrix are called as
# 'rows' while the vertical entries are called as 'columns'. If a matrix has r number of rows and c
# number of columns, then the order of matrix is given by r X c. Get the values of r and c from the user.
# Write a function to create and return the r X c matrix with the user input. Write another function to
# print the sums of each row.

r = int(input('Enter the number of rows: '))
c = int(input('Enter the number of columns: '))

def addValues(r,c):
    global matrix
    matrix = [[0 for j in range(c)] for i in range(r)]

    for i in range(r):
        for j in range(c):
            matrix[i][j] += int(input(f'Enter the value a{i + 1}{j + 1}: '))

    return matrix

def sumOfRows(matrix):
    for j in range(len(matrix)):
        print(f'The sum of row no. {j + 1} is: ', sum(matrix[j]))

sumOfRows(addValues(r, c))

# 2) Find the transpose of a given matrix using list comprehension.

l = eval(input('Enter a matrix: '))
lt = [[] for i in range(len(l))]
[lt[j].append(l[i][j]) for i in range(len(l)) for j in range(len(l[i]))]
print(lt)

# 3) For two matrices A and B, compute A+B and A*B. Show your answer with and without list
# comprehension. 

A = eval(input('Enter matrix A: '))
B = eval(input('Enter matrix B: '))

# With List Comprehension
# Compute the sum of A and B
sum_matrix = [[A[i][j] + B[i][j] for j in range(len(A[i]))] for i in range(len(A))]

print(sum_matrix)

# Compute the product of A and B
product_matrix = [[sum(A[i][k] * B[k][j] for k in range(len(B))) for j in range(len(B[0]))] for i in range(len(A))]

print(product_matrix) 

# Without List Compression
# Compute the sum of A and B
sum_matrix = []
for i in range(len(A)):
  sum_row = []
  for j in range(len(A[i])):
    sum_row.append(A[i][j] + B[i][j])
  sum_matrix.append(sum_row)

print(sum_matrix)  

# Compute the product of A and B
product_matrix = []
for i in range(len(A)):
  product_row = []
  for j in range(len(B[0])):
    product = 0
    for k in range(len(B)):
      product += A[i][k] * B[k][j]
    product_row.append(product)
  product_matrix.append(product_row)

print(product_matrix)  

# Part L
# Write a user-defined function to print and store squares of numbers for the given range into a
# dictionary. Example: For range 2 to N (both inclusive): If N = 5, the contents of the dictionary
# would be {2: 4, 3: 9, 4: 16, 5: 25}

def dictionaryFactorial(N):
    return {i : i ** 2 for i in range(2,N + 1)}

print (dictionaryFactorial(int(input('Enter till which number to get facorials for: '))))

# Write a function named reverseLookup that finds all of the keys in a dictionary that map to a
# specific value. The function will take the dictionary and the value to search as arguments. It will return
# a (possibly empty) list of keys from the dictionary that map to the provided value. Show that the
# reverseLookup function works correctly when it returns multiple keys, a single key, or no keys. 


def reverseLookup(dictionary, value):
    l = []
    for i,j in dictionary.items():
        if j == value:
            l.append(i)
    return l,value

output = reverseLookup(dictionary = eval(input('Enter a dictionary: ')), value = input('Enter the value to reverse lookedup: '))

print(f'The key value(s) for {output[1]} is/are {output[0]}')

# Create a new dictionary by combining two dictionaries whose key-value pairs are given.
# The new dictionary has to be created by adding values for common keys from the two
# dictionaries.

dict1 = {'A': 100, 'B': 200, 'C':300}
dict2 = {'A': 300, 'B': 500, 'D':400}
dictSum = {}

for key, value in dict1.items():
    if key in dict2:
        dictSum[key] = value + dict2[key]
    else:
        dictSum[key] = value

for key, value in dict2.items():
    if key not in dictSum:
        dictSum[key] = value 

print (dictSum)

# In the game of Scrabble, each letter has points associated with it. The total score of a word is the
# sum of the scores of its letters. More common letters are worth fewer points while less common letters
# are worth more points. The points associated with each letter are shown below:

d = {1: 'AEILNORSTU', 2: 'DG', 3: 'BCMP', 4: 'FHVWY', 5: 'K', 8: 'JX', 10: 'QZ'}

s = input('Enter a word to check scrabble score: ').upper()
score = 0
for i in s:
    for j,k in d.items():
        if i in k:
            score += j

print(score)