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

    def get_root_dir(self, path):
        x = -1
        p = list(path)
        reversed_root_name = ""

        while path[x] != "/":  # Could be a problem in Windows where the slashes are reversed
            # These get added beginning at the end so they are reversed
            reversed_root_name = reversed_root_name + p[x]
            x = x - 1

        # This trick reverses it (so it's back to being forward)
        corrected_root_name = reversed_root_name[::-1]
        # print(root_name)
        return corrected_root_name


s1 = Scanner("/Users/Schnider/Desktop/vapor/test_root")
# s1.print_dir_tree()
p1 = "/Users/Schnider/Desktop/vapor/test_root"
print(s1.get_root_dir(p1))
