# Sergio L. Novi Junior, sergiolnovi@gmail.com
#
#   STATEMENT OF THE PROBLEM FROM CODESIGNAL.COM
#
#A cryptarithm is a mathematical puzzle for which the goal is to
#find the correspondence between letters and digits, such that the 
#given arithmetic equation consisting of letters holds true when the 
#letters are converted to digits.
#
#You have an array of strings crypt, the cryptarithm, and an an array 
#containing the mapping of letters and digits, solution. The array crypt 
#will contain three non-empty strings that follow the structure: 
#    [word1, word2, word3], which should be interpreted as 
#    the word1 + word2 = word3 cryptarithm.
#
#If crypt, when it is decoded by replacing all of the letters in the 
#cryptarithm with digits using the mapping in solution, becomes a valid 
#arithmetic equation containing no numbers with leading zeroes, the 
#answer is true. If it does not become a valid arithmetic solution, 
#the answer is false.
#
#Note that number 0 doesn't contain leading zeroes 
#(while for example 00 or 0123 do).

def isCryptSolution(crypt, solution):
    lst=[];
    for word in crypt:
        aux='';
        for i in range(len(word)):
            for j in range(len(solution)):
                if solution[j][0]==word[i]:
                    aux = aux+solution[j][1];
        if len(aux)>1 and aux[0]=='0':
            return False;
        else: 
            lst.append(int(aux));
    
    if (lst[0]+lst[1]==lst[2]):
        return True;
    else:
        return False;