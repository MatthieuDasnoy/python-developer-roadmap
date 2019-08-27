grid = [['.', '.', '.', '.', '.', '.'],     
        ['.', 'O', 'O', '.', '.', '.'],    
        ['O', 'O', 'O', 'O', '.', '.'],     
        ['O', 'O', 'O', 'O', 'O', '.'],     
        ['.', 'O', 'O', 'O', 'O', 'O'],     
        ['O', 'O', 'O', 'O', 'O', '.'],     
        ['O', 'O', 'O', 'O', '.', '.'],     
        ['.', 'O', 'O', '.', '.', '.'],     
        ['.', '.', '.', '.', '.', '.']]     

#Browse table by columns
for y in range(len(grid[0])):     
    for x in range(len(grid)):    
        print(grid[x][y], end='')

    print()



