import os, shutil

src = r'C:\SelectiveCopy'
dst = r'C:\New folder'

if not os.path.exists(dst):
    os.makedirs(dst)

for root, dirs, files in os.walk(src):
    for filename in files:
        if filename.endswith('.jpg'):
            shutil.copy(os.path.join(root, filename), dst)

        
  
