def collatz(some_int):
    if some_int % 2 == 0: 
        result = some_int // 2
        
    else:               
        result = 3 * some_int + 1

    print(result)
    return(result)

while True:
    try:
        num = int(input("Enter a number : "))
        
        if num <= 0:
            print('Error: The number must be greater than 0.')
            
        else:
            while True:
                num = collatz(num)

                if num == 1:
                    break

            break

    except ValueError:
        print('Error: The number must be an integer.')
        print('Error: The number must be an integer.')
