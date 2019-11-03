# Sergio L. Novi Junior, sergiolnovi@gmail.com
#
#   STATEMENT OF THE PROBLEM FROM CODESIGNAL.COM
#
#You are given an n x n 2D matrix that represents an image. 
#Rotate the image by 90 degrees (clockwise).

def rotateImage(a):
    lst=[x[:] for x in a]
    n=len(a)-1;
    for j in range(len(a)):
        for i in range(len(a)):           
            lst[i][j]=a[n-j][i];
    
    return lst