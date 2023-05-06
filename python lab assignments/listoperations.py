#Q.5 Reverse a list in Python
# o Concatenate two lists index-wise.
# o Write a Python program to multiply all the items in a list.
# o Write a Python program to get the smallest number from a list.
list = ['sanika','madhuri','sneha','utkarsha']
list_number = [i*2 for i in range(len(list))]
print(list_number)
print("Reverse List is :",list[::-1])
print([x*6 for x in list_number])
print(min(list_number))
print([list[i]+str(list_number[i]) for i in range(len(list))])
####################################################################################################################

# Q. 1. Given a dictionary of students and their favourite colours:
people={'Zrham':'Blue','Lisa':'Yellow','Vinod':'Purple','Jenny':'Pink'}
# 1. Find out how many students are in the list
# 2. Change Lisa’s favourite colour
# 3. Remove 'Jenny' and her favourite colour
# 4. Sort and print students and their favourite colours alphabetically by name

people['Lisa'] = 'pink'
print(people)
people.pop('Jenny')
print(people)

print({i:people[i] for i in sorted(people.keys())})
####################################################################################################################

# Write a function translate() that will translate a text into "rövarspråket" (Swedish for "robber's
# language"). That is, double every consonant and place an occurrence of "o" in between. For
# example, translate("this is fun") should return the string "tothohisos isos fofunon".

def translate(str):
    str1=''

    for i in str:
        if i not in ['å','e','i','ö','u','a','o',' ']:
                str1 += i+'o'+i
        else:
                str1 += i
    print(str1)
translate("rövarspråket")
translate("this is fun")
####################################################################################################################
# Q. 2. Write a program that contains a function that has one parameter, n, representing an integer
# greater than 0. The function should return n! (n factorial). Then write a main function that calls this
# function with the values 1 through 20, one at a time, printing the returned results. This is what your
# output should look like:
# 1 1
# 2 2
# 3 6
# 4 24
# 5 120
# 6 720
# 7 5040
# 8 40320
# 9 362880
# 10 3628800
class less_than_zero_error(Exception):
    pass
def factorial(n):
    if n==1:
        return n
    return n*factorial(n-1)
try:
    input_number_range = 10 #int(input("Enter the input the number: "))
    if input_number_range > 0:
        for i in range(1,input_number_range+1):
            print(i," ",factorial(i))
    else:
        raise less_than_zero_error()
except less_than_zero_error:
    print("Number is less than or equal to zero!")    
####################################################################################################################
# Q. 2. We can define sum from 1 to x (i.e. 1 + 2 + ... + x) recursively as follows for integer x ≥ 1:

# 1, if x = 1
# x + sum from 1 to x-1 if x > 1

# Complete the following Python program to compute the sum 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# recursively:
# def main():
# compute and print 1 + 2 + ... + 10
    # print sum(10)
# def sum(x):
# you complete this function recursively main()

def sum(x):
    if x == 1:
        return x
    return x+sum(x-1)
def main():
    print(sum(10))
main()
####################################################################################################################
# Q. 3. Define a function overlapping() that takes two lists and returns True if they have at least one
# member in common, False otherwise.
list1 = ['sanika','prajakta','group','stars',334,0,22]
list2 = [22,0,'#','~','%','&','*']

print("Uncommon" if set(list1).isdisjoint(set(list2))==True else "Common")
####################################################################################################################
# Q. 4. Write a function find_longest_word() that takes a list of words and returns the length of the
# longest one.
import random
import string
list = [''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1,10))) for i in range(10)]
print(list)

def find_longest_word():
    max = len(list[0])
    word = ""
    for i in range(1,len(list)):
        if len(list[i]) > max:
            max = len(list[i])
            word = list[i]
    print("The longest word is",max,"characters long. And that word is ",word)
find_longest_word()
 

####################################################################################################################
# Q. 5. Write a function filter_long_words() that takes a list of words and an integer n and returns the
# list of words that are longer than n



def filter_long_words(list,n):
    list_new = []
    for i in list:
        if len(i) > n:
            list_new.append(i)
    print("List of words that are longer than ",n," is ",list_new)
            
def main():
    list = [''.join(random.choice(string.ascii_lowercase) for i in range(random.randint(1,8))) for i in range(10)]
    print(list)
    #filter_long_words(list,int(input("Enter the number: ")))
    filter_long_words(list,5)
main()

####################################################################################################################
# Q. 6. Define a simple "spelling correction" function correct() that takes a string and sees to it that
# 1) two or more occurrences of the space character is compressed into one, and
# 2) inserts an extra space after a period if the period is directly followed by a letter.
# e.g. correct("This is very funny and cool.Indeed!") should return "This is very funny and cool. Indeed!"
 
def correction(string):
    str = " ".join(string.split())
    new_str = ""
    for i in str:
        if i == ".":
            new_str += i+" "
        else:
            new_str += i
    print(new_str)

correction("This                         is very funny and cool.Indeed!")
####################################################################################################################
# Q. 7. In English, present participle is formed by adding suffix -ing to infinite form: go -> going. A
# simple set of heuristic rules can be given as follows:
#  If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
#  If the verb ends in ie, change ie to y and add ing
#  For words consisting of consonant-vowel-consonant, double the final letter before adding
# ing
#  By default just add ing
# Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive
# form returns its present participle form. Test your function with words such as lie, see, move and
# hug. However, you must not expect such simple rules to work for all cases.


def make_ing_form(string):
    new_str = ""
    flag = True
    if string[-1] == "e":
        if string not in ["be","see","flee","knee"]:
            new_str = string[:-1] + "ing"
            flag = False
    if string[-2:] == "ie":
            new_str = string[:-2]+"ying"
            flag = False
    if flag:
        new_str = string + "ing"
    
    print(new_str)


make_ing_form("move") #first if 'e'
make_ing_form("see") #first if 'ee' fails then go to last if 
make_ing_form("hug") #last if 
make_ing_form("go") #last if
make_ing_form("lie") #second if 'ie'
####################################################################################################################
