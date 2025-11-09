import os

file_path = "test.txt"
file_path2 = "./stuffs/test2.txt"

if os.path.exists(file_path2):
    print(f'File {file_path2} exists')
    if os.path.isfile(file_path2):
        print(f'That is a file')
    elif os.path.isdir(file_path2):
        print(f'Directory {file_path2} exists')
else:
    print('File does not exist')