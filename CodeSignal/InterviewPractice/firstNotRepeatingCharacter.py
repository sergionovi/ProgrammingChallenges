# Sergio L. Novi Junior, sergiolnovi@gmail.com
#
#   STATEMENT OF THE PROBLEM FROM CODESIGNAL.COM
#
# Given a string s consisting of small English letters, 
# find and return the first instance of a non-repeating 
# character in it. If there is no such character, return '_'.

##### EXAMPLE

# For s = "abacabad", the output should be
# firstNotRepeatingCharacter(s) = 'c'.
#
# There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.
#
# For s = "abacabaabacaba", the output should be
# firstNotRepeatingCharacter(s) = '_'.

# There are no characters in this string that do not repeat.


def firstNotRepeatingCharacter(s):
    lst=[]
    for item in s: 
        if not item in lst:
            if s.count(item)==1:
                return item;
            lst.append(item)
        
    return '_'