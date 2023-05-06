# Exercise 1: Convert two lists into a dictionary
# Below are the two lists. Write a Python program to convert them into a dictionary in a way that item from list1 is the key and item from list2 is the value

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

dictionary = dict(zip(keys,values))
print(dictionary)
# ####################################################################################################
# Exercise 2: Merge two Python dictionaries into one
dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# Expected output:

# {'Ten': 10, 'Twenty': 20, 'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict1.update(dict2)
# print(dict1)

dict3 = {**dict1, **dict2}
print(dict3)

####################################################################################################
# Exercise 3: Print the value of key ‘history’ from the below dict
sampleDict = {
    "class": {
        "student": {
            "name": "Mike",
            "marks": {
                "physics": 70,
                "history": 80
            }
        }
    }
}
# Expected output:

# 80
print(sampleDict['class']['student']['marks']['history'])
# print(sampleDict.get('class').get('student').get('marks').get('history'))
# ####################################################################################################
# Exercise 4: Initialize dictionary with default values
# In Python, we can initialize the keys with the same values.

# Given:

employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
# Expected output:

# {'Kelly': {'designation': 'Developer', 'salary': 8000}, 'Emma': {'designation': 'Developer', 'salary': 8000}}
employee = dict.fromkeys(employees,defaults)
print(employee)
####################################################################################################
# Exercise 5: Create a dictionary by extracting the keys from a given dictionary
# Write a Python program to create a new dictionary by extracting the mentioned keys from the below dictionary.

# Given dictionary:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# # Keys to extract
# keys = ["name", "salary"]
# Expected output:

# {'name': 'Kelly', 'salary': 8000}
keys = {}
for i in sample_dict.keys():
    if i == 'name':
        keys[i] = sample_dict.get(i)
    if i == 'salary':
        keys[i] = sample_dict.get(i)
        
print(keys)
########################################################################################
# Exercise 6: Delete a list of keys from a dictionary
# Given:

sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}

# Keys to remove
keys = ["name", "salary"]
{'city': 'New york', 'age': 25}
del sample_dict["name"]
del sample_dict['salary']
print(sample_dict)

########################################################################################
# Exercise 7: Check if a value exists in a dictionary

# We know how to check if the key exists in a dictionary. Sometimes it is required to check if the given value is present.

# Write a Python program to check if value 200 exists in the following dictionary.

# Given:

sample_dict = {'a': 100, 'b': 200, 'c': 300}
# Expected output:

# 200 present in a dict

for key,val in sample_dict.items():
    if val == 200:
        print(f"{val} present in a dict ")
        break
#####################################################################################################
# Exercise 8: Rename key of a dictionary
# Write a program to rename a key city to a location in the following dictionary.

# Given:

sample_dict = {
  "name": "Kelly",
  "age":25,
  "salary": 8000,
  "city": "New york"
}

location = sample_dict.pop('city')
sample_dict.update({'location':location})
print(sample_dict)
        
#####################################################################################################
# Exercise 9: Get the key of a minimum value from the following dictionary
sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}
# Expected output:

# Math

print(min(sample_dict))
#####################################################################################################
# Exercise 10: Change value of a key in a nested dictionary
# Write a Python program to change Brad’s salary to 8500 in the following dictionary.
# Given:

sample_dict = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 500}
}
# Expected output:

# {
#    'emp1': {'name': 'Jhon', 'salary': 7500},
#    'emp2': {'name': 'Emma', 'salary': 8000},
#    'emp3': {'name': 'Brad', 'salary': 8500}
# }

sample_dict['emp3']['salary'] = 8500
print(sample_dict)