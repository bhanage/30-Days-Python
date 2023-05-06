# Exercise 1: Reverse a list in Python
# Given:

list1 = [100, 200, 300, 400, 500]
# Expected output:

# [500, 400, 300, 200, 100]
list1 = list1[::-1]
print(list1)
############################################################################################################
# Exercise 2: Concatenate two lists index-wise
# Write a program to add two lists index-wise. Create a new list that contains the 0th index item from both the list, then the 1st index item, and so on till the last element. any leftover items will get added at the end of the new list.

# Given:

list_char1 = ["M", "na", "i", "Ke"]
list_char2 = ["y", "me", "s", "lly"]
# Expected output:

# ['My', 'name', 'is', 'Kelly']
def concate(l1_char,l2_char):
    return l1_char + l2_char

print(list(map(concate,list_char1,list_char2)))

############################################################################################################
# Exercise 3: Turn every item of a list into its square
# Given a list of numbers. write a program to turn every item of a list into its square.

# Given:

numbers = [1, 2, 3, 4, 5, 6, 7]
# Expected output:

# [1, 4, 9, 16, 25, 36, 49]
from my_functions_generic import my_square
print(list(map(my_square,numbers)))
############################################################################################################
# Exercise 4: Concatenate two lists in the following order
list_char11 = ["Hello ", "take "]
list_char22 = ["Dear", "Sir"]
# Expected output:

# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir']
def concate_space(l1,l2):
    return l1 + " " + l2
print(list(map(concate_space,list_char11,list_char22)))
############################################################################################################
# Exercise 5: Iterate both lists simultaneously
# Given a two Python list. 
# Write a program to iterate both lists simultaneously and 
# display items from list1 in original order and items from list2 in reverse order.
# Given

list_num1 = [10, 20, 30, 40]
list_num2 = [100, 200, 300, 400]
# Expected output:

# 10 400
# 20 300
# 30 200
# 40 100
for i in range(len(list_num2)):
    print(list_num1[i],end=' ')
    print(list_num2[len(list_num2)-i-1])
    
##########################################################################################################
# Exercise 6: Remove empty strings from the list of strings
list_user = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# Expected output:

# ["Mike", "Emma", "Kelly", "Brad"]


print(list(filter(bool,list_user)))

##########################################################################################################
# Exercise 7: Add new item to list after a specified item
# Write a program to add item 7000 after 6000 in the following Python List

# Given:

list_item = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:

# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]
list_item[2][2].append(7000)
print(list_item)
########################################################################################################
# Exercise 8: Extend nested list by adding the sublist
# You have given a nested list. 
# Write a program to extend it by adding the sublist ["h", "i", "j"] 
# in such a way that it will look like the following list.
# Given List:

nested_list = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n"]

# # sub list to add
sub_list = ["h", "i", "j"]
# Expected Output:

# ['a', 'b', ['c', ['d', 'e', ['f', 'g', 'h', 'i', 'j'], 'k'], 'l'], 'm', 'n']
nested_list[2][1][2].extend(sub_list)
print(nested_list)

########################################################################################################
# Exercise 9: Replace list’s item with new value if found
# You have given a Python list. Write a program to find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of an item.

# Given:

list_numbers = [5, 10, 15, 20, 25, 50, 20]
# Expected output:

# [5, 10, 15, 200, 25, 50, 20]
list_numbers[list_numbers.index(20)] = 200
print(list_numbers)

#######################################################################################################
# Exercise 10: Remove all occurrences of a specific item from a list.
# Given a Python list, write a program to remove all occurrences of item 20.

# Given:
list_ocurrence = [5, 20, 15, 20, 25, 50, 20]
# Expected output:

# [5, 15, 25, 50]

for i in list_ocurrence:
   if list_ocurrence.count(20) == 0:
       break
   j = list_ocurrence.index(20)
   del list_ocurrence[j]
   
print(list_ocurrence)