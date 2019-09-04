import re

filename = input('Enter a text file name (whithout extension): ')
file = open(filename + '.txt', 'r')
string = file.read()
file.close()

string_new = ''

for word in re.findall(r'\w+|\W', string):
    if word == 'ADJECTIVE':
        word = str(input('Enter an adjective: '))
        string_new += word

    elif word == 'NOUN':
        word = str(input('Enter a noun: '))
        string_new += word

    elif word == 'ADVERB':
        word = str(input('Enter an adverb: '))
        string_new += word

    elif word == 'VERB':
        word = str(input('Enter a verb: '))
        string_new += word

    else:
        string_new += word

print(string_new)

file_new = open(filename + '_new.txt', 'w')
file_new.write(string_new)
file_new.close()
