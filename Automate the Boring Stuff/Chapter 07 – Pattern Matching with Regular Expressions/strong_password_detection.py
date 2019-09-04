import re

def isStrongPassword(some_string):
    pattern_1 = re.compile(r'.{8}')    #8 characters
    pattern_2 = re.compile(r'[A-Z]')   #One uppercase character
    pattern_3 = re.compile(r'[a-z]')   #One lowercase character
    pattern_4 = re.compile(r'\d')      #One digit

    if not pattern_1.search(some_string):
        print('The password is not strong. It must be at least eight characters long.')

    elif not (pattern_2.search(some_string) and pattern_3.search(some_string)):
        print('The password is not strong. It must contain both uppercase and lowercase characters.')

    elif not pattern_4.search(some_string):
        print('The password is not strong. It must contain at least one digit.')

    else:
        print('The password is strong.')
    
isStrongPassword('Azerty12')




