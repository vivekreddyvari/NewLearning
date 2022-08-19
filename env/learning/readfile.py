#imports
import csv
import os
from pathlib import Path


class ReadFile:
    """ This procedure reads any file from any folder

        Inputs: File
        Outputs: FileData and FileType

    """

    def __init__(self, file_name):
        self._file_name = file_name
        self.path_default = os.path.abspath('')

    def __str__(self):
        return f"{self._file_name}"

    def directory_of_file(self):
        """
        This procedure finds input files directory and path
        Returns: directory of the file

        """
        obj_list = os.listdir(self.path_default)
        dir_name = []
        fil_name = []
        for f_name in obj_list:
            obj_name = Path(f_name).name
            if Path(f_name).is_dir():
                dir_name.append(obj_name)
            else:
                fil_name.append(obj_name)
        if self._file_name in fil_name:
            directory_of_file = self.path_default
            print(directory_of_file, self._file_name)
        else:
            directory_of_file = self.file_searcher(dir_name, self._file_name)

        return directory_of_file

    def file_searcher(self, dir_path, f_name):
        """
        Search the file from sub directories of a directory of the path

        Returns:
            input = directory_path
                    file_name
            output = path_setting
        """
        for directory_name in dir_path:
            path_setting = self.path_default + '/' + directory_name
            try:
                if f_name in os.listdir(path_setting):
                    return path_setting
            except FileNotFoundError as ex:
                print(f"{f_name} {ex}")

    def file_types(self):
        """
        Types of Extensions of files available in file directory
        Returns:

        """
        path = self.directory_of_file()
        file_types = []
        for file in os.listdir(path):file_types.append(Path(file).suffix)
        return file_types

    def read_file(self, file_type):
        """
        Reads a file, based on type
        Returns:
            output of the file

        """
        if file_type in self.file_types():
            # names = [name for name in os.listdir(self.file_directory())]
            names = [name for name in os.listdir(self.directory_of_file())]
            for name in names:
                # name_of_file = self.file_directory() + '/' + name\
                name_of_file = self.directory_of_file() + '/' + name
                if Path(name).suffix == '.txt':
                    with open(name_of_file, 'r') as f:
                        data = f.read()
                        return data
        else:
            raise Exception(f'Type of `{file_type}` file not found')




# reading a file

r = ReadFile('example.txt')
# print(dir(r))
print(r.read_file('.txt'))
print(str(r))
print(dir(r))
print(r.file_types())

csv_read_file = ReadFile('data.csv')
print(csv_read_file.read_file('.csv'))
print(str(csv_read_file))



