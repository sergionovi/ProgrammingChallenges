# Sergio L. Novi Junior, sergiolnovi@gmail.com
#
#   STATEMENT OF THE PROBLEM FROM CODESIGNAL.COM
#
#Sudoku is a number-placement puzzle. The objective is to fill a 9 × 9 grid 
#with numbers in such a way that each column, each row, and each of the 
#nine 3 × 3 sub-grids that compose the grid all contain all of the numbers 
#from 1 to 9 one time.
#
#Implement an algorithm that will check whether the given grid of numbers
#represents a valid Sudoku puzzle according to the layout rules described 
#above. Note that the puzzle represented by grid does not have to be solvable.


def sudoku2(grid):
    t_line =set();
    t_colum = set();
    t_triangle =set();
    for i in range(0,9):
        t_line.clear();
        t_colum.clear();
        for j in range(0,9):
            
            if grid[i][j].isdigit():
                if not grid[i][j] in t_line:
                    t_line.add(grid[i][j]);
                else:
                    return False

            if grid[j][i].isdigit():    
                if not grid[j][i] in t_colum:
                    t_colum.add(grid[j][i]);
                else:
                    return False
    
    for cnt in range(0,7,3):
        for cnt2 in range(0,7,3):
            t_triangle.clear()
            for j in range(cnt,cnt+3):
                for i in range(cnt2,cnt2+3):
                    if grid[i][j].isdigit():    
                        if not grid[i][j] in t_triangle:
                            t_triangle.add(grid[i][j]);
                        else:
                            return False 
        
    return True