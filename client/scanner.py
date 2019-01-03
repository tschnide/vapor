import os
try:
    from os import scandir, walk
except ImportError:
    from scandir import scandir, walk


class Scanner:

    def __init__(self, target_directory):
        self.target_directory = target_directory

    def print_dir_tree(self):
        # the other packing is there because I don't care about the list of subdirectories.
        for dir_path, *other, file_list in os.walk(self.target_directory, topdown=True):
            print("Path - " + dir_path)
            for file_name in file_list:
                print(file_name)


s1 = Scanner("/Users/Schnider/Desktop/vapor/test_root")
s1.print_dir_tree()
