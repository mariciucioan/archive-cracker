import os
from pathlib import Path

from termcolor import colored
import zipfile

from os.path import exists

import sys

import pyzipper

import cracker

import utils

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

def print_password(val):
    if val is None:
        print(colored('[-] PASSWORD NOT FOUND', 'red'))
    else:
        print(colored('[+] FOUND PASSWORD: %s' % val, 'green'))

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
                if zipfile.is_zipfile(param2) and os.path.isfile(param2):
                    try:
                        param3 = sys.argv[3].lower()
                        if param3 == 'brute':
                            try:
                                val = cracker.brute_force_attack_multi_thread(zipFile=param2, max_len=10)
                                print_password(val)
                            except Exception as e:
                                print(e)
                        elif param3 == 'dictionary':
                            try:
                                param4 = sys.argv[4]
                                if exists(param4):
                                    val = cracker.dictionary_attack(param2, param4)
                                    print_password(val)
                                else:
                                    print(colored("@param4 file does not exist", 'red'))
                            except:
                                val = cracker.dictionary_attack(param2)
                                print_password(val)
                    except:
                        print(colored("@param3 not valid/does not exist", 'red'))
                else:
                    print(colored('@param2 error', 'red'))
            except:
                print(colored("@param2 is not a zip file/does not exist", 'red'))
        else:
            print(colored('@param1 not valid/does not exist', 'red'))