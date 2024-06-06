import os
import os.path

def find_huge_files(folder, min_size=1000000):
    for foldername, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            abs_path = os.path.join(foldername, filename)
            size = os.path.getsize(abs_path)
            if size > min_size:
                print('Found', abs_path, '(', str(size), 'bytes )')

if __name__ == "__main__":
    find_huge_files('/vagrant/')

