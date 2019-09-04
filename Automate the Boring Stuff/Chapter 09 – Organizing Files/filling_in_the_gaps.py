import os, re, shutil

src = r'C:\FillingInTheGaps' 
pattern = re.compile(r'(spam)(\d{3})(.txt)')

def fillingInTheGaps(src, pattern):
    i = 1

    for filename in os.listdir(src) :
        mo = pattern.search(filename)

        if mo:
            filename_new = mo.group(1) + str(i).rjust(3, '0') + mo.group(3)
            i += 1

            shutil.move(os.path.join(src, filename), os.path.join(src, filename_new))
            
fillingInTheGaps(src, pattern)
            
        
        
        
        

   
        
