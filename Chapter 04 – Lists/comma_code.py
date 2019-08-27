spam = ['apples', 'bananas', 'tofu', 'cats']

def listToStr(some_list):
    new_string = ''

    if len(some_list) == 0:
        new_string = 'The list is empty'
    elif len(some_list) == 1:
        new_string = some_list[0]
    else:
        for i in range(len(some_list)):
            if i < len(some_list) - 1:
                new_string += some_list[i] + ', '
            else:
                new_string += 'and ' + some_list[i]
            
    return new_string


print(listToStr(spam))
