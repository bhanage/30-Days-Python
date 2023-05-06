# Exercise : Questions based on functions , loops, conditionals
# ------------------
# # ***********************************************************
# # Problem 1 
# # ***********************************************************
#  Create a game for FIZZ BUZ and keeping playing with the user untill the user chooses to skip the game
def fuzz_buzz(num):
    if_block_executed = 'F'
    if num % 3 == 0:
        print("FIZZ",end=' ')
        if_block_executed = 'T'
    if num % 5 == 0:
        print("BUZZ")
        if_block_executed = 'T'
    if if_block_executed != 'T':
        print("Invalid input")
choice = 'Y'
while(True):
    if choice == 'Y':
        fuzz_buzz(int(input("Enter the number: ")))
        choice = input("Do you want to continue then enter y/Y?").lower()
        if(choice != 'Y'):
            break
        
 
		
# ***********************************************************
# Problem 2
# ***********************************************************

# Addition/Squaring/exponenation should be done as part of single function named 
# "my_calculator"
# which takes in type of operation, number1,number2 as input 
# and outputs the answer based on the operation
#from my_functions import my_additions,my_exponential,my_square,my_divisions,my_mod,my_multiplication,my_subtraction
from my_functions_generic import my_calculator
continue_choice = 'Y'

while(True):
        print("********My Calculator*************")
        my_calculator()
        continue_choice = input("Do you want to continue? y,Y").lower()
        if continue_choice != 'y':
            break

    
    
    
        