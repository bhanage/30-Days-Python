#Declaring functions 
def my_additions(num1=0,num2=1):
    return num1+num2

def my_square(num1=1):
    return num1**2

def my_exponential(num1=1,num2=1):
    return num1**num2

def my_divisions(num1=2,num2=1):
    return num1/num2

def my_multiplication(num1=1,num2=2):
    return num1*num2

def my_subtraction(num1=2,num2=1):
    return num1-num2

def my_mod(num1=1,num2=2):
    return num1%num2


def my_string_upper(string='abc'):
       return string.upper()
   
def raise_salary_percentage(salary=900,increment=15):
    return salary + ((increment*salary)/100)


def height_in_inches(heignt=165):
    return round(heignt/39.84,2)



def dollar_conversion(rupees=165):
    return 82*rupees

def discount_calculation(discount_rate,fare):
    return fare - ((discount_rate*fare)/100)


def my_calculator():
    
        options = int(input("\n1.Addition \n2. exponential \n3.square \n4.subtraction \n5.multiplication \n6.Division \n7.mod \nEnter the choice:"))
        num1,num2 = int(input("Enter the first number:")),int(input("Enter the second number:"))
        if options == 1:
            print(my_additions(num1,num2))
        elif options == 2:
            print(my_exponential(num1,num2))
        elif options == 3:
            print(f"For {num1}: {my_square(num1)} \n For {num2}: {my_square(num2)}")
        
        elif options == 4:
            print(my_subtraction(num1,num2))
        elif options == 5:
            print(my_multiplication(num1,num2))
        elif options == 6:
            print(my_divisions(num1,num2))
        elif options == 7:
            print(my_mod(num1,num2))
    
        else:
            print("Invalid choice")
       