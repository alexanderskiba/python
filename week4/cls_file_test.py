import os.path
from cls_file import File

path_to_file = 'some_filename'
print (os.path.exists(path_to_file))
# False
file_obj = File(path_to_file)
print (os.path.exists(path_to_file))
# True
print (file_obj.read())
# ''
print (file_obj.write('some text'))

print (file_obj.read())
print (file_obj.write('other text'))

print (file_obj.read())

file_obj_1 = File(path_to_file + '_1')
file_obj_2 = File(path_to_file + '_2')
print (file_obj_1.write('line 1\n'))
# 7
print(file_obj_2.write('line 2\n'))
# 7
new_file_obj = file_obj_1 + file_obj_2
isinstance(new_file_obj, File)
# True
print(new_file_obj)
for line in new_file_obj:
    print(ascii(line))