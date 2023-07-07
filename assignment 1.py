#Programs on selection and Iteration operations. 
#Get an integer input from a user. If the number is odd, then find the factorial of a number and find the number of digits in the factorial of the number. If the number is even, then check the given number is palindrome or not. 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def is_palindrome(num):
    num = str(num)
    return num == num[::-1]


def count_digits(num):
    return len(str(num))
# Get input from the user
num = int(input("Enter an integer: "))

# Check if the number is odd or even
if num % 2 == 1:
    fact = factorial(num)
    digit_count = count_digits(fact)
    print("Factorial:", fact)
    print("Number of digits in factorial:", digit_count)
else:
    if is_palindrome(num):
        print("The number is a palindrome.")
    else:
        print("The number is not a palindrome.")
        
#Strings and its operations. 
#Given two strings, PRINT (YES or NO) whether the second string can be obtained from the first by deletion of none, one or more characters.
def can_obtain_string(string1, string2):
    i = 0
    j = 0

    while i < len(string1) and j < len(string2):
        if string1[i] == string2[j]:
            j += 1
        i += 1

    return j == len(string2)


# Get input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the second string can be obtained from the first
if can_obtain_string(string1, string2):
    print("YES")
else:
    print("NO")
def can_obtain_string(string1, string2):
    i = 0
    j = 0

    while i < len(string1) and j < len(string2):
        if string1[i] == string2[j]:
            j += 1
        i += 1

    return j == len(string2)


# Get input from the user
string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Check if the second string can be obtained from the first
if can_obtain_string(string1, string2):
    print("YES")
else:
    print("NO")





    
#List and its operations
#a) Programs for negative and positive indexing
def indexing_demo(lst):
    # Accessing elements using positive indexing
    print("Positive indexing:")
    for i in range(len(lst)):
        print("Element at index", i, ":", lst[i])

    # Accessing elements using negative indexing
    print("\nNegative indexing:")
    for i in range(-1, -len(lst) - 1, -1):
        print("Element at index", i, ":", lst[i])
#b)Program to check if the given list is ascending order or not
def is_ascending(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True


# Get input from the user
input_list = input("Enter a list of numbers (space-separated): ").split()
numbers = [int(num) for num in input_list]

# Check if the list is in ascending order
if is_ascending(numbers):
    print("The list is in ascending order.")
else:
    print("The list is not in ascending order.")




#tuples and its operations
#a)  Python program to convert a tuple to a string
def tuple_to_string(tup):
    string = ''.join(tup)
    return string


# Example usage
my_tuple = ('H', 'e', 'l', 'l', 'o')
result = tuple_to_string(my_tuple)
print("Converted string:", result)



#b) Python program to reverse a tuple
def reverse_tuple(tup):
    reversed_tuple = tuple(reversed(tup))
    return reversed_tuple


# Example usage
my_tuple = (1, 2, 3, 4, 5)
result = reverse_tuple(my_tuple)
print("Reversed tuple:", result)




#Sets and its operations. 
#Python program to check if a set is a subset of another set.
def is_subset(set1, set2):
    return set1.issubset(set2)


# Example usage
set1 = {1, 2, 3}
set2 = {1, 2, 3, 4, 5}
result = is_subset(set1, set2)

if result:
    print("set1 is a subset of set2.")
else:
    print("set1 is not a subset of set2.")










#Dictionaries and its operations. 
#Python program to iterate over dictionaries using for loops.
# Dictionary of student grades
grades = {'Alice': 85, 'Bob': 90, 'Charlie': 78, 'David': 92}

# Iterating over keys
print("Iterating over keys:")
for key in grades:
    print(key)

# Iterating over values
print("\nIterating over values:")
for value in grades.values():
    print(value)

# Iterating over key-value pairs
print("\nIterating over key-value pairs:")
for key, value in grades.items():
    print(key, "->", value)

#Computing using numpy functions
#a)Numpy program to convert a list of numeric values into a one dimensional NumPy array.
import numpy as np
l = list(map(float, input("Type number with space: ").split()))
print("Original List:",l)
a = np.array(l)
print("One-dimensional NumPy array: ",a)

#Example usage
Type number with space: 1.1 2 3.3
Original List: [1.1, 2.0, 3.3]
One-dimensional NumPy array: [1.1 2. 3.3]

#b)NumPy program to convert a list and tuple into arrays.
import numpy as np
lst = list(map(float, input("Type number with space (list): ").split()))
print("Original List: ",lst)
print("List to array conversion: ")
print(np.asarray(lst))
tup= tuple(map(float, input("Type number with space (Tuple): ").split()))
print("Original Tuple: ",tup)
print("Tuple to array: ")
print(np.asarray(tup))

#Example usage
Type number with space (list): 12 45 99 75
Original List:  [12.0, 45.0, 99.0, 75.0]
List to array conversion: 
[12. 45. 99. 75.]
Type number with space (Tuple): 66 33 21 90 54
Original Tuple:  (66.0, 33.0, 21.0, 90.0, 54.0)
Tuple to array: 
[66. 33. 21. 90. 54.]

#Data Manipulation using Pandas
#a)Program to convert a NumPy array and series to data frames.
arr = np.random.rand(3) #to create an one dimensional array 
print("Numpy array:")
print(arr)
#conversion of array to dataframe
d = pd.DataFrame(series,columns =['A'])
print("\nArray to DataFrame: ")
#conversion of array to series
series = pd.Series(arr)
print("Series : ")
display(series)
# conversion of series to dataframe
df = pd.DataFrame(series,columns =['A'])
print("\nSeries to DataFrame: ")
df


#b)Program to add,subtract,multiple and divide into Pandas Series
import pandas as pd
ds1 = pd.Series([12, 45, 6, 81, 10])
ds2 = pd.Series([1, 3, 5, 7, 9])
ds = ds1 + ds2
print("Addition of two Series:")
print(ds)
print("Subtraction of two Series:")
ds = ds1 - ds2
print(ds)
print("Multiplication of two Series:")
ds = ds1 * ds2
print(ds)
print("Division of Series1 by Series2:")
ds = ds1 / ds2
print(ds)

#Example usage
Addition of two Series:
0    13
1    48
2    11
3    88
4    19
 
Subtraction of two Series:
0    11
1    42
2     1
3    74
4     1
 
Multiplication of two Series:
0     12
1    135
2     30
3    567
4     90
Division of Series1 by Series2:
0    12.000000
1    15.000000
2     1.200000
3    11.571429
4     1.111111


 
