tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose'],
             ['one', 'two', 'three', 'four']]

def printTable(some_table):
    colWidths = [0] * len(some_table)

    #Browse table by rows
    for x in range(len(some_table)):
        for y in range(len(some_table[0])):
            if colWidths[x] < len(some_table[x][y]):
                colWidths[x] = len(some_table[x][y])

    #Browse table by columns          
    for y in range(len(some_table[0])):
        for x in range(len(some_table)):
            print(some_table[x][y].rjust(colWidths[x]), end = ' ')

        print()

printTable(tableData)
