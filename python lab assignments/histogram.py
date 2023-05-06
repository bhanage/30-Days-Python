# Q. 2. Define a procedure histogram() that takes a list of integers and prints a histogram to the
# screen. For example, histogram([4, 9, 7]) should print the following:
# ****
# *********
# *******
for i in [4,9,7]:
    print(i*'*')
    
############################################################################################################ 
#  Q. 3. Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go
# hang a salami I'm a lasagna hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan,
# Otis", "Lisa Bonet ate no basil", "Satan, oscillate my metallic sonatas", "I roamed under it as a tired
# nude Maori", "Rise to vote sir", or the exclamation "Dammit, I'm mad!". Note that punctuation,
# capitalization, and spacing are usually ignored.   
import string
def palindrome(str):
#    first =0
#    last = len(str)-1
#    while(first<last):
#   
#        if(str[first]==str[last]):
#            first = first + 1
#            last = last - 1
#        else:
#            return False
#    return True
    # whitelist = set(string.ascii_lowercase)
    
    # str = ''.join([char for char in str if char in whitelist])
    str = [ch for ch in str if ch.isalpha()]
    return str == str[::-1]


list = ["Go hang a salami I'm a lasagna hog.", 
        "Was it a rat I saw?", 
        "Step on no pets", 
        "Sit on a potato pan,Otis", 
        "Lisa Bonet ate no basil", 
        "Satan, oscillate my metallic sonatas", 
        "I roamed under it as a tirednude Maori", 
        "Rise to vote sir"]
#list =['madam','student','sanikakinas']
for i in list:
    print(f"{i} : {palindrome(i.strip().lower())}")
    
######################################################################################################

