import pyzipper

import terminal

from sys import argv
from os import remove
from pyzipper import is_zipfile

if __name__ == "__main__":
    argv_count = len(argv)
    if argv_count < 3:
        terminal.how_to()
    else:
        my_file = argv[1]
        if is_zipfile(my_file):
            # noinspection PyBroadException
            try:
                with pyzipper.AESZipFile(my_file, 'r') as archive:
                    archive.extractall()
                    for file in archive.namelist():
                        remove(file)

                print("The archive is not password protected!")
            except:
                method = argv[2].lower()
                if method == 'brute':
                    terminal.brute(my_file)
                elif method == 'dictionary':
                    terminal.dictionary(my_file)
        else:
            terminal.how_to()
