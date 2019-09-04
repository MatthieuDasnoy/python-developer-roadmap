import re

def regexStrip(some_string, some_chars=None):
    if some_chars:      
        l_pattern = re.compile(r'^[' + some_chars + ']*')
        r_pattern = re.compile(r'[' + some_chars + ']*$')
        
    else:
        l_pattern = re.compile(r'^\s*')
        r_pattern = re.compile(r'\s*$')

    return r_pattern.sub('', l_pattern.sub('', some_string))    

# Examples from https://www.programiz.com/python-programming/methods/string/strip
string = ' xoxo love xoxo   '
print(regexStrip(string))
print(regexStrip(string, ' xoxoe'))
print(regexStrip(string, 'sti'))

string = 'android is awesome'
print(regexStrip(string, 'an'))
