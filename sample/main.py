from pathlib import Path

from termcolor import colored
import zipfile

from os.path import exists

import sys

import pyzipper

import cracker

f_name = sys.argv[0]
how_to = ''' You need to specify parameters.

 @param1: terminal/gui
 @param2: file path (only for terminal use)
 @param3: attack method (brute/dictionary)
 @param4: path to dictionary (optional & use only for dictionary attack)
 
 e.g sessions: 
    py -3.9 %s gui
    py -3.9 %s terminal "C:\..\\file.zip" brute
    py -3.9 %s terminal "C:\..\\file.zip" dictionary
    py -3.9 %s terminal "C:\..\\file.zip" dictionary "C:\..\custom_dictionary.txt"
''' % (f_name, f_name, f_name, f_name)

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print(colored(how_to, 'green'))
    else:
        param1 = sys.argv[1].lower()

        if(param1 == 'gui'):
            pass
            #GUI().run()
        elif(param1 == 'terminal'):
            try:
                param2 = sys.argv[2]
                if zipfile.is_zipfile(param2):
                    try:
                        param3 = sys.argv[3].lower()
                        if param3 == 'brute':
                            pass # implement brute attack for file
                        elif param3 == 'dictionary':
                            try:
                                param4 = sys.argv[4]
                                if exists(param4):
                                    pass # implement dictionary attack for file
                                else:
                                    print(colored("@param4 file does not exist", 'red'))
                            except:
                                val = cracker.dictionary_attack(param2)
                                if val is None:
                                    print(colored('Password not found', 'red'))
                                else:
                                    print(colored('Password: %s' % val))
                    except:
                        print(colored("@param3 not valid/does not exist", 'red'))
            except:
                print(colored("@param2 is not a zip file/does not exist", 'red'))
        else:
            print(colored('@param1 not valid/does not exist', 'red'))