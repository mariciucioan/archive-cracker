from sys import argv
from os.path import exists
from termcolor import colored
from cracker import dictionary_attack, brute_force_attack_multi_thread

how_to_text = ''' You need to specify parameters.

 @param1: file path (only for terminal use)
 @param2: attack method (brute/dictionary)
 @param3[dictionary/optional]: path to dictionary

 e.g sessions: 
    py -3.9 %s "C:\..\\file.zip" brute
    py -3.9 %s "C:\..\\file.zip" dictionary
    py -3.9 %s "C:\..\\file.zip" dictionary "C:\..\custom_dictionary.txt"
''' % (argv[0], argv[0], argv[0])


def brute(file):
    val = brute_force_attack_multi_thread(zip_file=file, max_len=10)
    print_password(val)


# noinspection PyBroadException
def dictionary(file):
    val = None

    try:
        custom_dictionary = argv[3]
        if exists(custom_dictionary):
            val = dictionary_attack(file, custom_dictionary)
        else:
            print(colored(" [-] ERROR: CUSTOM DICTIONARY NOT FOUND", 'red'))
    except:
        val = dictionary_attack(file)

    print_password(val)


def how_to():
    print(colored(how_to_text, 'green'))


def print_password(val):
    if val is None:
        print(colored('[-] PASSWORD NOT FOUND', 'red'))
    else:
        print(colored('[+] FOUND PASSWORD: %s' % val, 'green'))
