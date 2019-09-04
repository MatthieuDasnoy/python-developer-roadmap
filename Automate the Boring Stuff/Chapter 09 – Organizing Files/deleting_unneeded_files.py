import os, shutil

src = r'C:\Windows'

for root, dirs, files in os.walk(src):
    for filename in files:
        file_path = os.path.join(root, filename)
        
        if os.path.getsize(file_path) > 100000000 :
            print(file_path)
