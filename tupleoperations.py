# o Create a tuple, print that tuple.
# o Use for/while loop while running the programme.
# o Insert/delete an item in tuple.

# my_tuple = (("sanika",23),("abc",244),("erer",344),("para",3434))

# # insert an item in the tuple
# my_tuple = my_tuple[:2] + (10,) + my_tuple[2:]
# print(my_tuple)
# # delete an item from the tuple
# my_tuple = my_tuple[:3] + my_tuple[4:]


# # print the modified tuple
# print("Modified tuple:", my_tuple)


import re

l1 = ["2009_rocking_person@yahoo.com",
       "GodFather2022@yahoo.com",
        "Brocklesner_89_WWE@yahoo.com",
        "TheRock_WWE@yahoo.com" ,
        "JohnCena_WWE@yahoo.com" ,
        "Undertaker_Roman_reigns@outlook.com" ,
        "6789764666@rediffmail.com" ,
        "Kane#6789@gmail.com"]



# for i in l1:
    # if gr := re.search(".*[ #~`!].*",i):
    #     print(gr.group(0))
    # if gr := re.search("^\d.*.@.*",i):
    #     print(gr.group(0))
    # if gr := re.search("^\d+_.*.@.*",i):
    #     print(gr.group(0))
    # if gr := re.search("^\d+[_a-z].*.@.*",i):
    #     print(gr.group(0))
    # if gr := re.search("^\d+[_a-zA-Z].*.@.*",i):
    #     print(gr.group(0))
        
    # if gr := re.search(".*[0-9]+[@].*",i):
    #     print(gr.group(0))
    #  if gr := re.search(".*\d.*.[@].*",i):
    #     print(gr.group(0))
    
text = "The quick brown fox jumps over\tthe\nlazy dog. 123.456 jumps"

# # match a single character except newline
# pattern = r"."
# matches = re.findall(pattern,text) #The re.findall() function is then used to find all matches of the pattern in the text and returns a list of all matched characters.
# print(matches)


#match particular pattern
# pattern = r"brown"
# matches = re.search(pattern,text)
# print(matches.group(0))

# Find all occurrences of a pattern in a string:
# pattern = r"the"
# matches = re.findall(pattern,text)


# Replace a pattern with a new string:
# pattern = r"the"
# replace = re.sub(pattern,"str",text)
# print(replace)

# Match a word.
# pattern = r"\bjumps\b"
# match = re.search(pattern,text)
# print(match.group(0))

# Match a single whitespace character. 
# pattern = r"\s"
# match = re.findall(pattern,text)
# print(match)

my_addition = lambda first,second: first+second
my_sqr = lambda first,second=None:first*first

def my_func(my_func,param1,param2=None):
    return  my_func(param1) if param2 is None else my_func(param1,param2)

print(my_func(my_addition,23,3))
print(my_func(my_sqr,9))