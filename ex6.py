# Dictionary Exercise
def dict_display_capitals(capitals): 
       print(capitals) # write logic here 
     
def dict_add_element(capitals):
     
       capitals.update({input("Enter the country:").replace('"','').strip():input("Enter the capital:").replace('"','').strip()})
       dict_display_capitals(capitals)

def dict_add_elements(capitals):
    for i in input("\nEnter the names as India:New Delhi,America:Washington DC etc.").split(","): # write logic here 
        key,val = i.split(":")
        capitals |= {key:val} # write logic here 
    dict_display_capitals(capitals)
     
def dict_remove_element(capitals):
    capitals.pop(input("Enter the country to be removed: "))# write logic here 
    dict_display_capitals(capitals)

def my_dict_store():
    print("\n Welcome to Our Dict Store !!! ")
    print("Please enter a list Comma seperated dictionary elements that you would want to perform Operation Upon")
    capitals = {}
    for i in input("\nEnter the names as India:New Delhi,America:Washington DC etc.").split(","):
        key,val = i.split(":")
        capitals[key.replace('"','').strip()] = val.replace('"','').strip()
    while(True):
        print("\n*************** Menu **********************")
        print("Operations supported by our program are :")
        print("    1: Display number of elements in the capitals collection")
        print('    2: Add an element to the capitals collection like --> Afghanistan: Kabul')
        print('    3: Add multiple elements to the capitals collection like -->  Albania:Tirana,Algeria:Algiers,Andorra:Andorra la Vella')
        print("    4: Remove an element from the collection 	")
        print("    5: Exit the Program ")
        choice = int(input("Please enter your choice "))
        
        if choice   ==1:
            dict_display_capitals(capitals) 
        elif choice ==2:
            dict_add_element(capitals)
        elif choice ==3:
            dict_add_elements(capitals)
        elif choice ==4:
            dict_remove_element(capitals) 
        elif choice ==5:
            break
        else:
            print("Invalid Input , Please Try Again !!!!  ")

                



my_dict_store()
