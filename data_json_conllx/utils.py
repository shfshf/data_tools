import os
import pathlib


def remove_files_in_dir(data_dir):
    input_file_list = [i.absolute() for i in pathlib.Path(data_dir).iterdir() if i.is_file()]
    for i in input_file_list:
        os.remove(i)