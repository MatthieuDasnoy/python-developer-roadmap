import re

def regexStrip(some_string, some_chars=None):
    if some_chars:      
        regex_left = re.compile(r'^[' + some_chars + ']*')
        regex_right = re.compile(r'[' + some_chars + ']*$')
        
    else:
        regex_left = re.compile(r'^\s*')
        regex_right = re.compile(r'\s*$')

    return regex_right.sub('', regex_left.sub('', some_string))    

#Examples from https://www.programiz.com/python-programming/methods/string/strip
string = ' xoxo love xoxo   '
print(regexStrip(string))
print(regexStrip(string, ' xoxoe'))
print(regexStrip(string, 'sti'))

string = 'android is awesome'
print(regexStrip(string, 'an'))
