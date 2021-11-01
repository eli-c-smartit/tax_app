from pathlib import Path

# my_dir = Path("db")

# db2_dir = Path(r"C:\Users\jbt\Documents\tax_app\tax_app\db2")
# db2_dir = Path("C:\\Users\\jbt\\Documents\\tax_app\\tax_app\\db2")
# if db2_dir.exists():
#     db2_dir.rmdir()


# if not my_dir.exists():
#     my_dir.mkdir()

# print(my_dir.absolute())

# my_dir.rename("db2")

# path_to_python_file = Path(r"infra\use_file_system.py")
# print(path_to_python_file.exists())

my_dir_files = Path(r"C:\Windows")
# files = my_dir_files.glob('*.*')
# for item in files:
#     print(item.name)

# files = my_dir_files.glob('*.*')
# for item in files:
#     if item.is_dir():
#         print(item.name)    
# print(type(files))

import os
import time
path_to_python_file = Path(r"infra\use_file_system.py")
file_info_stat = os.stat(path_to_python_file.absolute())
# print(os.stat(path_to_python_file.absolute()))
print(time.ctime(file_info_stat.st_ctime))
# print(path_to_python_file.exists())


# f = open('users.txt', 'w')
# f.write('user_1\n')

# f = open('users.txt', 'w')
# f.write('user_2\n')

# f = open('users.txt', 'a')
# f.write('user_3\n')



f = open('users.txt', 'r')
print(f.read(9))
print(f.read(26))
