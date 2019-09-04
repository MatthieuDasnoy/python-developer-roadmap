import os, re

while True:
    src = input("Enter the folder's path to search into: ")
    if os.path.exists(src):
        os.chdir(src)
        break
    else:
        print("Error: The folder doesn't exist.")
    
files = os.listdir()
txt_files = []

for filename in files:
    if filename.endswith('.txt'):
        txt_files.append(filename)

regex = input('Enter a regular expression to search for: ')
pattern = re.compile(regex)

for filename in txt_files:
    file = open(filename)
    lines = file.readlines()
    file.close()

    for line in lines:
        if pattern.search(line):
            print(line, end='')


    
