from os import listdir, path, mkdir
from shutil import move



class extention():
    #A class that checks for extentions
    @staticmethod
    def read(name):
        backwards = name[::-1]
        for i in range(len(backwards)):
            if backwards[i] == "." and backwards[i] != backwards[-1]:
                extention_name_backwards = backwards[0:i]
                extention_name_fixed = extention_name_backwards[::-1]
                return extention_name_fixed
        return "none"


def sort():
    global item_path_dict
    item_path_dict = {}

    is_path_valid = False
    while not is_path_valid:
        dir_path = input("enter folder path: (./X/Y/Z) \n")
        if path.isdir(dir_path):
            is_path_valid = True
        


    if dir_path[-1] == "/":
        dir_path = dir_path[:-1]
        print(dir_path)

    items_in_dir = set(listdir(dir_path))

    #Checking wether the sorting folders exist and creating them if not
    sorting_folders = {"Videos", "Pictures", "Text_Files", "etc"}
    for folder in sorting_folders:
        if folder not in items_in_dir:

            mkdir(f"{dir_path}/{folder}")
            print("the path did not include /")


    for file in items_in_dir:
        file_extention = extention.read(file)
        file_extention = file_extention.lower()
        is_file_dir = path.isdir(f"{dir_path}/{file}")

        if not is_file_dir and (file_extention == "png" or file_extention == "jpg" or file_extention == "gif"):
            move(f"{dir_path}/{file}", f"{dir_path}/Pictures")
            item_path_dict[file] = "Pictures"

        elif not is_file_dir and (file_extention == "mp4" or file_extention == "mov" or file_extention == "mkv"):
            move(f"{dir_path}/{file}", f"{dir_path}/Videos")
            item_path_dict[file] = "Videos"

        elif not is_file_dir and (file_extention == "txt" or file_extention == "py" or file_extention == "html"):
            move(f"{dir_path}/{file}", f"{dir_path}/Text_Files")
            item_path_dict[file] = "Text_Files"

        elif not is_file_dir:
            move(f"{dir_path}/{file}", f"{dir_path}/etc")
            item_path_dict[file] = "etc"


def items_search():
    while True:
        item_keys_values = item_path_dict
        item = input("input file name here (include extention)")
        if item in item_keys_values:
            print(item_keys_values[item])
        elif item == "break":
            break
        else:
            print("couldn't find item")



sort()
items_search()
