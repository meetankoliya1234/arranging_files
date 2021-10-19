import shutil
import os
source = input("Enter source folder name")
destination = input("Enter destination folder name")
source = source + '/'
destination = destination + '/'
list_f = os.listdir(source)
print(list_f)
for f in list_f:
    shutil.move((source + f), destination)
