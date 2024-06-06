import os
import re
import shutil

def find_skiped_files(folder, prefix, rename=False):
    files = {}          
    max_digit_len = 0  
    rest = ''          

    pattern = re.compile('^' + prefix + r'(\d+)(.*)')
    for filename in os.listdir(folder):
        mo = pattern.search(filename)
        if not mo:
            continue
        files[int(mo.group(1))] = filename
        max_digit_len = max(max_digit_len, len(mo.group(1)))
        rest = mo.group(2)

    if len(files) == 0:
        return

    org_index = sorted(files.keys())
    start = org_index[0]
    end = org_index[-1]
    for n in range(start, end + 1):
        if not n in files:
            print('Missing', prefix + str(n).rjust(max_digit_len, '0') + rest)

    if rename:
        for n,ind in enumerate(org_index):
            new_filename = prefix + str(start + n).rjust(max_digit_len, '0') + rest
            if new_filename == files[ind]:
                continue
            print('Rename', os.path.join(folder, files[ind]), 
                  '->', os.path.join(folder, new_filename))
            shutil.move(os.path.join(folder, files[ind]), 
                        os.path.join(folder, new_filename))

if __name__ == "__main__":
    find_skiped_files('seqfiles', 'spam')
    find_skiped_files('seqfiles', 'spam', True)
