import os

fromDir = input("From (absolute path): ")
toDir = input("To (absolute path): ")

for subdir, dirs, files in os.walk(fromDir):
    for file in files:
        print(os.path.join(subdir, file))
