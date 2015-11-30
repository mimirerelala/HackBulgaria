import os
import sys

def main():
    if len(sys.argv) > 1:
        folder = sys.argv[1]
    else:
        folder = os.getcwd()
    full_size = 0
    for each_tuple in os.walk(folder):
        (path, dirs, files) = each_tuple
        for cur_file in files:
            full_name_path = path + os.path.sep  + cur_file
            print(full_name_path, os.path.getsize(full_name_path))
            full_size += os.path.getsize(full_name_path)
    print("The size of %s is %4f KB" % (folder, full_size/1024))
    return full_size/1024

if __name__ == '__main__':
    main()
