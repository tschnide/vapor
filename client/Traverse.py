import os
try:
    from os import scandir, walk, mkdir
    from shutil import copyfile, copytree, rmtree
except ImportError:
    from scandir import scandir, walk, mkdir


class Traverse:

    def __init__(self, target_directory):
        self.target_directory = target_directory

    def print_dir_tree(self, get_root_dir):
        # the other packing is there because I don't care about the list of subdirectories.
        for dir_path, *other, file_list in os.walk(self.target_directory, topdown=True):
            print(get_root_dir(dir_path))
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

    # Just for learning how this works right now
    def copy(self):
        copytree("/Users/Schnider/Desktop/vapor/test_root",
                 "/Users/Schnider/Desktop/vapor/dest_root")

    # Delete this later it's just for testing
    def clear_dest_root(self):
        try:
            rmtree("dest_root/")
            print("Directory deleted.")
        except OSError:
            print("The directory was not deleted.")

    # Delete this later it's just for testing
    def create_dest_root(self):
        try:
            mkdir("/Users/Schnider/Desktop/vapor/dest_root")
            print("Directory created.")
        except OSError:
            print("The directory was not created.")


s1 = Traverse("/Users/Schnider/Desktop/vapor/test_root")
s1.clear_dest_root()
# s1.get_root_dir("/Users/Schnider/Desktop/vapor/test_root")
# s1.copy()
