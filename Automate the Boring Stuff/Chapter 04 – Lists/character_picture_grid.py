grid = [['.', '.', '.', '.', '.', '.'],     
        ['.', 'O', 'O', '.', '.', '.'],     
        ['O', 'O', 'O', 'O', '.', '.'],     
        ['O', 'O', 'O', 'O', 'O', '.'],     
        ['.', 'O', 'O', 'O', 'O', 'O'],     
        ['O', 'O', 'O', 'O', 'O', '.'],     
        ['O', 'O', 'O', 'O', '.', '.'],     
        ['.', 'O', 'O', '.', '.', '.'],     
        ['.', '.', '.', '.', '.', '.']]     

def printImage(some_list):
    for y in range(len(some_list[0])):       
        for x in range(len(some_list)):    
            print(some_list[x][y], end='')

        print()
        
printImage(grid)

