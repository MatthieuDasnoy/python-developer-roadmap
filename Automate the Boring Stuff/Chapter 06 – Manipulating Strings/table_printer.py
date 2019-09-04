tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['one', 'two', 'three', 'four']]

def printTable(some_list):
    colWidths = [0] * len(some_list)

    # Browse table by rows
    for x in range(len(some_list)):                      
        for y in range(len(some_list[0])):
            if colWidths[x] < len(some_list[x][y]):
                colWidths[x] = len(some_list[x][y])
  
    # Browse table by columns
    for y in range(len(some_list[0])):                   
        for x in range(len(some_list)):
            print(some_list[x][y].rjust(colWidths[x]), end = ' ')

        print()

printTable(tableData)
