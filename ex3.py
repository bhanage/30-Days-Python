
# """1) Take a number from the user and print sum from 1 to that number """

sum_upto_number = int(input("Please enter a number to sum upto: "))
sum = 0
cnt = 1
while (cnt <= sum_upto_number):
    sum += cnt
    cnt += 1

print(sum)
##################################################################################################
"""2) Take a number from the user and print all prime numbers from 1 to that number """


def prime_numbers(number):
    if number == 2:
        return True
    for divisor in range(2, number//2+1):
        if number % divisor == 0:
            return False

    return True


number = int(input("enter the number: "))
print("prime numbers: ")
for i in range(2, number+1):
    if prime_numbers(i):
        print(i, end=' ')

# 3
"""3) Take a number from the user and print all Odd numbers from 1 to that number """

user_input_number = int(input("Enter the number:"))
current_checked_number = 1
while (current_checked_number <= user_input_number):
    if current_checked_number % 2 != 0:
        print(f"{current_checked_number} is odd number")
    current_checked_number += 1

#####################################################################################################
"""4) Take a number from the user and print all Even numbers from 1 to that number """


user_input_number = int(input("Enter the number:"))
current_checked_number = 1
while (current_checked_number <= user_input_number):
    if current_checked_number % 2 == 0:
        print(f"{current_checked_number} is even number")
    current_checked_number += 1


#####################################################################################################
'''5) Take a number from the user and print fibonacci sequence till that number
# 	eg : fibonnaci sequence for 5 is 1,2,3,5 """'''
num1 = -1
num2 = 1
sum = 0
input_no = int(input(
    "Please enter the number till which you want to  print fibonacci sequence ?"))
# for i in range(-1,input_no):
while (True):
    sum = num1 + num2
    if sum > input_no:
        break
    print(sum, end=' ')
    num1 = num2
    num2 = sum
