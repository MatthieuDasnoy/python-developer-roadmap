import os, re, shutil, filling_in_the_gaps

src = r'C:\FillingInTheGaps' 
pattern = re.compile(r'(spam)(\d{3})(.txt)')
gap = 3

def insertGap(src, pattern, gap):
    filling_in_the_gaps.fillingInTheGaps(src, pattern)
    
    files = []

    for filename in os.listdir(src):
        mo = pattern.search(filename)

        if mo:
            files.append(filename)

    files.sort(reverse=True)

    i = len(files)

    for filename in files:
        mo = pattern.search(filename)
        
        if i >= gap:
            filename_new = mo.group(1) + str(i + 1).rjust(3, '0') + mo.group(3)
            i -= 1

            shutil.move(os.path.join(src, filename), os.path.join(src, filename_new))
            
insertGap(src, pattern, gap)
        




    
    



    
    
            
