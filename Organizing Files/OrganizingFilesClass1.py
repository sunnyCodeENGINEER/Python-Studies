# The Shutil Module

import os
import shutil

os.mkdir("C:\\")

# copying single files with the shutil module
shutil.copy("C:\\spam.txt", "C:\\delicious")
# renaming the copied file
shutil.copy("C:\\eggs.txt", "C:\\delicious\\eggs2.txt")

# copying entire directory with the shutil module
shutil.copytree("C:\\bacon", "C:\\bacon_backup")

# moving and renaming files
shutil.move("C:\\bacon.txt", "C:\\eggs")
# renaming the moved file
shutil.move("C:\\bacon.txt", "C:\\eggs\\new_bacon.txt")

# permanently deleting files
for filename in os.listdir():
    if filename.endswith(".rtx"):
        # os.unlink(filename)
        print(filename)
