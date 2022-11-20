# Compressing files with the zipfile module

import zipfile
import os

# Extracting from zip files.
zipPath = os.path.relpath(".")
os.chdir("C:\\")
exampleZip = zipfile.ZipFile("Hello.rar")
exampleZip.extractall(zipPath) # use .extract(Hello.txt) to extract a single file.
exampleZip.close()

# Creating and Adding to zip files
newZip = zipfile.ZipFile("newZip.zip", "w")  # use "a" to append to an already existing zip file
newZip.write("spam.txt", compress_type=zipfile.ZIP_DEFLATED)
newZip.close()
