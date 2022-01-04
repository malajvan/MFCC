import os
from unidecode import unidecode

def rename_folder_unidecode(folder):
    for count, filename in enumerate(os.listdir(folder)):
        dst = unidecode(filename)
        src =f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
        dst =f"{folder}/{dst}"

        # rename() function will
        # rename all the files
        os.rename(src, dst)
