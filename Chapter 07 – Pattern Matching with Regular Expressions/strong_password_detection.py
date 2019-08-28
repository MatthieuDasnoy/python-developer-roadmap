import re

def isStrongPassword(some_string):
    regex_1 = re.compile(r'.{8}')    #At least 8 characters
    regex_2 = re.compile(r'[A-Z]')   #At least one uppercase character
    regex_3 = re.compile(r'[a-z]')   #At least one lowercase character
    regex_4 = re.compile(r'\d')      #At least one digit

    if not regex_1.search(some_string):
        print('The password is not strong. It must be at least eight characters long.')

    elif not (regex_2.search(some_string) and regex_3.search(some_string)):
        print('The password is not strong. It must contain both uppercase and lowercase characters.')

    elif not regex_4.search(some_string):
        print('The password is not strong. It must contain at least one digit.')

    else:
        print('The password is strong.')
    
isStrongPassword('Azerty123')



