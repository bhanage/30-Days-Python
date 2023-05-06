# tuple operations
# Exercise 1: Reverse the tuple
# Given:
tuple1 = (10, 20, 30, 40, 50)
# Expected output:

# (50, 40, 30, 20, 10)
print(tuple1[::-1])
# 3
# Exercise 2: Access value 20 from the tuple
# The given tuple is a nested tuple. write a Python program to print the value 20.

# Given:

tuple1 = ("Orange", [10, 20, 30], (5, 15, 25))
# Expected output:

# 20
print(tuple1[1][1])
# 3

# Exercise 3: Create a tuple with single item 50

tuple12 = (50,)
print(tuple12)
############################################################################################
# Exercise 4: Unpack the tuple into 4 variables
# Write a program to unpack the following tuple into four variables and display each variable.

# Given:

tuple1 = (10, 20, 30, 40)
a, b, c, d = tuple1
print("a:", a, "\tb:", b, "\tc:", c, "\td:", d)
##############################################################################################
# Exercise 5: Swap two tuples in Python
# Given:

tuple1 = (11, 22)
tuple2 = (99, 88)

# Expected output:

# tuple1: (99, 88)
# tuple2: (11, 22)
tuple1, tuple2 = tuple2, tuple1
print("tuple1:", tuple1)
print("tuple2:", tuple2)
##############################################################################################
# Exercise 6: Copy specific elements from one tuple to a new tuple
# Write a program to copy elements 44 and 55 from the following tuple into a new tuple.

# Given:

tuple1 = (11, 22, 33, 44, 55, 66)
# Expected output:

# tuple2: (44, 55)
tuple2 = tuple1[-3:-1]
#tuple1[3:5]
print(tuple2)
##############################################################################################
# Exercise 7: Modify the tuple
# Given is a nested tuple. Write a program to modify 
# the first item (22) of a list inside a following tuple to 222

# Given:


tuple1 = (11, [22, 33], 44, 55)
# Expected output:

# tuple1: (11, [222, 33], 44, 55)


tuple1[1][0] = 222
print(tuple1)
##############################################################################################
# Exercise 8: Sort a tuple of tuples by 2nd item
# Given:

tuple1 = (('a', 23),('b', 37),('c', 11), ('d',29))
# Expected output:

(('c', 11), ('a', 23), ('d', 29), ('b', 37))

tuple1 = sorted(tuple1,key=lambda x:x[1])
print(tuple1)

##############################################################################################
# Exercise 9: Counts the number of occurrences of item 50 from a tuple
# Given:


tuple1 = (50, 10, 60, 70, 50)
# Expected output:

2
print(tuple1.count(50))

##############################################################################################
# Exercise 10: Check if all items in the tuple are the same
tuple1 = (45, 45, 45, 45)
print(all(i==tuple1[0] for i in tuple1))

##############################################################################################