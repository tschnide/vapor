import os
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk


class Scanner:

    def __init__(self, target_directory):
        self.target_directory = target_directory

    def get_file_names(self):
        for root, dirs, files in os.walk(self.target_directory):
            for directory_name in dirs:
                print(directory_name)
            for file_name in files:
                print(file_name)


s1 = Scanner("/Users/Schnider/Desktop/vapor")
print(s1.get_file_names())
