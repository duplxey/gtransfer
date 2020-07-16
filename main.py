import os

allowed_extensions = [
    "png",
    "jpg",
    "jpeg",
]

from_dir = input("From (absolute path): ")
to_dir = input("To (absolute path): ")

print("Searching for files...")

found_files = set()
all_files_amount = 0

for subdir, dirs, files in os.walk(from_dir):
    for file in files:
        full_path = os.path.join(subdir, file)
        filename, file_extension = os.path.splitext(file)
        all_files_amount += 1
        if (file_extension.replace(".", "")) in allowed_extensions:
            print(filename + " > " + file_extension + " (" + full_path + ")")
            found_files.add(full_path)

if len(found_files) == 0:
    exit("Could not find any files.")

print("Found", len(found_files), "matching files files (out of", all_files_amount, ").")
