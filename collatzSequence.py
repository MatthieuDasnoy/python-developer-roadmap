def collatz(some_int):
    if some_int % 2 == 0: 
        result = some_int // 2
    else:               
        result = 3 * some_int + 1

    print(result)
    return(result)
    
while True:
    #Input validation
    try:
        num = int(input("Enter a number : "))
        
        if num <= 1:
            print('Error: The number must be greater than 1.')
        else:
            while num != 1:
                num = collatz(num)

            break

    except ValueError:
        print('Error: The number must be an integer.')


    
    
