#handling userdefined Exception

"""
1) Write a program that creates a dictionary like this 
{
    1: "red" , 2: "Blue" , 3: "Orange"
}
Now take the key as input from the user and print its corresponding colour 
(Exception handle the code to terminate gracefully by printing 
Colour not found if the key doesnot exists )
"""
# class ColorNotFoundError(Exception):
#     pass
# try:
#     colors = {1: "red" , 2: "Blue" , 3: "Orange"}
#     id =int(input(f"Enter the id for color {colors}  :"))
#     if id in colors.keys():
#         print(colors[id])
#     else:
#         raise ColorNotFoundError()
        
# except ColorNotFoundError:
#     print("Id for the color does not exists.Hence cannot find color.Please check id.")

#################################################################################################
"""
2) Write a program that creates a list of 5 elements of your choice 
Now take the index that the user want the data of and print the value at that 
location 
Exception handle the code to  terminate gracefully by printing 
Value not found if the index doesnot exists 
"""
# import random 
# class IndexNotFoundError(Exception):
#     pass
# try:
#     list = [random.randint(1,99) for i in range(1,6)]
#     index = int(input(f"Enter the index for elements in list of {list}"))
#     if index in list:
#         print(list[index])
#     else:
#         raise IndexNotFoundError
# except IndexNotFoundError:
#     print("Index not found. Please check index number!")


###################################################################################################
"""
3) Create program that takes age of the user as input 
and prints number of days that user has lived for 
Exception handle the code such that if the user has lived for more than 
100001 days then user should get the message
, you lived for so long , may be you will die soon:)
"""
# class MessageForAge(Exception):
#     pass
# try:
#     age = int(input("Enter your age"))*365
#     if  age > 100001:
#         raise MessageForAge()
#     else:
#         print("number of days you are lived for : ",age)
# except MessageForAge:
#     print(f"you lived for so long {age}, may be you will die soon")
    
###################################################################################################
# 4) Complete the bits and pieces of the following below code 
class negative_number_error(Exception):
    pass
class positive_number_error(Exception):
    pass
class element_not_found(Exception):
    pass
class list_empty_error(Exception):
    pass
class homogenous_list_error(Exception):
    pass
class index_range_out_of_bound(Exception):
    pass
def create_positive_numbered_list(my_int_list1):
    for i in range(int(input("Enter the number range"))):
        num = int(input(f"Enter the {i}'th index number: "))
        if num < 0:
            raise negative_number_error()
        else:
            my_int_list1.append(num)
    if len(my_int_list1)==0:
        raise list_empty_error()
    
   

def create_negative_numbered_list(my_int_list2):
    for i in range(int(input("Enter the number range"))):
        num = int(input(f"Enter the {i}'th index number: "))
        if num > 0:
            raise positive_number_error()
        else:
            my_int_list2.append(num)
   
    
def  create_heterogenous_list(my_het_list3):
    
    for i in range(int(input("Enter the range for hetrogenous list: "))):
        datatype_choice = int(input("Please choose a datatype of the element to be added \
        \n 1) int \n 2) float \n 3) str \n 4) tuple \n 5) list \n 6) set \n 7) dictionary \n "))
        if datatype_choice == 1:
            my_het_list3.append(int(input("Enter the number: ")))
        elif datatype_choice == 2:
            my_het_list3.append(float(input("Enter the float number: ")))
        elif datatype_choice == 3:
            my_het_list3.append(input("Enter the string: "))
        elif datatype_choice == 4:
            my_het_list3.append(tuple(input("Please enter a tuple to be added like 1,2 ").split(",")))
        elif my_het_list3 == 5:
            my_het_list3.append(input("Enter the element for list itself: "))
        elif datatype_choice == 6:
            my_het_list3.append(set(input("Enter the elements in comma seperated form: ").split(",")))
        elif datatype_choice == 7:
            my_het_list3_tuple = []
            for str_elem in input("Enter the elements like  key1:value1,key2:value2 format: ").split(","):
                my_het_list3_tuple.append(tuple(str_elem.split(":")))
            my_het_list3.append(dict(my_het_list3_tuple))
        else:
            print("Invalid choice ")
    if len(my_het_list3) == 0:
        raise list_empty_error()
    counterint=0
    counterfloat=0
    counterstr=0
    countertuple=0
    counterset=0
    counterdict=0
    counterlist=0  
    for i in range(len(my_het_list3)):
        
        if type(my_het_list3[i]) == int:
            counterint += 1
        elif type(my_het_list3[i]) == float:
            counterfloat += 1
        elif type(my_het_list3[i]) == str:
            counterstr += 1
        elif type(my_het_list3[i]) == tuple:
            countertuple += 1
        elif type(my_het_list3[i]) == set:
            counterset += 1
        elif type(my_het_list3[i]) == dict:
            counterdict += 1
        elif type(my_het_list3[i]) == list:
            counterlist += 1
        
        else:
            pass
    if counterint > 1:
        raise homogenous_list_error()
    elif counterfloat > 1:
        raise homogenous_list_error()
    elif countertuple > 1:
        raise homogenous_list_error()
    elif counterstr > 1:
        raise homogenous_list_error()
    elif counterset > 1:
        raise homogenous_list_error()
    elif counterdict > 1:
        raise homogenous_list_error()
    elif counterlist > 1:
        raise homogenous_list_error()
    else:
        print(f"We get hetrogenous list: {my_het_list3}")
            
            
            
def display_list(my_list):
    print(my_list)
    
def find_an_element(my_list):
    if len(my_list)==0:
        raise list_empty_error()
    index_number = int(input("Enter the index for the element"))
    
    if index_number < len(my_list):
        if my_list[index_number] in my_list:
            print(f"Element founded at the location: {my_list[index_number]}")
        else:
            raise element_not_found()
    else:
        raise index_range_out_of_bound()
    


    

def my_exception_store(): 
    my_int_list1=[]
    my_int_list2=[]
    my_het_list3=[]

    while(True):
        try:
            print("Welcome to my_exception_store !!!!")
            print("-------------------------------------")
            print("Following operations are supported :")
            print("1) Create a positive numbered list  ")
            print("2) Create a negative numbered list  ")
            print("3) Create a heterogenous list ")
            print("4) Check if the element is present in the list ")
            print("5) Refresh the program to start with blank lists")
            print("6) Exit  ")
            
            choice = int(input("Please enter your choice !!!! "))
            if choice ==1:
                create_positive_numbered_list(my_int_list1)
            elif choice ==2:
                create_negative_numbered_list(my_int_list2)
            elif choice ==3:
                create_heterogenous_list(my_het_list3)
            elif choice ==4:
                print("Lists created are as below \n ----------------------")
                print("1.Positive Integers list: ", display_list(my_int_list1))
                print("2.Negative Integer List: ",display_list(my_int_list2))
                print("3.Heterogenous List: ",display_list(my_het_list3))
                while True:
                    check =int(input("Which of the below list you would want to search from "))
                    
                    if  check == 1:
                        find_an_element(my_int_list1)
                        break
                    elif check == 2:
                        find_an_element(my_int_list2)
                        break
                    elif check ==3:
                        find_an_element(my_het_list3)    
                        break
                    else:
                        print("Please choose something from the above")
            elif choice ==5:
                my_int_list1.clear()
                my_int_list2.clear()
                my_het_list3.clear()
                print("Store restarted !!!! ")
            elif choice ==6:
                break
            else:
                print("Please choose something from the above")
        except negative_number_error:     
            print("We received a negative number in the list and I handled negative_number_error exception")
            my_int_list1.clear()
        except positive_number_error:     
            print("We received a positive number in the list and I handled positive_number_error exception")
            my_int_list2.clear()
        except homogenous_list_error:    
            print("We received a Homogenous list and I handled homogenous_list_error exception")
            my_het_list3.clear()
        except list_empty_error:
            print("List is empty")
        except index_range_out_of_bound:
            print("Index range out of bound!")
        except element_not_found:
            print("Index Number not found!")
my_exception_store()   