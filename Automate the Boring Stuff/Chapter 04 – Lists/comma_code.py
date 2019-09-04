spam = ['apples', 'bananas', 'tofu', 'cats']

def listToStr(some_list):
    string = ''

    # Empty list
    if len(some_list) == 0:
        string = 'The list is empty.'

    # One item list    
    elif len(some_list) == 1:
        string = some_list[0]

    # Two or more items list    
    else:
        for i in range(len(some_list)):
            if i < len(some_list) - 1:
                string += some_list[i] + ', '
                
            else:
                string += 'and ' + some_list[i]
            
    return string

print(listToStr(spam))

