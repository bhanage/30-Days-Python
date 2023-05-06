# Q.1. Using for loop, write and run a Python program for this algorithm.
# Here is an algorithm to print out n! (n factorial) from 0! to 10! :
# 1. Set f = 1
# 2. Set n = 0
# 3. Repeat the following 10 times:
# a. Output n, "! = ", f
# b. Add 1 to n
# c. Multiply f by n

def factorial(number):
    fact=1
    for i in range(1,number+1):
        fact *= i
    return fact
#print(factorial(int(input("Enter the number: "))))
#######################################################################################################

# Q.2. Modify the program above using a while loop so it prints out all of the factorial values that are
# less than 2 billion. (You should be able to do this without looking at the output of the previous
# exercise.)
result = factorial(int(input("Enter the number")))
if result < 2000000000:
    print("factorial of number : ",result)
else:
    print("Cannot print factorial")