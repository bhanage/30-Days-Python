from my_functions import my_additions,my_exponential,my_square,my_string_upper,raise_salary_percentage,height_in_inches,dollar_conversion,discount_calculation
'''-------------------
Exercise : Questions based on variable, statements , input and print functions and operators 
------------------

1) Accept two numbers from the user and print 
a) addition 
b) first number squared 2 
c) first number raised to number second number'''
print("Addition: ",my_additions(int(input("Enter the first number: ")),int(input("Enter the first number: "))),
"\nSquare of a number : ",my_square(int(input("Enter thhe number for square: "))),
"\nExponential",my_exponential(int(input("Enter the first number: ")),int(input("Enter the first number: "))))


# ==============================================================================================================
# 2) Accept String from user and output upper case of the input string 
my_string_upper(input("Enter the string: "))

# ==============================================================================================================
'''
3) Define a variable named "raise_salary_percentage" and get the salary raise 
percentage from the user, Now apply the raise to an employee
with harcoded data Name= 'gaurav' existing_salary = 900 INR and 
print the incremented salary to the console'''
#name='gaurav' 
#existing_salary = 900
print("Incremented salary is",raise_salary_percentage(float(input("Enter the salary : ")),float(input("Enter the increment in salary in percentage: "))))


#==============================================================================================================
# 4) Get the height from the user in cms and display the user height back to console
# in foot/feet and inches
print("The height in inches is : ",height_in_inches(int(input("Enter the height: "))))
#==============================================================================================================


# '''5) Get the no of the dollars from the user apply the conversion of 
# 1 dollar = 82 rupees and print the amount to the console in rupees
print("Conversion in dollars is: ",dollar_conversion(int(input("Enter the rupees: "))))
##==============================================================================================================
'''
6) Take the source, destination, fare in INR, discount_rate percentage from the user and display the 
string ex: "fare from mumbai to pune is 300 INR with has a discount of 5%"
'''
source = input("Enter the source city: ")
destination = input("Enter the destination city: ")
fare = int(input("Enter the fare INR: "))
discount_rate= float(input("Enter the discount rate in %: "))
print(f"fare from {source} to {destination} is {discount_calculation} INR with has a discount of {discount_rate}%")