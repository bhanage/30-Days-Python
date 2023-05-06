# Q. 1. In cryptography, a Caesar cipher is a very simple encryption techniques in which each letter
# in the plain text is replaced by a letter some fixed number of positions down the alphabet. For
# example, with a shift of 3, A would be replaced by D, B would become E, and so on. The method is
# named after Julius Caesar, who used it to communicate with his generals. ROT-13 ("rotate by 13
# places") is a widely used example of a Caesar cipher where the shift is 13. In Python, the key for
# ROT-13 may be represented by means of the following dictionary:
import string
import re
key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w', 'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b',
       'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g', 'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm', 'A': 'N', 'B': 'O', 'C': 'P', 'D': 'Q', 'E': 'R',
       'F': 'S', 'G': 'T', 'H': 'U', 'I': 'V', 'J': 'W', 'K': 'X', 'L': 'Y', 'M': 'Z', 'N': 'A', 'O': 'B', 'P': 'C', 'Q': 'D', 'R': 'E', 'S': 'F',
       'T': 'G', 'U': 'H', 'V': 'I', 'W': 'J', 'X': 'K', 'Y': 'L', 'Z': 'M'}
# str = "Pnrfne pvcure? V zhpu cersre Pnrfne fnynq!"
# for i in str:

#     if re.search('\W', i):
#         print(i, end='')
#     else:
#         print(key.get(i), end='')


# ########################################################################################################
# Q. 4. A pangram is a sentence that contains all the letters of the English alphabet at least once, for
# example: The quick brown fox jumps over the lazy dog. Your task here is to write a function to
# check a sentence to see if it is a pangram or not.
#str = "The quick brown fox jumps over the lazy dog."
str = "sanika"


str = str.replace(" ","")
cnt=26
for i in str:
    if i.isalpha():
        if i in string.ascii_lowercase:
            cnt -= 1
            
if cnt>0:
    print("not pangrams")
else:
    print("pangrams")

########################################################################################################
