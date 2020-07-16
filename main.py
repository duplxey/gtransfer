import os
from shutil import copyfile
import ntpath

hr = "================================================="
welcome = """         ______                      ____         
   ____ /_  __/________ _____  _____/ __/__  _____
  / __ `// / / ___/ __ `/ __ \/ ___/ /_/ _ \/ ___/
 / /_/ // / / /  / /_/ / / / (__  ) __/  __/ /    
 \__, //_/ /_/   \__,_/_/ /_/____/_/  \___/_/     
/____/ Bulk copy specific filetypes with ease."""

print(welcome)
print(hr)

allowed_extensions = [
    "png",
    "jpg",
    "jpeg",
]

from_dir = input("Source folder: ")
to_dir = input("Destination folder: ")

print("Searching for files...")

matching_files = set()
all_files_amount = 0

for subdir, dirs, files in os.walk(from_dir):
    for file in files:
        full_path = os.path.join(subdir, file)
        filename, file_extension = os.path.splitext(file)
        all_files_amount += 1
        if (file_extension.replace(".", "")) in allowed_extensions:
            print(filename + " > " + file_extension + " (" + full_path + ")")
            matching_files.add(full_path)

if len(matching_files) == 0:
    exit("Could not find any files.")

print("Found", len(matching_files), "matching files files (out of", all_files_amount, ").")

proceed = input("Press 'y' to copy the files: ")

if proceed != 'y':
    print("Cancelling the operation.")

print("Started the copy process...")

for matching_file in matching_files:
    print("Copying " + matching_file)
    copyfile(matching_file, to_dir + ntpath.basename(matching_file))

print("Copy process completed.")
