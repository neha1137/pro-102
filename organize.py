import os
import shutil

from_dir = 'C:/Users/chair/Downloads/C102_assets-main'
to_dir = 'C:/Users/chair/Desktop/folders/NEHA/Downloaded_Images'

list_of_files = os.listdir(from_dir)
#print(list_of_files)

for file_name in list_of_files :
    name,extension = os.path.splitext(file_name)
    #print(name)
    #print(extension)
    if extension == '' :
        continue
    if extension in ['.jpg','.gif','.png','.jpeg','.jfif'] :
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + 'image_files'
        path3 = to_dir + '/' + 'image_files' + '/' + file_name
        
        if os.path.exists(path2):
            print("Moving " + file_name + "....")

            shutil.move(path1,path3)
        
        else :

            os.mkdir(path2)
            print("Moving " + file_name + "....")

            shutil.move(path1,path3)
