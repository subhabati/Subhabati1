import os
from string import digits
list_files=os.listdir("C:\\prank\\prank")
print(list_files)
os.chdir("C:\\prank\\prank")
#repeat the following steps for all the files in the prank directory
for file in list_files:
    #getoldname of file
    old_name = file
    print (old_name)
    #newname of file=oldname-numbers
    new_name=old_name.lstrip(digits)
    print(new_name)
    #rename the file(oldname,newname)
    os.rename(old_name,new_name)