spam = ['apples', 'bananas', 'tofu', 'cats']

def listToStr(some_list):
    new_string = ''
    
    for i in range(len(some_list)):
        if i < len(some_list) - 1:
            new_string += some_list[i] + ', '
        else:
            new_string += 'and ' + some_list[i]
            
    return new_string


print(listToStr(spam))
